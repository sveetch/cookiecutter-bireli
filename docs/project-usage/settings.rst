.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Project composer: https://project-composer.readthedocs.io/en/latest/
.. _django-configurations: https://django-configurations.readthedocs.io/en/stable/

.. _intro_backend_settings:

========
Settings
========

Project settings are defined using the `django-configurations`_ way, it means within
a class. There is no monolithic file which would hold every settings.

There is two setting file kinds:


.. _project_backend_app_settings:

Application settings
********************

Each application can have a settings file located in its own application module
directory in the composer repository (``composition_repository/``).

This is where you will configure all application settings.

.. Note::
    Sometime, an application module from composer repository can gather multiple
    third party applications when they not meant to be shared with other
    applications.


.. _project_backend_env_settings:

Environment settings
********************

They are located in ``project/settings/`` and their unique goal is to override some
application settings to fit some special environment requirements.

.. Warning::
    Environment settings must only include some settings override dedicated to the
    environment needing. It is not the place where you will configure an
    application.

We currently have the following environment:

* ``base`` that is the base settings shared to other environment. This environment
  is not meant to be used directly. Some of these settings are configured to aim
  production environment for some security reasons;
* ``development`` that is the environment you will use when running Django locally.
  This is the most commonly used one.
* ``test`` that is the environment used when running test suite;
* ``production`` that is the environment to be used with a deployed project.

And then the optional local environment, see :ref:`project_backend_local_settings`
for details.

.. _project_backend_local_settings:

Local settings
**************

A special environment settings can be used to add or override settings for your own
local purpose only. This is useful when you need to use some special things like
debugging tools, database configuration, etc..

This settings file does not exists yet and you must create it to
``project/settings/localsettings.py``.

.. Note::
   Alike all project settings files (from composer applications and environments), this
   local settings file has to be done for the `django-configurations`_ way.

.. Warning::
   This settings file must never be committed to the project repository since it is
   for your own local usage.


Basic
-----

This example is only for basic apps which only need some settings to work.

Here we just enable
`django-extensions <https://django-extensions.readthedocs.io/en/latest/>`_ and disable
cache. Its content should be something like: ::

    from .development import Development


    class LocalEnv(Development):
        # Disable every cache in local development
        CACHES = {
            "default": {
                "BACKEND": "django.core.cache.backends.dummy.DummyCache",
            }
        }

        @classmethod
        def post_setup(cls):
            super(LocalEnv, cls).post_setup()

            cls.INSTALLED_APPS.extend([
                "django_extensions",
            ])

There can only be a single class and it must be named ``LocalEnv`` and inherits from
``Development`` class.


Advanced
--------

Sometime an application needs some settings and to add some urls. Let's demonstrate it
with configuration for both
`django-extensions <https://django-extensions.readthedocs.io/en/latest/>`_ and
`django-debug-toolbar <https://django-debug-toolbar.readthedocs.io/en/latest/>`_.

First the settings file: ::

    from .development import Development


    class LocalEnv(Development):
        ROOT_URLCONF = "project.localurls"

        INTERNAL_IPS = [
            "localhost",
        ]

        DEBUG_TOOLBAR_PANELS = [
            # "debug_toolbar.panels.history.HistoryPanel",
            "debug_toolbar.panels.versions.VersionsPanel",
            "debug_toolbar.panels.timer.TimerPanel",
            "debug_toolbar.panels.settings.SettingsPanel",
            "debug_toolbar.panels.headers.HeadersPanel",
            "debug_toolbar.panels.request.RequestPanel",
            "debug_toolbar.panels.sql.SQLPanel",
            "debug_toolbar.panels.staticfiles.StaticFilesPanel",
            "debug_toolbar.panels.templates.TemplatesPanel",
            "debug_toolbar.panels.cache.CachePanel",
            # "debug_toolbar.panels.signals.SignalsPanel",
            # "debug_toolbar.panels.redirects.RedirectsPanel",
            # "debug_toolbar.panels.profiling.ProfilingPanel",
        ]

        # Disable every cache in local development
        CACHES = {
            "default": {
                "BACKEND": "django.core.cache.backends.dummy.DummyCache",
            }
        }

        @classmethod
        def setup(cls):
            super(LocalEnv, cls).setup()

            cls.MIDDLEWARE = [
                "debug_toolbar.middleware.DebugToolbarMiddleware",
            ] + cls.MIDDLEWARE

        @classmethod
        def post_setup(cls):
            super(LocalEnv, cls).post_setup()

            cls.INSTALLED_APPS.extend([
                "django_extensions",
                "debug_toolbar",
            ])

