requirements
    To build base requirements file for enabled applications from composition manifest
install-backend
    To install backend requirements with Virtualenv and Pip
install-frontend
    To install frontend requirements with Npm
install
    To install backend and frontend
update-backend
    To update backend after requirement changes
update-frontend
    To update frontend after requirement changes
update
    To update backend and frontend after requirement changes
freeze-dependencies
    To write a frozen.txt file with installed dependencies versions
clean
    To clean EVERYTHING (WARNING: you cannot recovery from this)
clean-var
    To clean data (uploaded medias, database, etc..)
clean-backend-install
    To clean backend installation
clean-frontend-install
    To clean frontend installation
clean-frontend-build
    To clean frontend built files
clean-pycache
    To recursively remove all Python cache
check
    To run all check tasks
check-apps
    To discover elligible Django application modules from directory: $(DJANGOAPPS_DIR)
check-composer
    To run Composer checking
check-django
    To run Django System check framework
check-migrations
    To check for pending application migrations (do not write anything)
check-disk
    To check Diskette configuration for dump operation
run
    To run Django development server
migrations
    To create all pending application migrations files
migrate
    To apply demo database migrations
superuser
    To create a superuser for Django admin
initial-data
    To load initial data
new-app
    To create a new project application
css
    To build CSS with default environnement
watch-css
    To launch watcher CSS with default environnement
css-prod
    To build CSS with production environnement
js
    To build distributed Javascript with default environnement
watch-js
    To launch watcher for Javascript sources with default environnement
js-prod
    To build distributed Javascript with production environnement
frontend
    To build frontend assets from sources (CSS and JS) with default environnement
frontend-prod
    To build frontend assets from sources (CSS and JS) with production environnement
po
    To update every PO files from composition apps, django apps and project code and templates for enabled languages
mo
    To build MO files from existing project PO files
disk-init
    To build Diskette definitions for enabled applications from composition manifest
disk-dump
    To create a Diskette archive with data and storages
disk-load
    To load a Diskette archive, your current database and storages will be overwritten
flake
    To launch Flake8 checking
black-check
    To launch Black checking
black-write
    To apply Black reformating
lint-templates
    To run djLint on templates sources
lint-scss
    To run Stylelint on Sass sources
lint-frontend
    To run all linters on frontend sources
test
    To launch base test suite using Pytest
test-initial
    To launch tests with pytest and re-initialized database (for after new application or model changes)
check-templates
    To check djLint reformatting before to fix it
fix-templates
    To automatically reformat templates with djLint
fix-scss
    To automatically reformat Sass sources with Stylelint
fix-frontend
    To launch all frontend reformatting tasks
quality
    To launch Flake8 checking and every tests suites
