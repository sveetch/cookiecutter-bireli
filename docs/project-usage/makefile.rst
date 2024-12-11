.. _intro_makefile:

========
Makefile
========

A project includes a Makefile which gather all common tasks you may need
to develop and maintain it.

Use its help to know about every available task: ::

    make help

.. Warning::
    Makefile is only available on Posix system like Linux or MacOS. Users with a
    Windows system will either have to install a compatibility layer or launch
    every commands itself, reading the Makefile can help.

Tasks
*****

Here is the help texts for all available Makefile tasks.

.. Note::
    Despite it is listed here, the Makefile task ``initial-data`` is currently disabled
    because of incompatibility with DjangoCMS 4. We hope to enable it again soon.

.. include:: ../_static/makefile_help.rst
