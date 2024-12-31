.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/stable/

.. _intro_bireli_options:

==============
Bireli options
==============

Once invoked, cookiecutter will prompt your for some informations about your project.

You may pre define some options in your
`cookiecutter user configuration <https://cookiecutter.readthedocs.io/en/stable/advanced/user_config.html>`_
to avoid to input them each time you use this cookie.

For example you could create a file ``.cookiecutterrc`` at root of your home
directory: ::

    default_context:
        versioning: bumpver
        language: fr

This would create a project using BumpVersion versionning style instead of default
"natural" and set default project language to French.

Cookiecutter is still asking for your option choices but get default choices from
the ``.cookiecutterrc`` file so you just have to fill "project_title" and maybe
"project_description" and just let the default choices for other options.

.. Note::

    It seems there is a little bug with Cookiecutter, the "rc" file and some kind of
    options, although you set a default language in rc file, the prompt is still showing
    the first choice as the default but finally it is indeed using the one from your
    rc file.


About project Internationalization and localization
***************************************************

Default behavior for a created project is to be a multiple languages site set with
default language as selected from ``language`` option.

If your project is not planned to have any other language than the default one, you
may disable it with option ``multiple_languages``, using any other value than ``true``
or ``True`` will disable any other langue and i18n urls (application urls starting with
language prefix like ``/en/``).

Project configuration can be easily switched to be a multiple language site or a single
language site further from settings, see :ref:`intro_backend_i18n`.


Result
******

Cookiecutter will create a new directory named after your project name. You can enter
into its directory and install it locally with ``make install`` (see
:ref:`intro_project_install` for details).
