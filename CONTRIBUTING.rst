Bireli contributing guide
=========================

Thank you for investing your time in contributing to our project! Any
contribution you make will be reflected on
`docs.github.com <https://docs.github.com/en>`_.

Read our **Code of Conduct** to keep our community approachable
and respectable.

In this guide you will get an overview of the contribution workflow from opening an
issue, creating a PR, reviewing, and merging the PR.

Use the table of contents icon on the top left corner of this document to get to a
specific section of this guide quickly.


New contributor guide
*********************

To get an overview of the project, read the **README**. Here are some
resources to help you get started with open source contributions on Github:

*  `Finding ways to contribute to open source on
   GitHub <https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github>`_
*  `Set up
   Git <https://docs.github.com/en/get-started/quickstart/set-up-git>`_
*  `GitHub
   flow <https://docs.github.com/en/get-started/quickstart/github-flow>`_
*  `Collaborating with pull
   requests <https://docs.github.com/en/github/collaborating-with-pull-requests>`_


Getting started
***************

To know how to start developing on this project, see
`Bireli full documentation <https://cookiecutter-bireli.readthedocs.io/>`_ and
especially the *Development* part.

Issues
------

Create a new issue
..................

If you spot a problem, `search if an issue already
exists <https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-issues-and-pull-requests#search-by-the-title-body-or-comments>`_.

If a related issue doesn’t exist, you can open a new issue using a relevant `issue
form <https://github.com/sveetch/cookiecutter-bireli/issues/new/choose>`_.

We will grant ouself the right to close issues that do not fit code of conduct or
without any recent activity.

Solve an issue
..............

Scan through our `existing
issues <https://github.com/sveetch/cookiecutter-bireli/issues>`_ to
find one that interests you. You can narrow down the search using
``labels`` as filters. As a general rule, we don’t assign issues to
anyone. If you find an issue to work on, you are welcome to open a PR
with a fix.

Asking for changes
------------------

We think a template projet can not implement every features or use cases
to ensure cohesion accessibility, so it is something with strong
opinions that may not fit to your needs.

We will try to answer properly to all your feature proposals if they
follow our code of conduct, our issues templates and if you take time to
correctly expose your ideas, proposals and code contribution.

It is likely we refuse features that have a very tiny limited use cases,
that we can’t maintain (like because it needs too much ressources) or
attach Bireli to a proprietary service or technology.

Finally, time ressources to work on this project is limited so don’t
expect quick resolution, even more if you don’t take time to help us to
help you.

Make Changes
------------

Proposed changes have to be done in a dedicated branch, based on last
“master” branch version. Then your branch have to be proposed through a
Pull Request on Github.

Your work have to fill all quality requirements.

Commit messages are important, we do not want too much noise in Git
history, so:

-  Respect our commit message format;
-  Try to limit commit message to a single line and not too long (120
   should be enough);
-  Message is only to resume what have be done;
-  Commonly a small to medium feature should stand in single commit. So
   when you are done, you should squash your commit to a single one. If
   you don’t, it is possible we will squash them ourself and you may
   lose credits on this work;

Commit message format is exactly:

::

   [ACTION] Message

Where possible ``ACTION`` is:

-  ``NEW``: A new feature or release have been introduced;
-  ``FIX``: Fixed an issue;
-  ``CHG``: Commonly, every change that are not a new feature or a fix;

Cookiecuter.json
----------------

To avoid managing main components versions through multiple files and miss some
inconsistencies, main component versions are stored through private variables in
cookiecutter template configuration file ``cookiecutter.json``.

These variables are strings that must be valid requirement versions for Python
package, except for the frontend components that must be valid versions for NPM.
