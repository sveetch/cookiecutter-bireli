.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/stable/
.. _virtualenv: https://virtualenv.pypa.io
.. _pip: https://pip.pypa.io

.. _intro_get_bireli:

==========
Get Bireli
==========

.. Hint::

    You don't need this to use a Bireli project, it is only for developers that
    need to create some fresh new projects.

.. _get_bireli_without_install:

Without install
***************

To use Bireli to create a new project you just need to install `Cookiecutter`_
version 2.1.0 or latter.

You may then use it from its repository URL: ::

    cookiecutter https://github.com/sveetch/cookiecutter-bireli.git

.. _get_bireli_with_install:

Install for development
***********************

To speed up project creation you may install this cookie on your system.

First ensure you have `pip`_ and `virtualenv`_ packages installed and *GNU make*
available on your system. Then type: ::

    git clone https://github.com/sveetch/cookiecutter-bireli.git
    cd cookiecutter-bireli
    make install

.. Warning::

    You will need to update your Bireli install yourself opposed to the direct
    repository usage (:ref:`get_bireli_without_install`) which always try to use the
    latest version from master branch.

Makefile task
-------------

Or you can use the Makefile task: ::

    make project

It will create all new project in ``dist/`` directory.

Bash alias
----------

Once installed you can also create shortcut with a bash alias in your
``.bash_aliases``: ::

    alias cookbireli='/home/your/install/cookiecutter-bireli/.venv/bin/cookiecutter /home/your/install/cookiecutter-bireli'

So you will just have to execute following command to create a new project: ::

    cookbireli
