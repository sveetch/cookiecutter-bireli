.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Project composer: https://project-composer.readthedocs.io/en/latest/
.. _django-configurations: https://django-configurations.readthedocs.io/en/stable/

.. _intro_project_backend:

=======
Backend
=======

Database
--------

A project is meant to work with different database drivers, at least PostgreSQL and
SQlite. SQlite is used for development and test environments. PostgreSQL is used in
all other deployment, especially production.

Settings
--------

Project settings are defined using the `django-configurations`_ way, it means within
a class. There is no more monolithic settings files.

There is two settings files kinds:

Application settings
    Each application can have a settings file located in application module in composer
    repository. This is where you will configure all application settings.

Environment settings
    They are located in ``project/settings/`` and their goal is to override some
    application settings to fit some special environment requirements.

Local settings
..............

A special environment settings can be used to add or override settings for your own
local purpose only. This is useful when you need to use some special things like
debugging tools, database configuration, etc..

This settings file does not exists yet and you must create it to
``project/settings/localsettings.py``. Its content should be something like: ::

    from .development import Development


    class LocalEnv(Development):
        @classmethod
        def post_setup(cls):
            super(LocalEnv, cls).post_setup()

            cls.INSTALLED_APPS.extend([
                "django_extensions",
            ])

There can only be a single class and it must be named ``LocalEnv`` and inherits from
``Development`` class.

.. Warning::
   This settings file must never be committed to the project repository since it is
   for your own local usage. And so it can be used to configure any project application
   that have not been properly configure in it application settings file.


Develop a new application
-------------------------

Use application template `cookiecutter-bireli-newapp <https://github.com/sveetch/cookiecutter-bireli-newapp>`_
that will create everything to start a new application.


Add a new third party application
---------------------------------

If it's to add a new package for an already enabled application, just put it in
application requirement file and configure it in its settings file. For example, a CMS
plugin should live in the CMS application.

Sometime a third party application may be shared by many applications, in this case
it will need its own composer application module. You may copy other application module
and edit it or use the application template `cookiecutter-bireli-newapp <https://github.com/sveetch/cookiecutter-bireli-newapp>`_
and just copy the composer application folder.

Quality
-------

* Pytest
* Flake
* ...
