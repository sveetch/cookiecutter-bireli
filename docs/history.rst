.. _intro_history:

=======
History
=======

Version 0.3.3 - Unreleased
--------------------------

* Disabled ``check-migrations`` task from ``quality`` task until CMS plugins have been
  updated for proper Django>=4.0 support, see issue #21 for details;
* Test environment settings no longer inherit from Development, instead some of
  Development have been copied to the Test settings;


Version 0.3.2 - 2023/01/30
--------------------------

* Started this history changelog;
* Started documentation;
* Added missing project directory `` locale`` and filled it with ``en`` and ``fr``
  locale directories;
* Added missing locale directories ``en`` and ``fr`` with their PO;
* Fixed settings to remove translation for language names, they must always stand in
  their own language;
