.. _intro_history:

=======
History
=======

Version 0.5.1 - 2025/05/18
**************************

Release for requirements updates and some modest improvements.

Backend requirement changes
---------------------------

* Upgraded 'django' to 5.2.x;
* Upgraded 'django-cms' to 5.x.x;
* Upgraded 'django-axes' to 7.1.x;
* Upgraded 'djangorestframework' to 3.16.x and relaxed 'drf-spectacular';
* Upgraded 'django-phonenumber-field' to 8.1.x;
* Upgraded 'django-recaptcha' to 4.1.x;
* Upgraded the following requirements to their latest release for the Django 5.2
  support:

  * 'cmsplugin-blocks' to 1.7.0;
  * 'djangocms-lotus' to 0.3.0;
  * 'django-blog-lotus' to 0.9.3;
  * 'django-smart-media' to 0.5.0;
  * 'emencia-django-staticpages' to 0.6.2;


Frontend requirement changes
----------------------------

Bootstrap has been upgraded to 5.3.6 but you probably have nothing to care about because
the last releases are almost only about fixes, nothing has really changed.


Review of DjangoCMS ecosystem
-----------------------------

* Restored 'djangocms_picture' in 4.1.1 since it has been validated to work with
  DjangoCMS 4. However it is not enabled on default since the CKEditor plugin
  ``image2`` is more coherent and is the recommended solution to insert images in
  text content;
* 'djangocms-snippet' is known to be compatible with DjangoCMS and already enabled;
* 'djangocms-audio', 'djangocms-file' and 'djangocms-video' should be compatible even
  they have no new release yet with an official support;


Moved to reCaptcha V3 in Request form
-------------------------------------

We have moved usage of reCaptcha from V2 to V3 in request form because V3 is now the
recommended version and it fixes a bug that prevented to have multiple forms using
reCAPTCHA in the same page.

You may still be able to use V2 in your forms (and request form by the way) since it is
just a matter of using the right form widget (``ReCaptchaV2`` or ``ReCaptchaV3``). Note
that the widget argument ``action`` is not supported in V2.

Be aware that V3 does not support the generic development keys from Google so now you
will need to set valid keys before using any form with reCaptcha V3 (so at least the
request form).

See Bireli documentation for details about reCaptcha.


Improved CKEditor experience with images
----------------------------------------

We restored Sass stylesheet named ``ckeditor.scss`` and updated Buckle Sass library
with a new object and mixins to improve rich content editor and render:

* Image alignments are fully supported on rendered contents;
* Image alignments from CKEditor plugin ``image2`` are fully supported in CKEditor;
* Image alignments from 'djangocms-picture' plugin are not supported in CKEditor
  (editor surround plugin content with elements that does not include any alignment
  classnames);

See Bireli documentation for details about *Rich content*.

Various
-------

* Moved setting ``X_FRAME_OPTIONS`` from ``djangocms`` to ``django_builtins`` composed
  application;
* Added initial POT catalog and an PO catalog for french language;
* Added a rule in ``.gitignore`` to ignore compiled translation catalogs (the ``*.mo``
  files);
* Fixed prototype index pages which used wrong variable to list pages;


Version 0.5.0 - 2025/02/18
**************************

A new release to bring new useful applications and some fixes.

Backend requirement changes
---------------------------

* Added **djangocms-lotus** requirement to enable the CMS plugin for Lotus;
* Enabled again 'djangocms-snippet' since its version 5.0.0 is compatible again;
* Added composition application ``search`` which configures **django-haystack** with
  **Whoosh** backend ready to implement a search engine. However the indexes, form and
  view are still to be implemented;
* Added composition application ``import_export`` which configures
  **django-import-export**. However there is actually no shipped ressources for any
  applications, those ones which already package them will be available but you will
  have to make ressource modules for the other applications;
* Added composition application ``api`` which configures **Django REST Framework** with
  **drf-spectacular** (to improve the API browser). Currently there is only endpoints
  from Lotus since other applications does not have any;
