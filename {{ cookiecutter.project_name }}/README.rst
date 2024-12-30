.. _Python: https://www.python.org/
.. _Django: https://www.djangoproject.com/
.. _Node.js: https://nodejs.org/dist/latest-v16.x/docs/api/
.. _NPM: https://docs.npmjs.com/
.. _Bootstrap: https://getbootstrap.com/docs/
.. _project-composer: https://github.com/sveetch/project-composer
.. _Webpack: https://webpack.js.org/
.. _django-configurations: https://django-configurations.readthedocs.io/
.. _Bireli: https://cookiecutter-bireli.readthedocs.io/en/{{ cookiecutter._bireli_version }}/

{{ '=' * cookiecutter.project_title|length }}
{{ cookiecutter.project_title }}
{{ '=' * cookiecutter.project_title|length }}

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

First steps
***********

This project has been generated from ``cookiecutter-bireli=={{ cookiecutter._bireli_version }}``.
You may learn more about your project usage on `Bireli`_ documentation.


Quick install
*************

Install backend and frontend, then build frontend and finally add some dummy initial
datas: ::

    make install frontend

You will need an admin user, create it with: ::

    make superuser

Once finished, you may ensure everything is working as expected with: ::

    make quality


Quick usage
***********

Just run the development server: ::

    make run

And open your browser on ``http://localhost:8001/``.


Further
*******

There is a lot of useful Makefile tasks to manage your project, read the Makefile
help: ::

    make help

And see `Bireli`_ documentation about project usage to know more.
