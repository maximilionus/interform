General Information
=======================================

About
--------------------------------
``serialix`` is a powerful and easy-to-use tool that provides unified API for various human-readable data serialization formats (like ``json``, ``yaml``, etc). Due to the how this tool designed, all the supported formats share the identical base between each other, meaning that switching between them will be almost the same. This tool can also be extended for your purposes or even your own serialization format support.

Usage example
--------------------------------
``serialix`` is very easy to use:

.. code:: python

    >>> from serialix import Serialix, JSON_Format                        # Import `Serialix` main class
    >>> default_settings = { 'version': '1.23.2' }                        # Specify the default values for our file
    >>> cfg = Serialix(JSON_Format, './settings.json', default_settings)  # Create serialix object for `json` format.
                                                                          # Local file will be automatically created.
    >>> cfg['version']                                                    # Read the `version` key
    '1.23.2'
    >>> cfg['version'] = '2.0.0'                                          # Change the `version` key value
    >>> cfg['version']                                                    # Read the values of `version` key again
    '2.0.0'
    >>> cfg.commit()                                                      # Commit the changes to local `settings.json` file

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
    Unified instance generator for any supported format. Implemented in version ``2.1.0`` and should be preferred as the main entry point for any interaction with this package.

:``JSON_Format``:
    Support for JSON format. Absolutely the same for built-in and external (ujson) ``json`` parsers.

:``YAML_Format``:
    Support for YAML format

:``TOML_Format``:
    Support for TOML format

Module Hierarchy
--------------------------------
- ``serialix`` - Contains main formats parsers and module meta information imports for easy access.
    - ``core`` - Realisation of basic features, that will be inherited and used in other modules.
    - ``meta`` - Meta information, like version, author, etc.
    - ``serialix`` - Instance generator implementation
    - ``cli`` - CLI realisation module. No public API available.
    - ``langs`` - Subpackage with implementation of main features for various serialization formats
        - ``json``
        - ``toml``
        - ``yaml``
    - ``tests`` - PyTest unit testing suite
