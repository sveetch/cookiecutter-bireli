VENV_PATH=.venv
VENV_BIN=$(VENV_PATH)/bin

PYTHON_INTERPRETER=python3
PYTHON_BIN=$(VENV_BIN)/python

PIP=$(VENV_BIN)/pip
PROJECT_COMPOSER=$(VENV_BIN)/project_composer
DJANGO_MANAGE=$(VENV_BIN)/python manage.py
FLAKE=$(VENV_BIN)/flake8
PYTEST=$(VENV_BIN)/pytest

DJANGOPROJECT_DIR=project
STATICFILES_DIR=$(DJANGOPROJECT_DIR)/static-sources
FRONTEND_DIR=frontend

# Formatting variables, FORMATRESET is always to be used last to close formatting
FORMATBLUE:=$(shell tput setab 4)
FORMATBOLD:=$(shell tput bold)
FORMATRESET:=$(shell tput sgr0)

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  requirements                  -- to build base requirements file for enabled applications from composition manifest"
	@echo
	@echo "  install-backend               -- to install backend requirements with Virtualenv and Pip"
	@echo "  install-frontend              -- to install frontend requirements with Npm"
	@echo "  install                       -- to install backend and frontend"
	@echo
	@echo "  freeze-dependencies           -- to write a frozen.txt file with installed dependencies versions"
	@echo
	@echo "  clean                         -- to clean EVERYTHING (WARNING: you cannot recovery from this)"
	@echo "  clean-var                     -- to clean data (uploaded medias, database, etc..)"
	@echo "  clean-backend-install         -- to clean backend installation"
	@echo "  clean-frontend-install        -- to clean frontend installation"
	@echo "  clean-frontend-build          -- to clean frontend built files"
	@echo "  clean-pycache                 -- to remove all __pycache__, this is recursive from current directory"
	@echo
	@echo "  run                           -- to run Django development server"
	@echo "  check-migrations              -- to check for pending application migrations (do not write anything)"
	@echo "  migrate                       -- to apply demo database migrations"
	@echo "  superuser                     -- to create a superuser for Django admin"
	@echo
	@echo "  css                           -- to build CSS with default environnement"
	@echo "  watch-css                     -- to launch watcher CSS with default environnement"
	@echo "  css-prod                      -- to build CSS with production environnement"
	@echo
	@echo "  js                            -- to build distributed Javascript with default environnement"
	@echo "  watch-js                      -- to launch watcher for Javascript sources with default environnement"
	@echo "  js-prod                       -- to build distributed Javascript with production environnement"
	@echo
	@echo "  frontend                      -- to build frontend assets from sources (CSS and JS) with default environnement"
	@echo "  frontend-prod                 -- to build frontend assets from sources (CSS and JS) with production environnement"
	@echo
	@echo "  flake                         -- to launch Flake8 checking"
	@echo "  test                          -- to launch base test suite using Pytest"
	@echo "  test-initial                  -- to launch tests with pytest and re-initialized database (for after new application or model changes)"
	@echo "  quality                       -- to launch Flake8 checking and every tests suites"
	@echo

clean-pycache:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Clear Python cache <---$(FORMATRESET)\n"
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

clean-backend-install:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Cleaning backend install <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf $(VENV_PATH)
.PHONY: clean-backend-install

clean-frontend-build:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Cleaning frontend built files <---$(FORMATRESET)\n"
	@echo ""
	rm -Rf $(STATICFILES_DIR)/webpack-stats.json
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
	$(PIP) install -r requirements/development.txt
.PHONY: install-backend

install-frontend:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Installing frontend requirements <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm install
	${MAKE} icon-font
.PHONY: install-frontend

install: venv create-var-dirs requirements install-backend migrate install-frontend
.PHONY: install

check-migrations:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Checking for pending project applications models migrations <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) makemigrations --check --dry-run -v 3
.PHONY: check-migrations

migrate:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Apply pending migrations <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) migrate
.PHONY: migrate

superuser:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Create new superuser <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) createsuperuser
.PHONY: superuser

run:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Running development server <---$(FORMATRESET)\n"
	@echo ""
	$(DJANGO_MANAGE) runserver 0.0.0.0:8001
.PHONY: run

css:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Build CSS for development environment <---$(FORMATRESET)\n"
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
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Build CSS for production environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run-script css-prod
.PHONY: css-prod

js:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Build distributed Javascript for development environment <---$(FORMATRESET)\n"
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
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Build distributed Javascript for production environment <---$(FORMATRESET)\n"
	@echo ""
	cd $(FRONTEND_DIR) && npm run js-prod
.PHONY: js-prod

frontend: css js
.PHONY: frontend

frontend-prod: css-prod js-prod
.PHONY: frontend-prod

flake:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Flake <---$(FORMATRESET)\n"
	@echo ""
	$(FLAKE) --statistics --show-source $(DJANGOPROJECT_DIR) django-apps tests composition_repository
.PHONY: flake

test:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Tests <---$(FORMATRESET)\n"
	@echo ""
	$(PYTEST) -vv --reuse-db tests/
	rm -Rf var/media-tests/
.PHONY: test

test-initial:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Tests from zero <---$(FORMATRESET)\n"
	@echo ""
	$(PYTEST) -vv --reuse-db --create-db tests/
	rm -Rf var/media-tests/
.PHONY: test-initial

freeze-dependencies:
	@echo ""
	@printf "$(FORMATBLUE)$(FORMATBOLD)---> Freeze dependencies versions <---$(FORMATRESET)\n"
	@echo ""
	$(PIP) freeze --all --local > requirements/requirements_freeze.txt
.PHONY: freeze-dependencies

quality: test-initial flake check-migrations
	@echo ""
	@echo "♥ ♥ Everything should be fine ♥ ♥"
	@echo ""
.PHONY: quality
