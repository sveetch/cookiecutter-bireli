VENV_PATH=.venv
VENV_BIN=$(VENV_PATH)/bin

PYTHON_INTERPRETER=python3
PYTHON_BIN=$(VENV_BIN)/python

PIP=$(VENV_BIN)/pip
PROJECT_COMPOSER=$(VENV_BIN)/project_composer
DJANGO_MANAGE=$(PYTHON_BIN) manage.py
FLAKE=$(VENV_BIN)/flake8
PYTEST=$(VENV_BIN)/pytest
DJLINT=$(VENV_BIN)/djlint
BLACK=$(VENV_BIN)/black

DJANGOPROJECT_DIR=project
DJANGOAPPS_DIR=django-apps
STATICFILES_DIR=$(DJANGOPROJECT_DIR)/static-sources
FRONTEND_DIR=frontend
PROJECT_APPS=$(PYTHON_BIN) $(DJANGOAPPS_DIR)/project_utils/ls-djangoapps.py $(DJANGOAPPS_DIR)/

# Formatting variables, FORMATRESET is always to be used last to close formatting
FORMATBLUE:=$(shell tput setab 4)
FORMATBOLD:=$(shell tput bold)
FORMATRESET:=$(shell tput sgr0)

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  Installation"
	@echo "  ============"
	@echo
	@echo "  install                       -- to install backend and frontend"
	@echo "  install-backend               -- to install backend requirements with Virtualenv and Pip"
	@echo "  install-frontend              -- to install frontend requirements with Npm"
	@echo "  requirements                  -- to build base requirements file for enabled applications from composition manifest"
	@echo "  update                        -- to update backend and frontend after requirement changes"
	@echo "  update-backend                -- to update backend after requirement changes"
	@echo "  update-frontend               -- to update frontend after requirement changes"
	@echo
	@echo "  Cleaning"
	@echo "  ========"
	@echo
	@echo "  clean                         -- to clean EVERYTHING (WARNING)"
	@echo "  clean-backend-install         -- to clean backend installation"
	@echo "  clean-frontend-build          -- to clean frontend built files"
	@echo "  clean-frontend-install        -- to clean frontend installation"
	@echo "  clean-pycache                 -- to recursively remove all Python cache"
	@echo "  clean-var                     -- to clean data (uploaded medias, database, etc..)"
	@echo
	@echo "  Django"
	@echo "  ======"
	@echo
	@echo "  migrate                       -- to apply demo database migrations"
	@echo "  migrations                    -- to create all pending application migrations files"
	@echo "  mo                            -- to build MO files from existing project PO files"
	@echo "  new-app                       -- to create a new project application"
	@echo "  po                            -- to update every PO files from composition apps, django apps and project code and templates for enabled languages"
	@echo "  run                           -- to run Django development server"
	@echo "  superuser                     -- to create a superuser for Django admin"
	@echo
	@echo "  Frontend"
	@echo "  ========"
	@echo
	@echo "  css                           -- to build CSS with default environnement"
	@echo "  css-prod                      -- to build CSS with production environnement"
	@echo "  js                            -- to build distributed Javascript with default environnement"
	@echo "  js-prod                       -- to build distributed Javascript with production environnement"
	@echo "  frontend                      -- to build frontend assets from sources (CSS and JS) with default environnement"
	@echo "  frontend-prod                 -- to build frontend assets from sources (CSS and JS) with production environnement"
	@echo "  watch-css                     -- to launch watcher CSS with default environnement"
	@echo "  watch-js                      -- to launch watcher for Javascript sources with default environnement"
	@echo
	@echo "  Diskette"
	@echo "  ========"
	@echo
	@echo "  disk-dump                     -- to create a Diskette archive with data and storages"
	@echo "  disk-init                     -- to build Diskette definitions for enabled applications from composition manifest"
	@echo "  disk-load                     -- to load a Diskette archive, your current database and storages will be overwritten"
	@echo
	@echo "  Project checks"
	@echo "  =============="
	@echo
	@echo "  check-apps                    -- to discover elligible Django application modules from directory: $(DJANGOAPPS_DIR)"
	@echo "  check-black                   -- to launch Black checking"
	@echo "  check-comb                    -- to check for requirement packages lateness"
	@echo "  check-composer                -- to run Composer checking"
	@echo "  check-disk                    -- to check Diskette configuration for dump operation"
	@echo "  check-django                  -- to run Django System check framework"
	@echo "  check-migrations              -- to check for pending application migrations (do not write anything)"
	@echo "  check-templates               -- to check djLint reformatting before to fix it"
	@echo "  check                         -- to run all check tasks"
	@echo
	@echo "  Linters"
	@echo "  ======="
	@echo
	@echo "  black-write                   -- to apply Black reformating"
	@echo "  fix-templates                 -- to automatically reformat templates with djLint"
	@echo "  fix-scss                      -- to automatically reformat Sass sources with Stylelint"
	@echo "  fix-frontend                  -- to launch all frontend reformatting tasks"
	@echo "  flake                         -- to launch Flake8 checking"
	@echo "  lint-frontend                 -- to run all linters on frontend sources"
	@echo "  lint-scss                     -- to run Stylelint on Sass sources"
	@echo "  lint-templates                -- to run djLint on templates sources"
	@echo
	@echo "  Quality"
	@echo "  ======="
	@echo
	@echo "  freeze-dependencies           -- to write a frozen.txt file with installed dependencies versions"
	@echo "  test                          -- to launch base test suite using Pytest"
	@echo "  test-initial                  -- to launch tests with pytest and re-initialized database (for after new application or model changes)"
	@echo "  quality                       -- to run tests, migration check and Flake linter"
	@echo