* Upgraded **Diskette** to version 0.5.0;

Diskette fixes
--------------

* Update diskette configuration for DjangoCMS to fix issue with DjangoCMS4 default
  manager that drops unpublished content in dump;
* Added datetime on default Diskette dump filename for admin but forced it to
  ``diskette_data_storages.tar.gz``` in Makefile tasks so they are compatible;

Internal Bireli changes
-----------------------

* Improved *Backend* documentation;
* Added a new docutils extension to get requirements from composer repository
  applications;
* Added new builder option ``api_enabled`` to enable or not the shipped API stuff. On
  default the API is disabled;
* Improved Tox configuration to be more DRY with environment variables for options;


Version 0.4.0 - 2025/01/01
**************************

The main purpose of this new release is to upgrade to Django 5, DjangoCMS 4,
Bootstrap 5.3.3 and Dart Sass embedded.

Upgraded backend requirements
-----------------------------

* Upgraded to Python 3.11, Django 5.0, DjangoCMS 4.1.0 and all other dependencies to
  their latest compatible version;
* Removed everything related to initial loader because it is not compatible anymore
  with DjangoCMS 4. We will soon provide a new way to load initial data but for
  now a new installed project will be blank;
* Removed factories related to DjangoCMS because they can not be made compatible
  with the new core API from DjangoCMS 4;
* We now use ``djangocms-text`` with CKEditor4 (for now) instead of
  ``djangocms-text-ckeditor`` that is ongoing to be deprecated;
* Added disabled requirements and settings class to enable CKEditor 5 in CMS so it
  can easily be tested, this to prepare the future migration;
* 'Django Icomoon' because it is incompatible and seems useless now;

Fobi removal and Request form as a workaround
---------------------------------------------

* Added a new internal application ``request_form`` to implement a basic request
  form to cover the basic need of a contact form since Fobi has been removed.
  Because this application model may differ from a site to another, the application
  is not enabled on default so you could adapt the model to the site needings,
  update its initial migration before enable application in your project;
* Removed everything about Fobi that is incompatible and unmaintained;

Diskette fixes
--------------

* Diskette configuration has been fixed from beta usage feedback so it should work
  really well now even it is know for some issues with loading dump from a
  production deployment. But loading locally a downloaded dump should be a proper
  workaround for now;

Improved project security
-------------------------

* The following settings ``SESSION_COOKIE_SECURE``,
  ``SESSION_EXPIRE_AT_BROWSER_CLOSE``, ``CSRF_COOKIE_SECURE`` have been turned on
  in production settings;
* Setting ``AUTH_PASSWORD_VALIDATORS`` now uses the strongest builtin validators;
* Added ``django-two-factor-auth`` and enabled it on default;
* Added ``django-axes`` and enabled it on default;

Django Recaptcha enabled again
------------------------------

* Restored django-recaptcha (actually only used from Request form) in last version
  and using its invisible mode widget therefore there is no checkbox to check,
  only a widget mark (in fixed position) about the form securized by Recaptcha;
* Added a Sass object to fix layout recaptcha v2 in invisible mode in request form
  (and possibly elsewhere);
* Removed old useless custom django-recaptcha templates;

Upgraded frontend requirements
------------------------------

* Upgraded to Bootstrap 5.3.3 and Webpack 5.91.0;
* Moved from 'node-sass' compiler to 'sass-embedded' 1.79.0. The first is
  deprecated since 3 years and the latter implements last Sass features (and
  faster that the simple 'sass' compiler);

Update Sass sources for last Bootstrap and Sass
-----------------------------------------------

* Added Bootstrap color toggler menu;
* Silented annoying warnings from Sass compiler against Bootstrap until it fixed
  them;
* Renamed Bootbutt to Buckle and added source part indexes modules;
* Restructured main Sass source;
* Upgraded to PyCssStyleguide v1.2.0 and updated its Sass mixin library;
* Updated Styleguide manifest to fit to the new Sass mixin library and
  Bootstrap 5.3.3;

Makefile improvement
--------------------

* Added "Dependency comb" to toolbox and add its Makefile task ``check-comb``;
* Renamed Makefile task ``black-check`` to ``check-black``;
* Restructured Makefile help to organize task per section;
* Updated Makefile parser to implement sections;

Various
-------

* Added custom "Lotus" admin stylesheet to fix compatibility issues with
  "djangocms-admin-style";
* Added Styleguide link to CMS toolbar;
* Improved documentation;


Version 0.3.13 - 2024/09/28
***************************

Internal Bireli changes
    * Changed Pytest command option to adopt the right modest verbose options;
    * Added a minimal version to all requirements to help Pip to resolve packages
      quicker;

Project template changes
    * Changed Pytest configuration and command option to adopt the right modest
      verbose options;
    * Pinned sorl-thumbnail to ``>=12.9.0,<12.11.0`` since its last version is
      incompatible with Django<5.0. We will remove this once we moved to Django 5.0,
      close #55;
    * Pinned django-ckeditor to ``==6.7.1`` to remove annoying warning message from
      CKEditor, close #52;
    * Fixed docstring typo in reCAPTCHA settings class, close #51;
    * Added a minimal version to every base and environments requirements to help Pip
      to resolve packages quicker;
    * django-debug-toolbar has been capped to 4.3.0 until we move to Django>=4.2;
    * django-configurations has been capped to 2.5.0 until we move to Django>=4.2;


Version 0.3.12 - 2024/04/24
***************************

Internal Bireli changes
    None.

Project template changes
    * Introduced new setting ``PARTS_PATH`` for the path of ``parts/`` directory;
    * Changed again the webpack configuration to build file ``webpack-stats.json`` into
      ``parts/`` instead of ``var/`` since the latter is not ensured to exist in
      deployed backend;
    * Fixed duplicate definition of setting ``DEFAULT_FROM_EMAIL`` in ``DjangoBase``
      class;
    * Introduced a new setting ``SITE_INDEX_METAS`` and changed skeleton to use it to
      switch meta "robots" value. Concretely on default the page only include directives
      to not index the site and only production environment expose directives to enable
      indexation;
    * Added `Diskette <https://diskette.readthedocs.io/>`_ with configurations for all
      available applications and Makefile tasks;
    * Removed project-composer initialization notification;
    * Added missing task ``disk-init`` in meta task ``install`` to create needed
      Diskette definitions;
    * Added new Makefile tasks ``update-backend``, ``update-frontend`` and ``update``
      to ease update with new project releases;
    * Renamed context processor ``site_metas`` to ``project_globals``, since the first
      was an old name that leaded to confusion with meta elements. This involve
      renaming for the occurences in various forms (``site metas``, ``site-metas``,
      etc..) in template and backend code. And especially the setting
      ``EXTRA_SITE_METAS`` which becomes ``EXTRA_PROJECT_GLOBALS``;
    * Added new view at ``/utils/project-globals/`` to display available variables
      from ``project_globals`` context processor. This view is only available for staff
      users. It's link is available from the CMS toolbar item ``Applications``;
    * Introduced a new setting ``EXTRA_PROJECT_GLOBALS`` to add extra data in context
      processor ``project_globals`` below the item name ``EXTRA``;


