.. _intro_history:

=======
History
=======

Version 0.3.7 - Unreleased
--------------------------

* Added two new options to ``cookiecutter.json`` to ask for default language and if
  project will use other languages so the project can start as a single language only
  site or not. Started possible default language to a minimal list. Default language
  will also determine project timezone;
* Improved context processor ``project_utils.context_processors.get_site_metas`` to
  store project informations (like release version) in ``PROJECT``;


Version 0.3.6 - 2023/05/22
--------------------------

* Upgraded ``cmsplugin-blocks`` to ``==1.1.0`` (fix critical bug that lost media
  during page publication);
* Added 404 and 500 templates;
* Fixed test settings to use ``setup()`` method instead of property to override
  ``MEDIA_ROOT``;
* Cleaned ``site_manifest.html`` template;
* Fixed ``freeze`` Makefile task to export to ``requirements/frozen.txt`` instead
  of ``requirements/requirements_freeze.txt``;
* Added *Basic requirements* new line about ``libcairo2`` in install documentation
  since it is a new requirement involved from library chain
  *django-filer < easy-thumbnail < reportlab*;
* Versionned main stylesheet using project version encoded in base64 for URL safety, it
  will be enough to prevent cache on production. However in development it won't really
  change anything since project version does not change often;
* Restored a proper CKEditor configuration with missing plugins CodeMirror, Youtube and
  Vimeo. Actually these plugins will be duplicated for ``django-ckeditor`` and
  ``djangocms-text-ckeditor`` because cookiecutter does not support symbolic link yet
  but a post hook will be done to resolve this;


Version 0.3.5 - 2023/04/28
--------------------------

* Added new applications in composer repository:

  * Added Lotus;
  * Added Cmsplugin-blocks;
  * Added Taggit;
  * Added DAL;

* Added a CMS toolbar for a shortcut link to Lotus articles, categories, Fobi,
  Taggit tags and Snippets;
* Added tasks for Black, Stylelint and djLint;
* Fixed issues from Stylelint on Sass sources;
* Fixed issues from djLint on templates;


Version 0.3.4 - 2023/03/28
--------------------------

* **Upgraded to Python>=3.10**;
* Removed usage of deprecated *setuptools private API* from ``project/__init__.py`` to
  get the project version. Instead it uses ``tomli`` to parse the project TOML file;
* Added ``migrations`` task to create all pending migrations from project applications;
* Added a common ``pagination.html`` template;
* Continued to improve documentation;
* Fixed ``urls.py`` from composer application which loaded url in the wrong order;
* Improved context process ``site_metas`` to include the project release version and
  included the version in skeleton into meta tag ``generator``;
* Disabled fobi form template with Bootstrap5 to turn back to the simple theme since we
  cannot implement the Bootstrap5 form errors with fobi;
* Override ``startapp`` command with a new one which use
  `bireli-newapp <https://github.com/sveetch/cookiecutter-bireli-newapp>`_;
* Added more useful dev requirements files:

  * ``codestyle`` to apply and maintain codestyle quality;
  * ``toolbox`` for some debugging;

* Added Bireli logo as default project logo and favicon;
* Continued to improve documentation;


Version 0.3.3 - 2023/02/06
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
* Moved ``DOTENV`` setting to ``DjangoPaths`` and make it conditional (to avoid
  confusing exception about Django apps and models) to Dotenv file existence;
* Fixed application settings and their ``.env`` sample. Now every setting that can be
  overwritten from Dotenv will use the default prefix ``DJANGO_`` such as a setting
  ``FOO`` is expected to be named ``DJANGO_FOO`` in Dotenv file;
* Fixed every applications settings files to explictely define ``super()`` arguments
  since it use ``cls`` and not ``self`` in setup methods;


Version 0.3.2 - 2023/01/30
--------------------------

* Started this history changelog;
* Started documentation;
* Added missing project directory ``project/locale`` and filled it with ``en`` and ``fr``
  locale directories;
* Added missing locale directories ``en`` and ``fr`` with their PO;
* Fixed settings to remove translation for language names, they must always stand in
  their own language;
