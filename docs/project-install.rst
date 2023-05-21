.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org

.. _intro_project_install:

===============
Project install
===============

.. Note::
   This document is about default procedure for a freshly created project. Some
   projects may have been changed by developers to involve less or more requirements,
   tasks and configurations.

   Commonly a project should documentate everything for their specific needs but it is
   out of scope of Bireli documentation.

System requirements
*******************

A project will requires `Python`, `pip`_, `virtualenv`_, *GNU make* and a recent
*Node.js* already installed and some system packages for installing and running.

Lists below are the required basic development system packages and some other optional
ones.


Basic requirements
------------------

.. Warning::
   Package names may differ depending your system.

* Git;
* Python :bireli-stack-item:`python`;
* ``python-dev``;
* ``python-virtualenv``;
* ``gettext``;
* ``gcc``;
* ``make``;
* ``libjpeg``;
* ``libcairo2``;
* ``zlib``;
* ``libfreetype``;

.. Hint::
   If your system does not have the right Python version as the default one, you should
   use something like `pyenv <https://github.com/pyenv/pyenv>`_ to install it and
   then use ``pyenv local`` to set the correct project Python version to use.

On Linux distribution
    You will install them from your common package manager like ``apt`` for Debian
    based distributions: ::

        apt install python-dev python-virtualenv gettext gcc make libjpeg libcairo2 zlib libfreetype

On macOS
    Recommended way is to use ``brew`` utility for system packages, some names
    can vary.

On Windows
    **Not supported**, you probably can install some needed stuff but with some
    works on your own.


Optional requirements
---------------------

These ones are common extra requirements that some projects may use. You don't need
to take care of them for now.

For Postgresql client driver (psycopg2)
    * ``libpq``;

For Mysql client driver
    * ``libmysqlclient-dev``;

For M2Crypto
    * ``swig``;

For Graphviz
    * ``graphviz``;
    * ``libgraphviz-dev``;
    * ``graphviz-dev``;


Local deployment
****************

A created project can be installed using a simple Makefile task: ::

    make install

Now you need to build the frontend assets: ::

    make frontend

When finished your project is ready to run.


Initial data
************

A new installed project is empty from any content, however a task exists to create some
initial data for main components: ::

    make initial-data

This will creates a user with username ``admin`` and password ``ok``.

If you don't want any initial data, you will need at least a super user to reach
the admin: ::

    make superuser


Upgrades
********

Later if a project introduces a new package or newer packages versions, you may use
the following commands to upgrade your local install.

To upgrade backend install: ::

    make install-backend

To upgrade frontend install: ::

    make install-frontend

.. Warning::
   Don't use the task ``install`` to upgrade your install, it has been made for a fresh
   new install and include some other tasks that are longer to run and that could also
   lost some of your changes.


Cleaning
********

If you need to reset your local install you may use the following command: ::

    make clean

However this will remove everything even your local data. If you just need to clean
some parts of your install, see Makefile help for all the specific cleaning tasks.


Production deployment
*********************

This is out of scope of Bireli because there is just too many ways to deploy a project,
you will have to add this layer on yourself into your project.

