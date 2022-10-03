.. _Python: https://www.python.org/
.. _Django: https://www.djangoproject.com/
.. _Node.js: https://nodejs.org/dist/latest-v16.x/docs/api/
.. _NPM: https://docs.npmjs.com/
.. _Bootstrap: https://getbootstrap.com/docs/
.. _project-composer: https://github.com/sveetch/project-composer
.. _Webpack: https://webpack.js.org/
.. _django-configurations: https://django-configurations.readthedocs.io/

{{ '=' * cookiecutter.project_title|length }}
{{ cookiecutter.project_title }}
{{ '=' * cookiecutter.project_title|length }}

*Generated from cookiecutter-bireli=={{ cookiecutter._bireli_version }}*

{{ cookiecutter.project_short_description|wordwrap(80) }}


Main stack components
*********************

* `Python`_ {{ cookiecutter._python_version }};
* `Django`_ {{ cookiecutter._django_version }};
* `project-composer`_ {{ cookiecutter._project_composer_version }};
* `django-configurations`_ {{ cookiecutter._django_configurations_version }};
* `Node.js`_ {{ cookiecutter._node_version }};
* `NPM`_ {{ cookiecutter._npm_version }};
* `Bootstrap`_ {{ cookiecutter._bootstrap_version }};


Install
*******

First ::

    make install

Then: ::

    make frontend

Finally you will need a super user to login into admin: ::

    make superuser

Usage
*****

::

    make run

There is a lot of useful Makefile commands to manage your project, read the Makefile
help: ::

    make help
