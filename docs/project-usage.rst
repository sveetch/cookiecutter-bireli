.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Project composer: https://project-composer.readthedocs.io/en/latest/

.. _intro_project_usage:

=============
Project usage
=============

Projects are made to run within a virtual environnement from `virtualenv`_.


Makefile tasks
**************

Once a project is installed, you will use the Makefile to achieve all the common tasks,
use its help to know about every available task: ::

    make help

The following list is a summary of important tasks, use them like ``make TASKNAME``.

requirements
    To build base requirements file for enabled applications from composition manifest.

    This is only to use when you change requirements files from repository application
    or when you change enabled application from composer manifest.

install
    To perform a new install with both backend and frontend.

install-backend
    To install or upgrade backend requirements with Virtualenv and Pip.

install-frontend
    To install or upgrade frontend requirements with Npm.

freeze-dependencies
    To write a frozen.txt file with installed dependencies versions

clean
    To clean EVERYTHING (WARNING: you cannot recovery from this).

    This use all the available clean tasks, see Makefile help to know about them.

check-django
    To run Django System check framework. This is the most simple way to check about
    your project health but it won't go deeper like tests can do.

check-migrations
    To check for pending application migrations. It does not write anything, just
    output all pending migration Django found from your project.

    This is useful when you are working on models since every tiny change can require
    a migration.

run
    To run Django development server on your local network interface on port ``8001``.

    By default you will be able to reach it with ``http://localhost:8001/``.

migrate
    To apply pending models migrations. This is to run when you have created new
    migrations or when you updated your local install which can bring some model
    changes.

superuser
    To quickly create a new superuser for Django admin from commandline. Obviously once
    you already have a superuser you may use the Django admin to create new users.

initial-data
    To load initial data for enabled applications. You should not run it twice on the
    same database.

css
    To build CSS for development environnement, this means without any optimization.

watch-css
    To launch watcher CSS for development environnement. On every Sass sources change a
    build will be performed to update CSS.

js
    To build distributed Javascript for development environnement.

watch-js
    To launch watcher for Javascript sources for development environnement.

frontend
    To build frontend assets from sources (CSS and JS) for development environnement.

po
    To update every PO files from composition apps, django apps and project code and
    templates for enabled languages.

    This won't create the locale directory for new enabled languages from settings, you
    must boot it yourself.

    Saying to add French language, first you need to add ``("fr", "French"),`` to
    ``settings.LANGUAGES``. Then after you will run a command like this: ::

        .venv/bin/python manage.py makemessages --keep-pot --no-obsolete --locale fr

    Never copy another language directory and rename it to your new locale name, it
    will miss some specific locale options added by gettext (like plural formula).

mo
    To build MO files from existing project PO files.

flake
    To launch Flake8 checking on project backend code.

test
    To launch project test suite using Pytest.

quality
    To launch all quality tasks, any failure will stop its execution.
