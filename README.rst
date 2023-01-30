.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Python: https://www.python.org
.. _virtualenv: https://virtualenv.pypa.io
.. _pip: https://pip.pypa.io
.. _Pytest: http://pytest.org
.. _Napoleon: https://sphinxcontrib-napoleon.readthedocs.org
.. _Flake8: http://flake8.readthedocs.org
.. _Sphinx: http://www.sphinx-doc.org
.. _tox: http://tox.readthedocs.io
.. _livereload: https://livereload.readthedocs.io
.. _Read the Docs: https://readthedocs.org/
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
.. _django-configurations: https://github.com/jazzband/django-configurations

===================
cookiecutter-bireli
===================

Yet another `Cookiecutter`_ template to produce a repository to start a Django site
project.

It emphases on simple package with quality and modern stack.


Package content
***************

A Django package with everything to start:

* Development in a Python virtual environment with `virtualenv`_ and `pip`_;
* Promote Test Driven Development with `Pytest`_;
* Latest Django versions support;
* Modern frontend with Bootstrap5 and Node.js;
* Settings are managed with `django-configurations`_;
* Adopted ``pyproject.toml`` to store backend tools configurations;
* A Makefile with every useful commands.


Usage
*****

Just invoke the `Cookiecutter`_ template to create a new project: ::

    cookiecutter https://github.com/sveetch/cookiecutter-bireli.git


Package requirements
--------------------

To use it from repository url you just need `Cookiecutter`_ version >=2.1.0.

.. note::

    Cookiecutter 2.x is a major version with a lot of changes so you may not be able to
    use this cookie template with Cookiecutter 1.x.


Once project is created, you can install it locally with ``make install``.

However you can install this cookie locally (to avoid doing request each time
you use it), you will need virtualenv, clone it where you want and use its
``make install`` command. Once installed you can create shortcut with a bash
alias in your ``.bash_aliases``: ::

    alias cookdjango='/home/your/install/cookiecutter-bireli/.venv/bin/cookiecutter /home/your/install/cookiecutter-bireli'

Options
-------

You can define version start, project name and project short description.

You may pre define some options in your
`cookiecutter user configuration <https://cookiecutter.readthedocs.io/en/stable/advanced/user_config.html>`_
to avoid to input them each time you use this cookie. This is especially
recommended for the author and username ones.

.. note::

    To avoid managing main components versions through multiple files and miss some
    inconsistencies, these versions are stored through private variables in cookiecutter
    template configuration file. These variables are strings that must be valid
    requirement versions for Python package, except for the frontend components that
    must be valid versions for NPM.

    However this is only used when generating a new project so you only have to bother
    about this if your are contributing to this template repository.
