.. _virtualenv: https://virtualenv.pypa.io
.. _pip: https://pip.pypa.io
.. _Pytest: http://pytest.org
.. _Napoleon: https://sphinxcontrib-napoleon.readthedocs.org
.. _Flake8: http://flake8.readthedocs.org
.. _Sphinx: http://www.sphinx-doc.org
.. _tox: http://tox.readthedocs.io
.. _livereload: https://livereload.readthedocs.io
.. _twine: https://twine.readthedocs.io

.. _intro_development:

===========
Development
===========

.. _install_development:

Install for development
***********************

First ensure you have `pip`_, `virtualenv`_ packages installed and *GNU make*
available on your system. Then type: ::

    git clone https://github.com/sveetch/cookiecutter-bireli.git
    cd cookiecutter-bireli
    make install

Once installed you can create shortcut with a bash alias in your ``.bash_aliases``: ::

    alias cookdjango='/home/your/install/cookiecutter-bireli/.venv/bin/cookiecutter /home/your/install/cookiecutter-bireli'

So you will just have to execute following command to create a new project: ::

    cookdjango


Contribution
------------

Every feature proposal and bug fixes must pass through a Pull request.

.. note::

    To avoid managing main components versions through multiple files and miss some
    inconsistencies, main component versions are stored through private variables in
    cookiecutter template configuration file ``cookiecutter.json``.

    These variables are strings that must be valid requirement versions for Python
    package, except for the frontend components that must be valid versions for NPM.
