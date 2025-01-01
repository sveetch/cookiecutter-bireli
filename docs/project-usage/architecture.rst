.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Project composer: https://project-composer.readthedocs.io/en/latest/

.. _intro_project_architecture:

============
Architecture
============


.. _project_architecture_composition:

Composition
***********

Basically a Bireli project is not *monolithic*, meaning it don't store settings, URLs
and requirements in single files. Instead it stands on `Project composer`_ to structure
its main parts (settings, URLs and requirements) gathered from a *collection*.

.. Hint::
    You will need to understand the concept of `Project composer`_ before to be really
    effective for developing on a project.

    The `Project composer workflow documentation <https://project-composer.readthedocs.io/en/latest/workflow.html>`_
    contains a diagram example of resumed workflow for a Django project.

.. _project_architecture_composition_overview:

Overview
--------

The composer configuration lives in the ``pyproject.toml`` file in the sections named
like ``tool.project_composer[.**]``.

Commonly you will only have to care about the option ``collection`` where is enabled
all compose applications.

.. Note::

    The sections named ``tool.project_composer[.**]`` combine many options that shape
    the composer configuration into a *Manifest*.

The collection is a list of module directory names from ``composition_repository/``.

**You rarely have to edit the environment settings from** ``project/settings`` because
their purpose is only to override base settings for very specific environment needs.

All the **Django builtins settings are located in the compose application**
``django_builtins``. And in the same idea, **each project application settings will be
in their compose application**.

.. _project_architecture_structure:

Structure
*********

Here below we will explain the default project structure, there are many more files
and directories but for a better explanation we will only focus on important parts: ::

    .
    ├── composition_repository/
    │   ├── django_builtins/
    │   └── sample_app/
    ├── django-apps/
    │   ├── project_utils/
    │   └── sample_app/
    ├── frontend/
    │   ├── js/
    │   ├── scss/
    │   ├── package.json
    │   └── webpack.config.js
    ├── Makefile
    ├── project/
    │   ├── settings/
    │   ├── static-sources/
    │   ├── templates/
    │   └── urls.py
    ├── pyproject.toml
    ├── requirements/
    └── tests/

composition_repository/
    This is the directory which holds the applications configurations that will compose
    the project. These applications are enabled in the ``collection`` list from
    ``pyproject.toml``.

django-apps/
    This is the directory which holds the applications code (models, urls, views,
    etc..).

frontend/
    Everything related to frontend assets is defined and built from there.

    * Javascript sources are in ``js/``;
    * Sass sources are in ``scss/``;
    * Frontend requirements are defined in ``package.json``;
    * Asset management is configured in ``webpack.config.js``;

project/
    This holds the Django project configuration and built assets.

    * ``settings/`` store all the environment settings;
    * ``static-sources/`` will contains all built static to serve. It is not to mistake
      with ``static/`` that is virtual directory that is only used in production so
      don't put anything there.
    * ``templates/`` store all the project and applications templates;
    * ``urls.py`` mount all the applications urls modules;

requirements/
    This holds all :ref:`intro_backend_requirements`.

tests/
    This is where to write all backend tests including project tests and all
    applications tests. No test in the applications directories is allowed because we
    want to store them in the same place.

pyproject.toml
    The project backend manifest contains the Project composer manifest, versionning
    and many development tool configurations.
