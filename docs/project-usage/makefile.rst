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

.. _makefile_tasks:

Tasks
*****

Here is the help texts for all available Makefile tasks.

.. Note::
    Some tasks are *meta task* meaning they are gathering some other tasks like
    ``install`` gathers  everything to boot project install then install backend and
    frontend or ``clean`` gathers everything cleaning methods to fully reset (even data)
    a project.

.. include:: ../_static/makefile_help.rst
