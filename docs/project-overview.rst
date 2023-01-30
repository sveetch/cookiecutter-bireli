.. _virtualenv: http://www.virtualenv.org/
.. _pip: http://www.pip-installer.org
.. _Project composer: https://project-composer.readthedocs.io/en/latest/

.. _intro_project_overview:

================
Project overview
================

Composition
***********

Bireli strongly stands on `Project composer`_ to structure its main parts, this means
settings, urls and requirements. You will need to properly understand
`Project composer`_ before to be able to properly work on a project.

To resume the purpose of composition is to assemble main parts from *bricks*, each
*brick* is dedicated to a single scope like a CMS application, a library when its usage
is shared through many other bricks or a project module.

.. Note::

    You should understand the *brick* concept when looking into available application
    bricks from the project directory ``composition_repository/``.

The *Workflow* document from `Project composer`_  documentation contains a diagram
exemple of resumed workflow within a Django project.

Where
-----

The **composer configuration lives in the** ``pyproject.toml`` file in sections named
``tool.project_composer[.**]``. Commonly you will only have to care about the option
``collection`` where is enabled all compose applications.

.. Note::

    Sections ``tool.project_composer[.**]`` assemble many options which assemble the
    composer configuration and that is called the *Manifest*.

The **collection is a list of module directory names from** ``composition_repository/``.

How
---

**You rarely have to edit the environment settings from** ``project/settings`` because
their purpose is only to override base settings for very specific environment needs.

All the **Django builtins settings are located in the compose application**
``django_builtins``. And in the same idea, **each project application settings will be
in their compose application**.

What
----

Because the project is modular, **you won't have monolithic settings file, urls file or
requirements file anymore**. There is still a project/settings/base.py but it does not
contain anything except the composer code to compose settings from enabled applications.

Thanks to ``django-configurations``, each application settings file can override or
alter a previously defined settings. By *previously*, we means that applications are
loaded in order defined in ``collection`` (plus some composer options).
``django_builtins`` is always the very first loaded application.

Why
---

The purpose of the modular project is to be able to share proper applications
configurations among many projects.

Also it strongly structure your project to avoid having many applications configured
dropped anywhere without consistency.

Finally the modular concept allow to enable or disable applications more easily.


TODO

* How to change settings ?
* How to add/remove new requirement ?
* How to add/remove new project module ?
* How to add/remove new composition app ?

Backend
*******

Database
--------

A project is meant to work with different database drivers, at least PostgreSQL and
SQlite. SQlite is used for development and test environments. PostgreSQL is used in
all other deployment, especially production.


Frontend
********

Webdesign integration
---------------------

TODO

Javascript interface
--------------------

TODO

Quality
-------

TODO
