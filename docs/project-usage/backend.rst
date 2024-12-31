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

Sometime a third party application may be shared by many applications, in this case
it will needs its own composer application module.

You may copy an other application module and edit it or use the command from
:ref:`project_backend_newapp` and just keep the composer application folder.
