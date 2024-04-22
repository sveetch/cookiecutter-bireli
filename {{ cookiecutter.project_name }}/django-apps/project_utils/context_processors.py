import base64

from django.conf import settings
from django.contrib.sites.models import Site

from project import __version__


def get_site_metas(with_static=False, with_media=False, is_secure=False, extra={}):
    """
    Return meta informations from project and the current Site object.

    This can be used in code out of a Django requests (like in management
    commands) or in a context processor to get the Site url.

    Return informations (typed as they would be used from a template):

    SITE.name
        Current *Site* entry name.
    SITE.domain
        Current *Site* entry domain.
    SITE.web_url
        The Current *Site* entry domain prefixed with the http protocol like
        ``http://mydomain.com``. If HTTPS is enabled 'https' will be used instead of
        'http'.
    SITE.scheme
        Either return ``https`` or ``http`` depending ``is_secure`` argument is true
        or not.
    PROJECT.release
        Current project release version.
    PROJECT.release_base64
        Current project release version encoded in base64.
    PROJECT.enable_i18n_urls
        Determine if project enable i18n urls or not. Value depends from
        ``settings.ENABLE_I18N_URLS``.
    PROJECT.index_metas
        Determine if project enable meta element for site indexation. Value depends
        from ``settings.SITE_INDEX_METAS``.

    It can have also ``STATIC_URL`` and ``MEDIA_URL`` variable if enabled from
    arguments.

    And optionally there can be extra variables from setting ``EXTRA_SITE_METAS``, its
    content will be available in 'EXTRA' context variable.

    .. Warning:
        Don't add any secret variable here since it is widely exposed and may even
        be displayed from view ``ExposedSiteMetasView``. This would be a major security
        breach.

    Keyword Arguments:
        with_static (boolean): If True adds ``STATIC_URL`` to returned dict. Default
            is False.
        with_media (boolean): If True adds ``MEDIA_URL`` to returned dict. Default
            is False.
        is_secure (boolean): If True the site url will be in ``https``. Default
            is False.
        extra (dict): Additional variables to add. This update the whole main data
            dictionnary so you should not use ``SITE``, ``PROJECT`` item names else it
            would lost their original content. This is another possibility to add extra
            data in addition to the ``EXTRA`` part.

    Returns:
        dict: Meta informations.
    """
    site_current = Site.objects.get_current()

    if is_secure:
        scheme = "https"
    else:
        scheme = "http"

    metas = {
        "SITE": {
            "name": site_current.name,
            "domain": site_current.domain,
            "web_url": "{}://{}".format(scheme, site_current.domain),
            "scheme": scheme,
        },
        "PROJECT": {
            "release": __version__,
            "release_base64": base64.urlsafe_b64encode(
                __version__.encode("utf-8")
            ).decode("utf-8"),
            "enable_i18n_urls": getattr(settings, "ENABLE_I18N_URLS", False),
            "index_metas": getattr(settings, "SITE_INDEX_METAS", False),
        },
    }

    if with_media:
        metas["MEDIA_URL"] = getattr(settings, "MEDIA_URL", "")

    if with_static:
        metas["STATIC_URL"] = getattr(settings, "STATIC_URL", "")

    if getattr(settings, "EXTRA_SITE_METAS", None):
        metas["EXTRA"] = getattr(settings, "EXTRA_SITE_METAS")

    metas.update(extra)

    return metas


def site_metas(request):
    """
    Context processor to add the current Site metas to the context.

    Args:
        request (object): A Django Request object.

    Returns:
        dict: Meta informations to add to template context.
    """
    return get_site_metas(is_secure=request.is_secure())
