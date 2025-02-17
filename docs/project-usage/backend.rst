.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Project composer: https://project-composer.readthedocs.io/en/latest/
.. _django-configurations: https://django-configurations.readthedocs.io/en/stable/

.. _Django REST Framework: https://www.django-rest-framework.org/
.. _Lotus: https://django-blog-lotus.readthedocs.io/
.. _django-crispy-forms: https://django-crispy-forms.readthedocs.io/
.. _Diskette: https://diskette.readthedocs.io/
.. _django-import-export: https://django-import-export.readthedocs.io/
.. _django-recaptcha: https://github.com/django-recaptcha/django-recaptcha
.. _Django Haystack: https://django-haystack.readthedocs.io/
.. _sitemap.xml: https://www.sitemaps.org/protocol.html
.. _Django Two-Factor: https://django-two-factor-auth.readthedocs.io/en/stable/index.html
.. _Django CMS: https://docs.django-cms.org/en/latest/
.. _django-axes: https://django-axes.readthedocs.io/
.. _Whoosh: https://sygil-dev.github.io/whoosh-reloaded/

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
all other deployments, especially production.

Typically when a project is running locally for your development it will use SQlite
database stored in a file, the tests are runned with a SQlite database in memory (that
disappear once finished) and deployed projects will run with a PostgreSQL database.


.. _project_backend_apps:

Included applications
*********************

There is currently around 25 applications availables in composition repository and
around 4 in internal project applications. Not all of these application are
enabled, it mainly depends on collection from :ref:`project_architecture_composition`.

Here below is a resume about the main applications.

.. Note::
    We don't show every implied requirements, only the direct requirement specifiers
    from these applications. The effective installed versions can vary depending
    specifiers.

API
---

If you enabled the composed application ``api``, you will have a project API with
`Django REST Framework`_ that you can browse on ``/api/`` or ``/api/search/redoc/``
or ``/api/schema/swagger-ui/``.

Currently it only includes API endpoints from Lotus but you can gathers applications
from other applications.

.. composer-app-requirements:: api
   :title: Requirements

Blog
----

`Lotus`_ is the Weblog solution to manage articles.

.. composer-app-requirements:: lotus
   :title: Requirements

Rich Editor
-----------

CKEditor is the rich text editor used in applications like DjangoCMS, Lotus and others.

Content Management System
-------------------------

`Django CMS`_ is the Content Management System used to create pages. There is also some
CMS plugins enabled to add many content kinds in pages.

.. composer-app-requirements:: djangocms,cmsplugin_blocks,djangocms_lotus
   :title: Requirements

Form layout
-----------

To help webdesign integration for forms, `django-crispy-forms`_ is enabled and used
from various other applications. It is enabled with its Bootstrap5 plugin.

.. composer-app-requirements:: crispy
   :title: Requirements

Backup and restore
------------------

`Diskette`_ is the data and media manager that can dump data using the native
`Django fixtures <https://docs.djangoproject.com/en/stable/topics/db/fixtures/>`_
feature.

.. composer-app-requirements:: diskette
   :title: Requirements

Import Export
-------------

If you enabled the composed application ``import_export``, the package
`django-import-export`_ will be installed with basic settings to allow for CSV and
XSLX formats.

Still there is actually no application that provides
`Import Export resources <https://django-import-export.readthedocs.io/en/latest/getting_started.html#creating-a-resource>`_
but you can add some for your applications.

.. composer-app-requirements:: import_export
   :title: Requirements

Request form
------------

A basic request form as an internal application that you can adapt to your needs.
It use `django-recaptcha`_ to include a Captcha field and include a RGPD check.

.. composer-app-requirements:: request_form
   :title: Requirements

Security
--------

Additionally to the proper Django settings configuration, a project enables also
`Django Two-Factor`_ and `django-axes`_ applications to improve security.

.. composer-app-requirements:: axes,two_factor_auth
   :title: Requirements

Sitemaps
--------

This is an internal application that exposes all CMS pages and Lotus articles in
a `sitemap.xml`_. You can add more content kind from other applications if you
need it.

Search engine
-------------

If you enabled the composed application ``search``, `Django Haystack`_ will be installed
and configured with `Whoosh`_ backend.

However you will have to
`implement the indexes, form and view <https://django-haystack.readthedocs.io/en/master/tutorial.html#handling-data>`_
yourself for your applications.

Finally remember that you will need to manage (re)generation of your data indexes.

.. composer-app-requirements:: search
   :title: Requirements


Styleguide
----------

A basic application that build a synthetic styleguide directly computed from the
Sass sources. It is configured for the shipped layout with Bootstrap so you would
need to adapt its manifest if you want it to work with another frontend toolkit.

.. composer-app-requirements:: styleguide
   :title: Requirements

Utilities
---------

There is an internal application named ``project_utils`` that includes the
*magic* of a Bireli project which is mainly Python scripts to help for some
architecture tasks (Makefile, project-composer, etc..) and some modules for useful
code.

Also you can find inside many utilities to help writing tests, some internal scripts and
management commands.

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

Disabling or removing an application
************************************

Basically it should be easy as removing its line from the Composer collection in
``pyproject.toml`` but it is a little bit naive.

Commonly the lightweight applications just can be disabled and removed but they
possibly have a test to remove.

There is also other applications that are tied together, you will need to find if they
are a dependency of another application, the command ``make check-composer`` can help
you for this.

Finally there are applications that may be required from some templates which use their
template tags, you will need to dig into templates to find them all but at this point
it should be easy and you are probably done.

.. Hint::
    Project composer as a
    `purge task <https://project-composer.readthedocs.io/en/latest/cli.html#purge>`_ to
    automatically remove unused application from composer repository but it won't help
    you about further cleaning in tests, code and templates.

Remember to help you with the quality tasks to valid every removing.
