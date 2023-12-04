import factory

from taggit.models import Tag


class TagFactory(factory.django.DjangoModelFactory):
    """
    Factory to create instance of a Tag for ``django-taggit``.
    """
    name = factory.Sequence(lambda n: "Tag {0}".format(n))
    slug = factory.Sequence(lambda n: "tag-{0}".format(n))

    class Meta:
        model = Tag
        skip_postgeneration_save = True
