General Information
=======================================

About
--------------------------------
``serialix`` is a powerful and easy-to-use tool that provides a unified interaction layer for various data interchange formats *(DIF)* like json, yaml, etc. Due to the how this tool designed, all the supported languages share the identical base between each other, meaning that process of working with those languages will be almost the same. Tool can also be extended for your purposes or even your own DIF language parser support.

Usage example
--------------------------------
``serialix`` is very easy to use:

.. code:: python

    >>> from serialix import Serialix                                # Import `Serialix` main class
    >>> default_settings = { 'version': '1.23.2' }                   # Specify the default values for our file
    >>> cfg = Serialix('json', './settings.json', default_settings)  # Create serialix object for `json` format.
                                                                     # Local file will be automatically created.
    >>> cfg['version']                                               # Read the `version` key
    '1.23.2'
    >>> cfg['version'] = '2.0.0'                                     # Change the `version` key value
    >>> cfg['version']                                               # Read the values of `version` key again
    '2.0.0'
    >>> cfg.commit()                                                 # Commit the changes to local `settings.json` file

Supported Languages
--------------------------------

List
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

Public Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
List of classes for supported DIF languages, that can be used:

:``Serialix``:
    Unified instance generator for any supported language. Implemented in version ``2.1.0`` and should be preferred as the main entry point for any interaction with this package.

:``JSON_Format``:
    Support for JSON language. Absolutely the same for built-in and external (ujson) ``json`` parsers.

:``YAML_Format``:
    Support for YAML language

:``TOML_Format``:
    Support for TOML language

Module Hierarchy
--------------------------------
- ``serialix`` - Contains main language parsers and module meta information imports for easy access.
    - ``core`` - Realisation of basic features, that will be inherited and used in other modules.
    - ``meta`` - Meta information, like version, author, etc.
    - ``serialix`` - Instance generator implementation
    - ``cli`` - CLI realisation module. No public API available.
    - ``langs`` - Subpackage with realisation of main features for various DIF languages
        - ``json``
        - ``toml``
        - ``yaml``
    - ``tests`` - PyTest unit testing suite
