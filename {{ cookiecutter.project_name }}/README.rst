.. _Python: https://www.python.org/
.. _Django: https://www.djangoproject.com/{% if cookiecutter.enable_drf|lower == 'true' %}
.. _Django REST framework: https://www.django-rest-framework.org/{% endif %}

{{ '=' * cookiecutter.project_title|length }}
{{ cookiecutter.project_title }}
{{ '=' * cookiecutter.project_title|length }}

{{ cookiecutter.project_short_description|wordwrap(80) }}

Dependancies
************

* `Python`_>=3.8;
* `Django`_>=4.0;{% if cookiecutter.enable_drf|lower == 'true' %}
* `Django REST framework`_>=3.13.1;{% endif %}

Install
*******

First ::

    make install

Then: ::

    make frontend

Usage
*****

::

    make run
