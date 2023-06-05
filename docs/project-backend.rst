.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Project composer: https://project-composer.readthedocs.io/en/latest/
.. _django-configurations: https://django-configurations.readthedocs.io/en/stable/

.. _intro_project_backend:

=======
Backend
=======

Backend base dependencies
*************************

.. bireli-backend-stack::


Database
********

A project is meant to work with different database drivers, at least PostgreSQL and
SQlite. SQlite is used for development and test environments. PostgreSQL is used in
all other deployment, especially production.

Settings
********

Project settings are defined using the `django-configurations`_ way, it means within
a class. There is no more monolithic settings files.

There is two settings files kinds:

Application settings
    Each application can have a settings file located in application module in composer
    repository. This is where you will configure all application settings.

Environment settings
    They are located in ``project/settings/`` and their goal is to override some
    application settings to fit some special environment requirements.


.. _project_backend_local_settings:

Local settings
--------------

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
.....

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
........

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
            #"debug_toolbar.panels.history.HistoryPanel",
            "debug_toolbar.panels.versions.VersionsPanel",
            "debug_toolbar.panels.timer.TimerPanel",
            "debug_toolbar.panels.settings.SettingsPanel",
            "debug_toolbar.panels.headers.HeadersPanel",
            "debug_toolbar.panels.request.RequestPanel",
            "debug_toolbar.panels.sql.SQLPanel",
            "debug_toolbar.panels.staticfiles.StaticFilesPanel",
            "debug_toolbar.panels.templates.TemplatesPanel",
            "debug_toolbar.panels.cache.CachePanel",
            #"debug_toolbar.panels.signals.SignalsPanel",
            #"debug_toolbar.panels.redirects.RedirectsPanel",
            #"debug_toolbar.panels.profiling.ProfilingPanel",
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


.. _project_backend_newapp:

Developing a new application
****************************

A Makefile task exists to help you to quickly start a new application into your
project, just use: ::

    make new-app

It will prompt you for a full title that will be used to build proper Python names
(using slugify) and generate everything (composer application module, Django
application module, etc..).

Once done the command outputs a resume and a some help to enable your new application.


Add a new third party application
*********************************

To add a new package for an already enabled application just put it in
application requirement file and configure it in its settings file. For example, a CMS
plugin should live in the CMS application settings.

But sometime a third party application may be shared by many applications, in this case
it will needs its own composer application module.

You may copy an other application module and edit it or use the command from
:ref:`project_backend_newapp` and just keep the composer application folder.


.. _project_backend_env_requirements:

Environment Requirements
************************

Environment requirements are divided into multiple files because each environment may
not use everything and so does not install everything.

.. Warning::
   Don't edit these files and prefer to add your requirements through a composer
   application to keep project well structured.

``composer.txt``
    This is for the composer requirement itself which is appart from the backend base
    requirements.

    It is required by every environment.

``base_template.txt``
    This is a template used by composer to generate again the base requirements file,
    do not edit it.

    It is not required directly by any environment.

``base.txt``
    This is the base project requirements. Don't write anything in it since it
    generated from composer, all you changes will be lost definitively.

    It is required by every environment.

``development.txt``
    This is for requirements used to run test and other quality check.

    It is required by environments that need to run tests and quality check.

``production.txt``
    This is for requirements used to serve project, specify a proper SGBD driver, etc..

    It is only required by all "non-local" environments that need to serve and run
    project.

``codestyle.txt``
    This is extra requirements in local environment to check and apply linters on code.

    It is not required by any environment. However it is installed in local
    environment.

``toolbox.txt``
    This is extra requirements in local environment for some common helpful tools for
    debugging.

    It is not required by any environment. However it is installed in local
    environment.

.. Note::
   Project does not include extra requirements configurations. You will need to enable
   and configure them through your :ref:`project_backend_local_settings`.


.. _project_backend_i18n:

Internationalization and localization
*************************************

This is mostly driven by settings and URLs. Bireli as already set everything (following
option choices when creating project), this means:

Default language
    The default language used to write contents (templates, text in code and content
    in applications that implement it).

    It is used even in single language site but does not really have consequences,
    except for text translation from PO catalog files (at least used in Django admin).

    Be aware that application contents store the language it has been written with, so
    if you change default language on a single language site, you may not see your
    content anymore (but they should not be lost).

    Default language value is defined in ``settings.LANGUAGE_CODE`` from
    ``django_builtins`` module in composition repository.

Available languages
    All other languages that are available for translation and application contents. At
    least it must contains the default language, this will leads to a single language
    site.

    If you enable more language it turns project to a multiple language site,
    this is only about translations and application contents then you will need to
    enable i18n urls also (see next parts).

    Available languages are defined in ``settings.LANGUAGES`` from
    ``django_builtins`` module in composition repository.

Timezone
    The default assumed timezone that will be used to determine date and time formatting
    in default language and also used to write date and time in content applications.

    It has already been set by Bireli according to the default language option but you
    may change it further to a more accurate one if needed.

    Timezone value is defined in ``settings.TIME_ZONE`` from ``django_builtins`` module
    in composition repository.

Usage of i18n URLs
    This determines if your application urls will be prefixed with language like ``/en/``
    or not.

    Commonly if you have a single language site, you don't need it and it is disabled
    and a multiple language site enables it.

    For Django it is just materialized with usage of ``i18n_patterns()`` and
    middleware ``django.middleware.locale.LocaleMiddleware`` enabled. If they are both
    unused, project is a single language site.

    Note that application from composition repository should implement a switch to use
    i18n urls or not, depending from an internal setting ``settings.ENABLE_I18N_URLS``
    from ``django_builtins`` so you should only have to set this setting to True,
    however you have to enable middleware ``LocaleMiddleware`` yourself. Obviously this
    behavior is only suitable with applications that implement i18n.

Finally, knowing these parts, you should be able to easily switch project configuration
to turn it to a single language site or a multiple language site.
