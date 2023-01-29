.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/stable/

.. _intro_project_creation:

================
Project creation
================

.. Warning::

    You don't need this just to use a project, this is only for developers that need
    to create some fresh new projects.

To create a new project you just need to install `Cookiecutter`_ version >=2.1.0.

You may then use it with this template repository URL: ::

    cookiecutter https://github.com/sveetch/cookiecutter-bireli.git

.. Note::

    To speed up project creation you may install this cookie on your system, read
    :ref:`install_development` to know how.

    However you will need to keep your install up to date yourself opposed to the
    direct repository usage which will always try to use the latest version.


Options
-------

Once invoked, cookiecutter will prompt your for some informations about your project.

You may pre define some options in your
`cookiecutter user configuration <https://cookiecutter.readthedocs.io/en/stable/advanced/user_config.html>`_
to avoid to input them each time you use this cookie.


Result
------

Once project is created, you can install it locally with ``make install``.