clean-pycache:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Cleaning Python cache <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf .pytest_cache
	find . -type d -name "__pycache__"|xargs rm -Rf
	find . -name "*\.pyc"|xargs rm -f
.PHONY: clean-pycache

clean-var:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Cleaning var/ directory <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf var
.PHONY: clean-var

clean-backend-install: clean-pycache
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Cleaning backend install <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf $(VENV_PATH)
.PHONY: clean-backend-install

clean-frontend-build:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Cleaning frontend built files <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf parts/webpack-stats.json
	rm -Rf $(STATICFILES_DIR)/css
	rm -Rf $(STATICFILES_DIR)/js
.PHONY: clean-frontend-build

clean-frontend-install:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Cleaning frontend install <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf $(FRONTEND_DIR)/node_modules
.PHONY: clean-frontend-install

clean: clean-var clean-backend-install clean-frontend-install clean-frontend-build clean-pycache
.PHONY: clean

venv:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Install virtual environment <---$(FORMATRESET)\n"
	@echo ""
	virtualenv -p $(PYTHON_INTERPRETER) $(VENV_PATH)
	# This is required for those ones using old distribution
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade setuptools
.PHONY: venv

requirements:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Build base requirements file <---$(FORMATRESET)\n"
	@echo ""
	$(PIP) install -r requirements/composer.txt
	$(PROJECT_COMPOSER) -v 5 requirements --dump requirements/base.txt
.PHONY: requirements

create-var-dirs:
	@mkdir -p var/db
	@mkdir -p var/media
	@mkdir -p var/static
	@mkdir -p $(DJANGOPROJECT_DIR)/media
	@mkdir -p $(STATICFILES_DIR)/fonts
.PHONY: create-var-dirs

icon-font:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Copying bootstrap-icons to staticfiles directory <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf $(STATICFILES_DIR)/fonts/icons
	cp -r $(FRONTEND_DIR)/node_modules/bootstrap-icons/font/fonts $(STATICFILES_DIR)/fonts/icons
.PHONY: icon-font

install-backend:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Installing backend requirements <---$(FORMATRESET)\n"
	@echo ""
	$(PIP) install -r requirements/development.txt -r requirements/codestyle.txt -r requirements/toolbox.txt
.PHONY: install-backend

install-frontend:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Installing frontend requirements <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm install
	#${MAKE} icon-font
.PHONY: install-frontend

install: venv create-var-dirs requirements install-backend migrate disk-init install-frontend
.PHONY: install

update-backend: requirements install-backend migrate disk-init
.PHONY: update-backend

update-frontend: install-frontend frontend
.PHONY: update-frontend

update: update-backend update-frontend
.PHONY: update

check-apps:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Discovering app directories <---$(FORMATRESET)\n"
	@echo ""
	@$(PROJECT_APPS)
.PHONY: check-apps

check-composer:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Running Project composer check <---$(FORMATRESET)\n"
	@echo ""
	$(PYTHON_BIN) ./$(DJANGOAPPS_DIR)/project_utils/composer_check.py
.PHONY: check-composer

check-django:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Running Django System check framework <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) check
.PHONY: check-django

check-migrations: check-apps
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Checking for pending project applications models migrations <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) makemigrations --check --dry-run -v 3 `$(PROJECT_APPS)`
.PHONY: check-migrations

check-disk:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Checking Diskette dump configuration <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) diskette_dump -v 2 --check
.PHONY: check-disk

check-comb:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Making Dependency comb report <---$(FORMATRESET)\n"
	@echo ""
	$(COMB) -v 5 report --failures --format=rich requirements/base.txt
.PHONY: check-comb

check-black:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Running Black checking <---$(FORMATRESET)\n"
	@echo ""
	$(BLACK) --check $(DJANGOPROJECT_DIR) $(DJANGOAPPS_DIR) tests composition_repository
.PHONY: check-black

