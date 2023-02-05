.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Project composer: https://project-composer.readthedocs.io/en/latest/

.. _intro_project_architecture:

============
Architecture
============

Composition
***********

Bireli strongly stands on `Project composer`_ to structure its main parts (settings,
urls and requirements). You will need to properly understand `Project composer`_ before
to properly work on a project.

The *Workflow* document from `Project composer`_  documentation contains a diagram
exemple of resumed workflow for a Django project.

Details
-------

The **composer configuration lives in the** ``pyproject.toml`` file in sections named
``tool.project_composer[.**]``. Commonly you will only have to care about the option
``collection`` where is enabled all compose applications.

.. Note::

    Sections ``tool.project_composer[.**]`` assemble many options which assemble the
    composer configuration and that is called the *Manifest*.

The **collection is a list of module directory names from** ``composition_repository/``.

**You rarely have to edit the environment settings from** ``project/settings`` because
their purpose is only to override base settings for very specific environment needs.

All the **Django builtins settings are located in the compose application**
``django_builtins``. And in the same idea, **each project application settings will be
in their compose application**.

Structure
*********

Here below we will explain the default project structure, there is many more files and
directories but for a better explanation we will only focus on important parts.

::

    .
    ├── composition_repository
    │   ├── django_builtins
    │   └── sample_app
    ├── django-apps
    │   ├── project_utils
    │   └── sample_app
    ├── frontend
    │   ├── js
    │   ├── package.json
    │   ├── scss
    │   └── webpack.config.js
    ├── Makefile
    ├── project
    │   ├── settings
    │   ├── static-sources
    │   ├── templates
    │   └── urls.py
    ├── pyproject.toml
    ├── requirements
    └── tests

composition_repository/
    This is the directory which holds the applications configurations that will compose
    the project. These applications are enabled or not from the ``collection`` list
    from ``pyproject.toml``.

django-apps/
    This is the directory which hold the applications code (models, view urls, views,
    etc..).

frontend/
    Everything related to frontend assets is defined and built from there.

    * Javascript sources are in ``js/``;
    * Sass sources are in ``scss/``;
    * Frontend requirements are defined in ``package.json``;
    * Asset management is configured in ``webpack.config.js``;

project/
    This holds the Django project configuration, built assets.

    * ``settings/`` store all the environment settings;
    * ``static-sources`` will contains all built static to serve. It is not to mistake
      with ``static`` that is virtual directory which is only used in production so
      don't put anything there.
    * ``templates/`` store all the project and applications templates because we do not
      want to scatter templates amongst applications;
    * ``urls.py`` mount all the applications urls modules;

requirements/
    This holds all the requirements files for backend for various environment.

    * ``composer.txt`` is for the composer requirement itself which is appart from the
      backend base requirements;
    * ``base_template.txt`` is a template for the composer to generate again the base
      requirements file;
    * ``base.txt`` is the base requirements file. Don't write anything in it since it
      generated from composer, all you changes will be lost definitively;
    * All other requirements files are used to add some requirements for various
      environment parts;

tests/
    This is where to write all backend tests including project tests and all
    applications tests. No test in the applications directories is allowed because we
    want to store them in the same place.

pyproject.toml
    The project backend manifest contains the Project composer manifest, versionning
    and many development tool configurations.