Version 0.3.11 - 2024/01/09
***************************

Internal Bireli changes
    * Added some minor improvements about localization and install documentations;

Project template changes
    * Added new available CMS applications in composer repository:

      * djangocms-audio
      * djangocms-file
      * djangocms-video

    * Pinned django-ckeditor and DjangoCMS requirements to more recent stable versions;
    * Improved DjangoCMS and Lotus sitemaps with custom sitemap classes which include
      more flexible item priority. This involves some new settings;
    * Added new template ``admin/base.html`` to patch django-admin-styles stylesheet
      to resolve issue with CKEditor plugins modals that were unable to positionnate
      correctly. The modal position is not optimal yet but is a real improvement;
    * Added new stylesheet
      ``django-apps/project_utils/static/css/django-ckeditor-patch.css``  that can be
      included in custom application admin (or form) to fix CKEditor width (obviously
      only needed if CKEditor is used);
    * Changed webpack configuration so its file ``webpack-stats.json`` is now built in
      ``var/`` instead of previously ``project/static-sources`` so it can not be
      reached as a static file anymore;
    * Updated included default site favicon with the new Bireli logo;


Version 0.3.10 - 2023/12/04
***************************

Internal Bireli changes
    * Upgraded to cookiecutter>=2.3.0;
    * Improved post generation hook;
    * Added cookiecutter prompts for options;
    * Added a Tox configuration to automatically check for project creation,
      installation and quality with options variants;
    * Added new option ``init_git_repository`` to initialize created project as a GIT
      repository with an initial commit to include project files;
    * Added Python script ``docs/makefile_parser.py`` to automatize Makefile help
      texts documentation;
    * Moved changelog to ``CHANGELOG.rst`` and made an alias to it in documentation;
    * Restructured changelog to separate changes on Bireli itself from those ones on
      Project template;