check-templates:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Checking djLint formatting on templates sources <---$(FORMATRESET)\n"
	@echo ""
	$(DJLINT) --check project/templates/
.PHONY: check-templates

check: check-composer check-django check-migrations check-disk
.PHONY: check

migrations: check-apps
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Creating pending applications models migrations <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) makemigrations -v 3 `$(PROJECT_APPS)`
.PHONY: migrations

migrate:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Applying pending migrations <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) migrate
.PHONY: migrate

superuser:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Creating new superuser <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) createsuperuser
.PHONY: superuser

new-app:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Creating a new application <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) startapp
.PHONY: new-app

run:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Running development server <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) runserver 0.0.0.0:8001
.PHONY: run

css:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Building CSS for development environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run-script css
.PHONY: css

watch-sass:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Watching Sass sources for development environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run-script watch-css
.PHONY: watch-sass

css-prod:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Building CSS for production environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run-script css-prod
.PHONY: css-prod

js:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Building distributed Javascript for development environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run js
.PHONY: js

watch-js:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Watching Javascript sources for development environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run watch-js
.PHONY: watch-js

js-prod:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Building distributed Javascript for production environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run js-prod
.PHONY: js-prod

frontend: css js
.PHONY: frontend

frontend-prod: css-prod js-prod
.PHONY: frontend-prod

po:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Updating project PO files <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) makemessages -a --keep-pot --no-obsolete
.PHONY: po

mo:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Building project MO files <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) compilemessages --verbosity 3 --ignore='.venv' --ignore='frontend/node_modules' --ignore='tests' --ignore='var' --ignore='.git' --ignore='.pytest_cache' --ignore='chart' --ignore='requirements'
.PHONY: mo

disk-init:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Build Diskette definitions file <---$(FORMATRESET)\n"
	@echo ""
	$(PYTHON_BIN) ./django-apps/project_utils/diskette_definitions.py
.PHONY: disk-init

disk-dump:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Creating a Diskette archive <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) diskette_dump -v 2 --filename diskette_data_storages.tar.gz
.PHONY: disk-dump

disk-load:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Loading local Diskette archive <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf var/backup_db
	rm -Rf var/backup_media
	mv var/db var/backup_db
	mv var/media var/backup_media
	$(MAKE) create-var-dirs
	$(MAKE) migrate
	$(DJANGO_MANAGE) diskette_load -v 2 --keep --storages-basepath . diskette_data_storages.tar.gz
.PHONY: disk-load

flake:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Flake <---$(FORMATRESET)\n"
	@echo ""
	$(FLAKE) --statistics --show-source $(DJANGOPROJECT_DIR) $(DJANGOAPPS_DIR) tests composition_repository
.PHONY: flake

black-write:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Apply Black reformating <---$(FORMATRESET)\n"
	@echo ""
	$(BLACK) --verbose $(DJANGOPROJECT_DIR) $(DJANGOAPPS_DIR) tests composition_repository
.PHONY: black-write

lint-templates:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Running djLint linting on templates sources <---$(FORMATRESET)\n"
	@echo ""
	$(DJLINT) project/templates/
.PHONY: lint-templates

lint-scss:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Running Stylelint on Sass sources <---$(FORMATRESET)\n"
	@echo ""
	cd frontend && npx stylelint --ignore-path .stylelintignore "scss/**/*.scss"
.PHONY: lint-scss

lint-frontend: lint-templates lint-scss
.PHONY: lint-frontend

test:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Tests <---$(FORMATRESET)\n"
	@echo ""
	$(PYTEST) --reuse-db tests/
	rm -Rf var/media-tests/
.PHONY: test

test-initial:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Tests from zero <---$(FORMATRESET)\n"
	@echo ""
	$(PYTEST) --reuse-db --create-db tests/
	rm -Rf var/media-tests/
.PHONY: test-initial

fix-templates:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Running djLint formatting on templates sources <---$(FORMATRESET)\n"
	@echo ""
	$(DJLINT) --warn --quiet --reformat project/templates/
.PHONY: fix-templates

fix-scss:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> (WIP) Running Stylelint formatting on Sass sources <---$(FORMATRESET)\n"
	@echo ""
	cd frontend && npx stylelint --ignore-path .stylelintignore --fix "scss/**/*.scss"
.PHONY: fix-scss

fix-frontend: fix-scss fix-templates
	@echo ""
	@echo "✓ ✓ Frontend should be correctly formatted ✓ ✓"
	@echo ""
.PHONY: fix-frontend

freeze-dependencies:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Freeze dependencies versions <---$(FORMATRESET)\n"
	@echo ""
	$(PIP) freeze --all --local > requirements/frozen.txt
.PHONY: freeze-dependencies

quality: test-initial flake check-migrations
	@echo ""
	@echo "♥ ♥ Everything should be fine ♥ ♥"
	@echo ""
.PHONY: quality