As you can see we define a new main ``urls.py`` file that will inherit from the base
main one and add some custom urls. Let's create it to ``project/localurls.py``: ::

    from django.urls import include, path

    from project.urls import urlpatterns


    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

Alike the local settings file, this file must never be commited to the repository.


.. _project_backend_settings_django_config:

Django configuration in practice
********************************

A Bireli project use `django-configurations`_ to define settings with classes, in
practice this is achieved either:

As a class attribute
    The easiest way but it's reserved for base application settings because
    it can not use previously defined settings and it can be overwritten from class
    methods (see further).

    Example: ::

        from project_composer.marker import EnabledApplicationMarker


        class SomeAppSettings(EnabledApplicationMarker):
            GREETINGS = "Hello"

    .. Note::
        Inherited class ``EnabledApplicationMarker`` is just a
        `class marker for Composer <https://project-composer.readthedocs.io/en/latest/core/miscellaneous.html#project_composer.marker.EnabledApplicationMarker>`_
        so it knows that this is a class to collect for settings.

    This would result to: ::

        >>> from django.conf import settings
        >>> settings.GREETINGS
        'Hello'

In setup() method
    The common way to extend shared settings.

    Example: ::

        from project_composer.marker import EnabledApplicationMarker


        class SomeAppSettings(EnabledApplicationMarker):
            GREETINGS = "Hello"


        class AnotherAppSettings(EnabledApplicationMarker):
            NAME = " World"

            @classmethod
            def setup(cls):
                super().setup()

                cls.GREETINGS = cls.GREETINGS / cls.NAME

                NOT_A_SETTING = "niet"

    .. Note::
        As you can see in setup method you must define settings as an attribute of
        the class object ``cls``, only class object attributes are assumed as a
        settings and without it the variable won't be available in settings.

        Post setup method have the same constraint.

    This would result to: ::

        >>> from django.conf import settings
        >>> settings.GREETINGS
        'Hello World'
        >>> settings.NOT_A_SETTING
        AttributeError: 'Settings' object has no attribute 'NOT_A_SETTING'


In post_setup() method
    Post setup is a way to computate settings from other settings that
    may have been defined from class attribute or setup() method.

    This may be considered as a last resort solution for shared settings.

    Example: ::

        from project_composer.marker import EnabledApplicationMarker


        class SomeAppSettings(EnabledApplicationMarker):
            GREETINGS = "Hello"


        class AnotherAppSettings(EnabledApplicationMarker):
            NAME = " World"

            @classmethod
            def setup(cls):
                super().setup()

                cls.GREETINGS = cls.GREETINGS + cls.NAME


        class NihilisticAppSettings(EnabledApplicationMarker):
            @classmethod
            def post_setup(cls):
                super().post_setup()

                cls.GREETINGS = "Nope"

    This would result to: ::

        >>> from django.conf import settings
        >>> settings.GREETINGS
        'Nope'

Finally remember that 'django-configuration' class leads to a "one-way cascade". This
means a setting defined in ``setup()`` method won't be overwritten from a class
attribute so at least it will have to be in ``setup()`` method. And it is the same way
with settings from ``post_setup()`` method.

Obviously for a setting defined in the same way in multiple classes this is the last
loaded one that will win, the order of your application composition does matter.
