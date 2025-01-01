.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Project composer: https://project-composer.readthedocs.io/en/latest/
.. _django-configurations: https://django-configurations.readthedocs.io/en/stable/

.. _intro_project_backend:

=======
Backend
=======

.. _project_backend_dependencies:

Backend base dependencies
*************************

.. bireli-backend-stack::


.. _project_backend_database:

Database
********

A project is meant to work with different database drivers, at least PostgreSQL and
SQlite. SQlite is used for development and test environments. PostgreSQL is used in
all other deployment, especially production.


.. _project_backend_apps:

Included applications
*********************

There is currently around 25 applications available in composition repository and
around 4 in internal project applications. Not all of these application are
enabled, it mainly depends on collection from :ref:`project_architecture_composition`.

Here below is a resume about the main applications.

CKEditor
    The rich text editor used in applications like CMS, Lotus and others.

Crispy forms
    To help webdesign integration for forms, Django crispy forms is enabled and used
    from various other applications.

DjangoCMS
    The Content Management System used to create pages. There is also many CMS plugins
    enabled to add many content kinds in pages.

Django Blog Lotus
    The Weblog solution to manage articles.

Diskette
    A manager for data and media dumps.

Project utilities
    This is an internal application that includes the magic of a Bireli project.

    You can find many utilities to help writing tests, some internal scripts and
    management commands.

Request form
    A basic request form as an internal application that you can adapt to your needs.
    It use 'django-recaptcha' to include a Captcha field and include a RGPD check.

Security
    Additionally to the proper Django settings configuration, a project enables also
    'Django two factor' and 'Django Axes' applications to improve security.

Sitemaps
    This is an internal application that exposes all CMS pages and Lotus articles in
    a ``sitemap.xml``. You can add more content kind from other application if you
    need it.

Styleguide
    A basic application that build a synthetic styleguide directly computed from the
    Sass sources. It is configured for the shipped layout with Bootstrap so you would
    need to adapt its manifest if you want it to work with another frontend toolkit.

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


.. _project_backend_thirdparty_app:

Add a new third party application
*********************************

To add a new package for an already enabled application just put it in
application requirement file and configure it in its settings file. For example, a CMS
plugin should live in the CMS application settings.

Sometime a third party application may be shared by many applications, in this case
it will needs its own composer application module.

You may copy an other application module and edit it or use the command from
:ref:`project_backend_newapp` and just keep the composer application folder.
