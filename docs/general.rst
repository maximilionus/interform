General Information
=======================================

About
----------
``interform`` is a powerful and easy-to-use tool that provides a unified interaction layer for various data interchange formats *(DIF)* like ``json``, ``yaml``, etc. Due to the how this tool designed, all the supported languages share the identical base between each other, meaning that process of working with those languages will be absolutely the same. Tool can also be extended for your purposes or even your own DIF language parser support.


.. _general-supported-langs:

Supported Languages
--------------------------------------
List of currently supported languages.

- Native Support
    - ``json``
- External Support
    - ``ujson`` *(replacement for python built-in json parser)*
    - ``yaml`` *(version <= 1.2)*
    - ``xml``

.. note::
    Languages, listed in **Native Support** are supported by python without any external packages, while **External Support** requires external packages to be installed. For more detailed information go here: :doc:`guide_installation`

Module Hierarchy
--------------------------------
- ``interform`` - Contains main language parsers and module meta information imports for easy access.
    - ``core`` - Realisation of basic features, that will be inherited and used in other modules.
    - ``meta`` - Meta information, like version, author, etc.
    - ``langs`` - Subpackage with realisation of main features for various DIF languages
        - ``json``
        - ``yaml``
        - ``ini``
    - ``tests`` - PyTest unit testing suite subpackage
