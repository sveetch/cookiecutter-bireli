.. _intro_history:

=======
History
=======

Version 0.3.12 - 2024/04/24
---------------------------

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
---------------------------

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
---------------------------

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
--------------------------

Internal Bireli changes
    * Updated ``.readthedocs.yml`` file to follow service deprecations changes;

Project template changes
    * Upgraded to ``cmsplugin-blocks==1.2.0``;


Version 0.3.8 - 2023/08/01
--------------------------

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
--------------------------

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
--------------------------

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
--------------------------

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
--------------------------

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
--------------------------

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
--------------------------

* Started this history changelog;
* Started documentation;
* Added missing project directory ``project/locale`` and filled it with ``en`` and ``fr``
  locale directories;
* Added missing locale directories ``en`` and ``fr`` with their PO;
* Fixed settings to remove translation for language names, they must always stand in
  their own language;
