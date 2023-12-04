import factory

from django.conf import settings
from django.utils.text import slugify

from cms import models as cms_models
from cms.utils import get_current_site

from .auth import UserFactory


class TitleFactory(factory.django.DjangoModelFactory):
    """
    Create a proper Title object for a CMS page.
    """

    page = None
    title = factory.Faker("catch_phrase")

    class Meta:
        model = cms_models.Title
        skip_postgeneration_save = True

    @factory.lazy_attribute
    def language(self):
        """
        Default language is defined from settings.

        This is a lazy attribute to avoid to be evaluated on definition and be able
        to override it from test.
        """
        return settings.LANGUAGE_CODE

    @factory.lazy_attribute
    def path(self):
        """
        Path is automatically build from 'slug'+'language'
        """
        return self.page.get_path_for_slug(self.slug, self.language)

    @factory.lazy_attribute
    def slug(self):
        """
        Slug is automatically build from 'title'
        """
        return slugify(self.title)

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        """
        Update the related page's languages.
        """
        super()._after_postgeneration(instance, create, results=results)
        page = instance.page
        if page:
            page_languages = page.get_languages()

            if instance.language not in page_languages:
                page.update_languages(page_languages + [instance.language])


class PageFactory(factory.django.DjangoModelFactory):
    """
    TODO: Create a proper CMS page with possible Title translations.
    """

    title = factory.RelatedFactory(TitleFactory, "page")
    in_navigation = True
    login_required = False

    # Utility fields that are used in attribute methods but not given to model
    # constructor (since they are not valid fields).
    parent = None
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = cms_models.Page
        exclude = ["parent", "user"]
        skip_postgeneration_save = True

    @factory.lazy_attribute
    def changed_by(self):
        """
        Changed_by is automatically build from 'username'
        """
        return slugify(self.user.username)

    @factory.lazy_attribute
    def created_by(self):
        """
        Created_by is automatically build from 'username'
        """
        return slugify(self.user.username)

    @factory.lazy_attribute
    def node(self):
        """
        Create a node for the page (under its parent if applicable).
        """
        site = get_current_site()
        new_node = cms_models.TreeNode(site=site)

        if self.parent:
            return self.parent.node.add_child(instance=new_node)

        return cms_models.TreeNode.add_root(instance=new_node)

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        """
        This hook method is called last when generating an instance from a factory. The
        super method saves the instance one last time after all the "post_generation"
        hooks have played.

        This is the moment to finally publish the pages. If we published the pages
        before this final "save", they would be set back to a pending state and would
        not be in a clean published state.
        """
        super()._after_postgeneration(instance, create, results=results)
        instance.rescan_placeholders()

        if results.get("should_publish", False):
            for language in instance.get_languages():
                instance.publish(language)

            instance.get_public_object().rescan_placeholders()

        instance.refresh_from_db()

    @factory.post_generation
    def should_publish(obj, create, extracted, **kwargs):
        """
        Mark the page for publishing.

        The actual publishing is done by the ``_after_post_generation`` hook method.
        """
        if create and extracted:
            return True

        return False

    @factory.post_generation
    def set_homepage(obj, create, extracted, **kwargs):
        """
        Define page as a homepage.
        """
        if create and extracted:
            obj.set_as_homepage()

            return True

        return False

    @factory.post_generation
    def reverse_id(obj, create, extracted, **kwargs):
        """
        Define the page 'reverse_id' attribute.

        This is only for a create strategy.

        If extracted is True, this will copy the Page title slug, be careful that a
        slug is not unique among pages, so it is not safe.

        Else if extracted is not empty its value will be used to fill the attribute,
        obviously the value must be a String.
        """
        if create:
            if extracted is True:
                obj.reverse_id = obj.get_slug()
                obj.save()
            elif extracted:
                obj.reverse_id = extracted
                obj.save()

        return None

    @factory.post_generation
    def add_translations(obj, create, extracted, **kwargs):
        """
        Create Title translations for this page.
        """
        # Assert that the languages passed are declared in settings
        enabled_languages = [code for code, name in settings.LANGUAGES]
        existing_languages = obj.get_languages()

        if create and extracted:
            for language, title in extracted.items():
                if language not in enabled_languages:
                    msg = (
                        "You can't translate page in a language that are not declared "
                        "from 'settings.LANGUAGES': {}"
                    )
                    raise ValueError(msg.format(language))

                elif language in existing_languages:
                    msg = (
                        "A translation with language '{}' has already been created "
                        "for this Page."
                    )
                    raise ValueError(msg.format(language))

                TitleFactory(
                    language=language,
                    title=title,
                    slug=slugify(title),
                    page=obj,
                )


