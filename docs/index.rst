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


.. include:: ../README.rst


Dependencies
************

The main dependencies are:

.. bireli-full-stack::

.. Note::
    ``bireli`` is not involved anymore in a project once it has been created.

Summary
*******

If you are a **developer which wants to create new projects** with Bireli see
the part **Create a project with Bireli**.

If you are a **developer which wants to use a project** made with Bireli see
the part **Use a Bireli project** because Bireli itself is not involved anymore in
project life.

.. toctree::
   :caption: Create a project with Bireli
   :maxdepth: 2

   project-creation/get-bireli.rst
   project-creation/bireli-options.rst

.. toctree::
   :caption: Use a Bireli project
   :maxdepth: 3

   project-usage/install.rst
   project-usage/architecture.rst
   project-usage/makefile.rst
   project-usage/settings.rst
   project-usage/backend.rst
   project-usage/backend_requirements.rst
   project-usage/i18n.rst
   project-usage/frontend.rst

.. toctree::
   :caption: Bireli development
   :maxdepth: 2

   history.rst
   contribute.rst
   code_of_conduct.rst
   security.rst
