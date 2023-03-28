.. _node-sass: https://github.com/sass/node-sass
.. _django-webpack-loader: https://github.com/django-webpack/django-webpack-loader
.. _Webpack: https://webpack.js.org/
.. _Sass: https://sass-lang.com/documentation/
.. _Bootstrap: https://getbootstrap.com/

.. _intro_project_frontend:

========
Frontend
========

Frontend base dependencies
**************************

.. bireli-frontend-stack::


Asset management
----------------

Frontend assets are managed with `Webpack`_ and Django is aware of them through
`django-webpack-loader`_ so you can load them from templates.

Compiled CSS from Sass sources are not managed from Webpack since there is currently no
Sass compiler that are properly usable. So these CSS files are just loaded as simple
static files.


Webdesign integration
---------------------

Layout stylesheets (CSS) are built from `Sass`_ sources.

It is not allowed to use inline styles in templates and no *scoped* style from
Javascript interfaces. The only source of truth for layout stylesheets are the Sass
sources.

The build from Sass to CSS is performed from the frontend stack with `node-sass`_. We
still use `node-sass`_ because it's still the fastest compiler in Javascript.

Default project frontend use `Bootstrap`_ framework and all templates are made with its
components.


Javascript interface
--------------------

Default Javascript sources shipped in a project are basic and just load the Bootstrap
components. Code sources are to be done for ES6 and jQuery is still available.

Logo and favicon
----------------

A project is generated with a default logo and favicon that you should change to fit
to your project brand design.

Note than favicon is configured using a site manifest to cover multiple devices
behaviors, you may build a new full site manifest from online tool like
`Favicon Generator <https://realfavicongenerator.net/>`_ (recommended).
