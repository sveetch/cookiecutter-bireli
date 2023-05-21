import base64

from django.conf import settings
from django.contrib.sites.models import Site

from project import __version__


def get_site_metas(with_static=False, with_media=False, is_secure=False,
                   extra={}):
    """
    Return metas from the current *Site* and settings

    Added Site metas will be callable in templates like this
    ``SITE.name``

    This can be used in code out of a Django requests (like in management
    commands) or in a context processor to get the *Site* urls.

    Default metas returned :

    * PROJECT_RELEASE: Current project release version;
    * SITE.name: Current *Site* entry name;
    * SITE.domain: Current *Site* entry domain;
    * SITE.web_url: The Current *Site* entry domain prefixed with the http
      protocol like ``http://mydomain.com``. If HTTPS is enabled 'https' will
      be used instead of 'http';
    * SITE.scheme: Either return ``https`` or ``http`` depending ``is_secure``
      argument is true or not;

    Optionally it can also return ``STATIC_URL`` and ``MEDIA_URL`` if needed
    (like out of Django requests).
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
        "PROJECT_RELEASE": __version__,
        "PROJECT_RELEASE_BASE64": base64.urlsafe_b64encode(
            __version__.encode("utf-8")
        ).decode("utf-8"),
    }

    if with_media:
        metas["MEDIA_URL"] = getattr(settings, "MEDIA_URL", "")

    if with_static:
        metas["STATIC_URL"] = getattr(settings, "STATIC_URL", "")

    metas.update(extra)
    return metas


def site_metas(request):
    """
    Context processor to add the current Site metas to the context
    """
    return get_site_metas(is_secure=request.is_secure())