Project template changes
    * Pinned django-recaptcha to ``<4.0.0`` since 4.x version has incompatible changes
      but Fobi is not ready yet;
    * Upgraded to ``lotus==0.8.1``;
    * Added new application ``project_sitemaps`` to configure and publish Sitemap XML
      for CMS pages and Lotus articles;
    * Added sample image crafter utilities for tests in ``project_utils.imaging``;
    * Refactored third part factories from ``project_utils`` and added factories for
      Tag and CMS extension;
    * Improved project README;


Version 0.3.9 - 2023/08/18
**************************

Internal Bireli changes
    * Updated ``.readthedocs.yml`` file to follow service deprecations changes;

Project template changes
    * Upgraded to ``cmsplugin-blocks==1.2.0``;


Version 0.3.8 - 2023/08/01
**************************

Internal Bireli changes
    * Improved documentation:

      * Changed Bireli logo to a new colorful one;
      * Changed documentation to a Sphinx theme
        `Furo <https://github.com/pradyunsg/furo>`_;
      * Changed documentation to a new document structure;

    * Added all documents to fullfil Github Community Standards;
    * Added quality with Flake8 and Pytest configurations;
    * Added Post generation hook with a task to create symlinks from
      ``cookiecutter._apply_symlink_to``;
    * Added basic building test coverage with Cookiecutter;

Project template changes
    * Improved how elligible Django application modules are discovered in Makefile
      tasks that need it. This should fix issue with some system that don't have a
      complete support of all ``ls`` arguments so it has been written in a full Python
      script;
    * Upgraded to ``django-filer>=3`` and remove its dependancy to ``mptt`` that are no
      longer needed;
    * Upgraded to ``lotus==0.6.0``;


Version 0.3.7 - 2023/06/06
**************************

Internal Bireli changes
    * Added two new options to ``cookiecutter.json`` to ask for default language and if
      project will use other languages so the project can start as a single language
      only site or not. Started available languages list to a minimal list. Also the
      default language will also determine project timezone;

Project template changes
    * Added missing url and template for HTTP 403 response;
    * Added new application ``crispy`` in composer repository to enable
      ``django-crispy-forms`` with Bootstrap5 theme;
    * Upgraded to ``lotus==0.5.2.1`` to include fix about pending migration;
    * Upgraded to ``fobi==0.19.8`` and removed temporary ``LoginRequiredDashboardView``
      view since original Fobi dashboard view has been fixed;
    * Improved context processor ``project_utils.context_processors.get_site_metas`` to
      store project informations (like release version) in ``PROJECT``;
    * Changed ``skeleton.html`` template for a little bit of space optimization;
    * Changed ``base.html`` template to build homepage url depending
      ``settings.ENABLE_I18N_URLS``;
    * Fixed CMS toolbar to remove duplicate "Tags management" item and add missing
      "Fobi" item;


