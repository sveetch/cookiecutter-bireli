.. _Python: https://www.python.org/
.. _Django: https://www.djangoproject.com/{% if cookiecutter.enable_drf|lower == 'true' %}
.. _Django REST framework: https://www.django-rest-framework.org/{% endif %}
.. _Node.js: https://nodejs.org/dist/latest-v16.x/docs/api/
.. _NPM: https://docs.npmjs.com/
.. _Bootstrap: https://getbootstrap.com/docs/
.. _Webpack: https://webpack.js.org/

{{ '=' * cookiecutter.project_title|length }}
{{ cookiecutter.project_title }}
{{ '=' * cookiecutter.project_title|length }}

{{ cookiecutter.project_short_description|wordwrap(80) }}


Main stack components
*********************

* `Python`_ {{ cookiecutter._python_version }};
* `Django`_ {{ cookiecutter._django_version }};{% if cookiecutter.enable_drf|lower == 'true' %}
* `Django REST framework`_ {{ cookiecutter._drf_version }};{% endif %}
* `Node.js`_ {{ cookiecutter._node_version }};
* `NPM`_ {{ cookiecutter._npm_version }};
* `Bootstrap`_ {{ cookiecutter._bootstrap_version }};
* `Webpack`_ {{ cookiecutter._webpack_version }};


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
