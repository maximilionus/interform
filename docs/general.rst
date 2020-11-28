General Information
=======================================

.. contents:: Table of Contents
    :depth: 2
    :local:

About
--------------------------------
``serialix`` is a powerful and easy-to-use tool that provides a unified interaction layer for various data interchange formats *(DIF)* like json, yaml, etc. Due to the how this tool designed, all the supported languages share the identical base between each other, meaning that process of working with those languages will be almost the same. Tool can also be extended for your purposes or even your own DIF language parser support.


Supported Languages
--------------------------------

Names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
List of currently supported languages.

- Native Support
    - ``json``
- External Support
    - ``ujson`` *(replacement for python built-in json parser)*
    - ``yaml`` *(version <= 1.2)*
    - ``toml``

.. note::
    Languages, listed in **Native Support** are supported by python without any external packages, while **External Support** requires external packages to be installed. For more detailed information go here: :doc:`guide_installation`

Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
List of classes for supported DIF languages, that can be used:

:``JSON_Format``:
    Support for JSON language. Absolutely the same for built-in and external (ujson) ``json`` parsers.

:``YAML_Format``:
    Support for YAML language

:``TOML_Format``:
    Support for TOML language


All ``serialix``'s supported languages are easy to access and can be imported straight from main package without stating any subpackage or submodule:

.. code:: python

    from serialix import <lang_class_here>

    # <lang_class_here> should be replaced
    # with any class name listed above


Module Hierarchy
--------------------------------
- ``serialix`` - Contains main language parsers and module meta information imports for easy access.
    - ``core`` - Realisation of basic features, that will be inherited and used in other modules.
    - ``meta`` - Meta information, like version, author, etc.
    - ``cli`` - CLI realisation module. No public API available.
    - ``langs`` - Subpackage with realisation of main features for various DIF languages
        - ``json``
        - ``toml``
        - ``yaml``
    - ``tests`` - PyTest unit testing suite subpackage