Version 0.3.6 - 2023/05/22
**************************

Internal Bireli changes
    * Added *Basic requirements* new line about ``libcairo2`` in install documentation
      since it is a new requirement involved from library chain
      *django-filer < easy-thumbnail < reportlab*;

Project template changes
    * Upgraded ``cmsplugin-blocks`` to ``==1.1.0`` (fix critical bug that lost media
      during page publication);
    * Added 404 and 500 templates;
    * Fixed test settings to use ``setup()`` method instead of property to override
      ``MEDIA_ROOT``;
    * Cleaned ``site_manifest.html`` template;
    * Fixed ``freeze`` Makefile task to export to ``requirements/frozen.txt`` instead
      of ``requirements/requirements_freeze.txt``;
    * Versionned main stylesheet using project version encoded in base64 for URL
      safety, it will be enough to prevent cache on production. However in development
      it won't really change anything since project version does not change often;
    * Restored a proper CKEditor configuration with missing plugins CodeMirror, Youtube
      and Vimeo. Actually these plugins will be duplicated for ``django-ckeditor``
      and ``djangocms-text-ckeditor`` because cookiecutter does not support symbolic
      link yet but a post hook will be done to resolve this;


Version 0.3.5 - 2023/04/28
**************************

Internal Bireli changes
    None

Project template changes
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
**************************

Internal Bireli changes
    * Continued to improve documentation;
    * Override ``startapp`` command with a new one which use
      `bireli-newapp <https://github.com/sveetch/cookiecutter-bireli-newapp>`_;
    * Added Bireli logo as default project logo and favicon;

Project template changes
    * **Upgraded to Python>=3.10**;
    * Removed usage of deprecated *setuptools private API* from ``project/__init__.py``
      to get the project version. Instead it uses ``tomli`` to parse the project TOML
      file;
    * Added ``migrations`` task to create all pending migrations from project
      applications;
    * Added a common ``pagination.html`` template;
    * Fixed ``urls.py`` from composer application which loaded url in the wrong order;
    * Improved context process ``site_metas`` to include the project release version
      and included the version in skeleton into meta tag ``generator``;
    * Disabled fobi form template with Bootstrap5 to turn back to the simple theme
      since we cannot implement the Bootstrap5 form errors with fobi;
    * Added more useful dev requirements files:

      * ``codestyle`` to apply and maintain codestyle quality;
      * ``toolbox`` for some debugging;



Version 0.3.3 - 2023/02/06
**************************

Internal Bireli changes
    None

Project template changes
    * Changed ``check-migrations`` task so it does not scan anymore for packaged app
      migrations, only the project ones from ``django-apps``. This is to overcome issues
      CMS plugin apps that don't have yet a proper Django>=4.0 support, see
      `issue #21 <https://github.com/sveetch/cookiecutter-bireli/issues/21>`_ for
      details;
    * Test environment settings no longer inherit from Development, instead some of
      Development settings have been copied to the Test settings;
    * Fixed Composer check command which wrongly used resolver in lazy mode (leading to
      wrong order in output);
    * Added feature for the optional local environment settings file
      ``localsettings.py``;
    * Moved ``DOTENV`` setting to ``DjangoPaths`` and make it conditional (to avoid
      confusing exception about Django apps and models) to Dotenv file existence;
    * Fixed application settings and their ``.env`` sample. Now every setting that can
      be overwritten from Dotenv will use the default prefix ``DJANGO_`` such as a setting
      ``FOO`` is expected to be named ``DJANGO_FOO`` in Dotenv file;
    * Fixed every applications settings files to explictely define ``super()`` arguments
      since it use ``cls`` and not ``self`` in setup methods;


Version 0.3.2 - 2023/01/30
**************************

* Started this history changelog;
* Started documentation;
* Added missing project directory ``project/locale`` and filled it with ``en`` and ``fr``
  locale directories;
* Added missing locale directories ``en`` and ``fr`` with their PO;
* Fixed settings to remove translation for language names, they must always stand in
  their own language;
