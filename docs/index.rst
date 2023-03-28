.. _Python: https://www.python.org
.. _virtualenv: https://virtualenv.pypa.io
.. _pip: https://pip.pypa.io
.. _Django: https://www.djangoproject.com/
.. _Pytest: http://pytest.org
.. _Napoleon: https://sphinxcontrib-napoleon.readthedocs.org
.. _Flake8: http://flake8.readthedocs.org
.. _Sphinx: http://www.sphinx-doc.org
.. _tox: http://tox.readthedocs.io
.. _livereload: https://livereload.readthedocs.io
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
.. _django-configurations: https://django-configurations.readthedocs.io/en/stable/
.. _Project composer: https://project-composer.readthedocs.io/en/latest/
.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/stable/

.. cookiecutter-bireli documentation master file, created by David Thenon


======
Bireli
======

Bireli is a Django project template with `Cookiecutter`_ to produce a ready to start
project.

It emphases on quality, modularity and modern stable stack.

.. Hint::

    This documentation is an ongoin work, not everything have been covered yet and it
    will continue to evolve.


Features
********

* Development in a Python virtual environment with `virtualenv`_ and `pip`_;
* Project include a ``pyproject.toml`` to store (almost) all backend tools
  configurations;
* Promote Test Driven Development with `Pytest`_;
* Latest stable stack support;
* Frontend assets built with Node.js and managed with Webpack;
* Default shipped layout with Bootstrap5;
* Backend application architecture is modular through `Project composer`_;
* Settings are managed with `django-configurations`_;
* Internationalization and localization enabled;
* Include a set of main applications (CMS, blog, form builder, etc..) pre-configured;
* A Makefile with every useful commands.


Dependencies
************

All involved dependencies

.. bireli-full-stack::

.. Note::
    ``Bireli`` and ``Bireli-newapp`` are not involved in a project once it has been
    created.

Links
*****

* Read the documentation on `Read the docs <https://cookiecutter-bireli.readthedocs.io/>`_;
* Clone it on its `Github repository <https://github.com/sveetch/cookiecutter-bireli>`_;


Summary
*******

.. toctree::
   :maxdepth: 3

   project-creation.rst
   project-install.rst
   makefile.rst
   project-architecture.rst
   project-backend.rst
   project-frontend.rst
   development.rst
   history.rst
