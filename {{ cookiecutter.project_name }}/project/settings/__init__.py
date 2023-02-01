"""
=====================
Environments settings
=====================

TODO: Move this to the cookie docs and adjust it since some things have changed.

We use ``django-configurations`` to structure settings with a class per component and
environment.

Explanation
***********

There are four kind of classes involved:

* Django component classes for Django builtin components like a Template class,
  Database class, etc..
* Application classes for non Django builtin applications, like from external
  packages or internal project applications;
* A base composer class which assemble all classes for components required by project;
* Environment classes, these are the ones you will directly use when you use Django.

Commonly when you create a project you will just alter the base composer with required
component classes and possibly the environment ones if needed.

Class definition
----------------

* If a setting is just a simple variable like a string, integer, bool, etc.. you just
  need to define as a class attribute;
* If a setting require to be a computation on another setting or variable, you may
  define it as a property (with the proper decorator). But be aware it won't be simply
  usable from a setup method;
* Any other complex setting should be defined in a setup method.

Setup methods are ``pre_setup``, ``setup`` and ``post_setup``. As their name indicate
it ``pre_setup`` is called first, then ``setup`` and finally ``post_setup``. Obviously
these methods are executed after the class attributes. Also, never forget to call the
super setup method in your class setup method.

For a clean execution structure, Django component classes and Application classes only
use the ``setup`` and only the environment classes use the ``post_setup``.

"""
from .development import Development  # noqa: F401
from .test import Test  # noqa: F401
from .production import Production  # noqa: F401

# Try to get optional local environment settings file
try:
    from .localsettings import LocalEnv  # noqa: F401
except ImportError:
    pass