def get_extended_object_payload(cls):
    """
    Helper to build Page payload for ``extended_object`` attribute with
    ``CMSExtensionAbstractFactory`` or its inheriters.

    This function can not live as a factory method since it won't be available from
    returned model object but we need to factorize it. So it lives as a function
    helper.

    Arguments:
        cls (object): The built object from factory, commonly the ``self`` argument
            given to the lazy attribute method.

    Returns:
        dict: Built payload.
    """
    payload = {}

    if hasattr(cls, "page_template"):
        payload["template"] = cls.page_template

    if hasattr(cls, "page_parent"):
        payload["parent"] = cls.page_parent

    if hasattr(cls, "page_title"):
        payload["title__title"] = cls.page_title

    if hasattr(cls, "page_language"):
        payload["title__language"] = cls.page_language
    else:
        payload["title__language"] = settings.LANGUAGE_CODE

    if hasattr(cls, "page_translations"):
        payload["add_translations"] = cls.page_translations

    return payload


class CMSExtensionAbstractFactory(factory.django.DjangoModelFactory):
    """
    Abstract factory to inherit from to implement an CMS extension factory.

    DjangoCMS extension reference:

    https://docs.django-cms.org/en/latest/how_to/extending_page_title.html

    .. Note::
        Since an extension factory won't be able to know if it creates a Page or Title
        factory, we need more concrete abstraction which implement a proper
        ``extended_object`` lazy attribute method to return the right object (Page or
        Title).

        So this abstract only implement methods that can be compatible to both objects
        but is not ready to make a proper factory.

        Commonly you will prefer to inherit directly from either
        ``PageExtensionAbstractFactory`` or ``TitleExtensionAbstractFactory`` from
        your extension factory.
    """
    class Meta:
        abstract = True
        skip_postgeneration_save = True

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        """
        Hook method that is called last when generating an instance from a factory.

        The super method saves the instance one last time after all the
        "post_generation" hooks have played. this is the moment to finally publish the
        pages. If we published the pages before this final "save", they would be set
        back to a pending state and would not be in a clean published state.
        """
        if results.get("should_publish", False):
            # Get the page object to trigger publication
            # Either we extend Title object so we need to get it from attribute
            if hasattr(instance.extended_object, "page"):
                page = instance.extended_object.page
            # Or this we just extend a Page object
            else:
                page = instance.extended_object

            available_languages = page.get_languages()

            for language in available_languages:
                page.publish(language)

        instance.refresh_from_db()

    @factory.post_generation
    def should_publish(self, create, extracted, **kwargs):
        """
        Mark object for publishing.

        Effective publication will be donne by the ``_after_post_generation`` hook
        method.
        """
        if create and extracted:
            return True
        return False


class PageExtensionAbstractFactory(CMSExtensionAbstractFactory):
    """
    Abstract factory to inherit from to create a CMS Page Extension.

    Described attributes are optional attributes to control Page creation, you need
    to exclude them from your concrete factory with ``Meta.exclude``. If you need more
    control on Page attributes, you will need to craft a Page yourself in pass it
    directly as the ``extended_object`` argument.

    Attributes:
        page_template (string): Page template path to define.
        page_title (string): Page title to define.
        page_language (string): Page language to define.
        page_parent (Page): Parent page to link to page.
        page_translations (dict): Dictionnary of translations as supported from
            ``PageFactory.add_translations``.
    """
    class Meta:
        abstract = True

    @factory.lazy_attribute
    def extended_object(self):
        """
        Automatically create a related Page object.

        Returns:
            Page: Created random Page as expected from Page extension.
        """
        page_payload = get_extended_object_payload(self)
        return PageFactory(**page_payload)


class TitleExtensionAbstractFactory(CMSExtensionAbstractFactory):
    """
    Abstract factory to inherit from to create a CMS Title Extension.

    Described attributes are optional attributes to control Page creation, you need
    to exclude them from your concrete factory with ``Meta.exclude``. If you need more
    control on Page attributes, you will need to craft a Page yourself in pass it
    directly as the ``extended_object`` argument.

    Attributes:
        page_template (string): Page template path to define.
        page_title (string): Page title to define.
        page_language (string): Page language to define.
        page_parent (Page): Parent page to link to page.
        page_translations (dict): Dictionnary of translations as supported from
            ``PageFactory.add_translations``.
    """
    class Meta:
        abstract = True

    @factory.lazy_attribute
    def extended_object(self):
        """
        Automatically create a related Page object.

        Returns:
            Title: Created random Title as expected from Page extension.
        """
        page_payload = get_extended_object_payload(self)

        page = PageFactory(**page_payload)
        return page.get_title_obj(page_payload["title__language"])
