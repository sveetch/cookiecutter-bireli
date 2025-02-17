.. _intro_backend_requirements:

======================
Requirements structure
======================

Backend requirements are divided into multiple files and each one is dedicated to a
context which is commonly related to an environment.

.. Warning::
   Don't edit these files and prefer to add your requirements through a composer
   application to keep project well structured.

composer.txt
************

It contains Composer requirement that is installed by every environment just before
the base requirements.

It is required by every context.

base_template.txt
*****************

This is a template used by composer to generate the ``base.txt`` requirements file,
do not edit it.

It is not required directly by any context.

base.txt
********

It contains the base project requirements. Don't write anything in it since it
is automatically generated and updated from ``requirements.txt`` files in applications
from composer repository, see :ref:`project_architecture_composition` for more details.

It is required by every context.

development.txt
***************

It contains requirements used to run test and other quality check.

It is required by environments that need to run tests and quality check.

production.txt
**************

It contains requirements used to serve project, specify a proper SGBD driver, etc..

It is only required by all "non-local" environments that need to serve and run
project.

codestyle.txt
*************

It contains extra requirements for tools that perform check and apply linters on code.

This does not correspond to any real environment but is linked to development.

It is not required by any context. However it is installed with local environment.

toolbox.txt
***********

It contains requirements in local environment for some common helpful debugging tools.

This does not correspond to any real environment but is linked to development.

It is not required by any context. However it is installed with local environment.

You are not allowed to edit it without discussion with developer team since they
will inherit from your changes.

.. Note::
    Project does not include configurations for these extra requirements. You will
    need to enable and configure them through a
    :ref:`project_backend_local_settings`.
