.. _intro_history:

=======
History
=======

Version 0.3.3 - Unreleased
--------------------------

* Changed ``check-migrations`` task so it does not scan anymore for packaged app
  migrations, only the project ones from ``django-apps``. This is to overcome issues
  CMS plugin apps that don't have yet a proper Django>=4.0 support, see
  `issue #21 <https://github.com/sveetch/cookiecutter-bireli/issues/21>`_ for details;
* Test environment settings no longer inherit from Development, instead some of
  Development settings have been copied to the Test settings;
* Fixed Composer check command which wrongly used resolver in lazy mode (leading to
  wrong order in output);
* Added feature for the optional local environment settings file ``localsettings.py``;


Version 0.3.2 - 2023/01/30
--------------------------

* Started this history changelog;
* Started documentation;
* Added missing project directory `` locale`` and filled it with ``en`` and ``fr``
  locale directories;
* Added missing locale directories ``en`` and ``fr`` with their PO;
* Fixed settings to remove translation for language names, they must always stand in
  their own language;
