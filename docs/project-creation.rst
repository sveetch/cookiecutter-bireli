.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/stable/

.. _intro_project_creation:

====================
Create a new project
====================

.. Warning::

    You don't need this just to use a Bireli project, this is only for developers that
    need to create some fresh new projects.

To create a new project you just need to install `Cookiecutter`_ version >=2.1.0.

You may then use it with this template repository URL: ::

    cookiecutter https://github.com/sveetch/cookiecutter-bireli.git

.. Note::

    To speed up project creation you may install this cookie on your system, read
    :ref:`install_development` to know how.


Options
-------

Once invoked, cookiecutter will prompt your for some informations about your project.

You may pre define some options in your
`cookiecutter user configuration <https://cookiecutter.readthedocs.io/en/stable/advanced/user_config.html>`_
to avoid to input them each time you use this cookie.


Result
------

Once project is created, you can go into its directory and install it locally with
``make install``.

Cookiecutter will create a new directory named after your project name where you enter
in to install it and start to use.
