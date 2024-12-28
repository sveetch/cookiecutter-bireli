.. _node-sass: https://github.com/sass/node-sass
.. _django-webpack-loader: https://github.com/django-webpack/django-webpack-loader
.. _Webpack: https://webpack.js.org/
.. _Sass language: https://sass-lang.com/documentation/
.. _sass: https://www.npmjs.com/package/sass
.. _sass-embedded: https://www.npmjs.com/package/sass-embedded
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

Compiled CSS files (from Sass sources) are not managed from Webpack because it is too
slow during its JavaScript build phase and would slow down the CSS build.

So these CSS files are just loaded as simple static files without the Django Webpack
layer.


Webdesign integration
---------------------

Layout stylesheets (CSS) are built from `Sass language`_ sources.

It is not allowed to use inline styles in templates and no *scoped* style from
Javascript interfaces. The only source of truth for layout stylesheets are the Sass
sources.

We are using Sass compiler `sass-embedded`_ that is an Npm package which embed the Dart
binary instead of legacy `sass`_ package that just ship a pure JavaScript
implementation. This is because the pure JavaScript implementation is largely slower
that the Dart binary.

.. Note::
    Previously we used `node-sass`_ that was developed with the "Libsass" engine that is
    unmaintained and not uptodate with the last `Sass language`_ features.

    So we have moved to the "Dartsass" engine that is the new legacy.

Default project frontend use `Bootstrap`_ framework and all templates are made with its
components.

.. Note::
    Although the current last version of Bootstrap (v5.3.3) is fully working with
    Dartsass engine, it did not have migrated yet to the last language changes and so
    raise some warnings from compiler. Commandline script to build CSS has temporarily
    muted these warnings until next Bootstrap version.


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
