
Installation
------------

install
    To install backend and frontend
install-backend
    To install backend requirements with Virtualenv and Pip
install-frontend
    To install frontend requirements with Npm
requirements
    To build base requirements file for enabled applications from composition manifest
update
    To update backend and frontend after requirement changes
update-backend
    To update backend after requirement changes
update-frontend
    To update frontend after requirement changes

Cleaning
--------

clean
    To clean EVERYTHING (WARNING)
clean-backend-install
    To clean backend installation
clean-frontend-build
    To clean frontend built files
clean-frontend-install
    To clean frontend installation
clean-pycache
    To recursively remove all Python cache
clean-var
    To clean data (uploaded medias, database, etc..)

Django
------

migrate
    To apply demo database migrations
migrations
    To create all pending application migrations files
mo
    To build MO files from existing project PO files
new-app
    To create a new project application
po
    To update every PO files from composition apps, django apps and project code and templates for enabled languages
run
    To run Django development server
superuser
    To create a superuser for Django admin

Frontend
--------

css
    To build CSS with default environnement
css-prod
    To build CSS with production environnement
js
    To build distributed Javascript with default environnement
js-prod
    To build distributed Javascript with production environnement
frontend
    To build frontend assets from sources (CSS and JS) with default environnement
frontend-prod
    To build frontend assets from sources (CSS and JS) with production environnement
watch-css
    To launch watcher CSS with default environnement
watch-js
    To launch watcher for Javascript sources with default environnement

Diskette
--------

disk-dump
    To create a Diskette archive with data and storages
disk-init
    To build Diskette definitions for enabled applications from composition manifest
disk-load
    To load a Diskette archive, your current database and storages will be overwritten

Project checks
--------------

check-apps
    To discover elligible Django application modules from directory: $(DJANGOAPPS_DIR)
check-black
    To launch Black checking
check-comb
    To check for requirement packages lateness
check-composer
    To run Composer checking
check-disk
    To check Diskette configuration for dump operation
check-django
    To run Django System check framework
check-migrations
    To check for pending application migrations (do not write anything)
check-templates
    To check djLint reformatting before to fix it
check
    To run all check tasks

Linters
-------

black-write
    To apply Black reformating
fix-templates
    To automatically reformat templates with djLint
fix-scss
    To automatically reformat Sass sources with Stylelint
fix-frontend
    To launch all frontend reformatting tasks
flake
    To launch Flake8 checking
lint-frontend
    To run all linters on frontend sources
lint-scss
    To run Stylelint on Sass sources
lint-templates
    To run djLint on templates sources

Quality
-------

freeze-dependencies
    To write a frozen.txt file with installed dependencies versions
test
    To launch base test suite using Pytest
test-initial
    To launch tests with pytest and re-initialized database (for after new application or model changes)
quality
    To run tests, migration check and Flake linter
