CLI Toolset
========================


About
------------------------
Since version **1.3.0** ``serialix`` has a built-in command line interface *(CLI)* toolset that can be accessed from terminal. It provides various tools for quick work with data interchange format files.

**CLI** module can be accessed with executing any of this commands:

.. code-block:: bash

    $ serialixcli

.. code-block:: bash

    $ python -m serialix.cli

Executing one of the above commands with no arguments or with the ``--help`` (``-h``) argument will print the *help* message with information about all available tools.


Tools
------------------------

``convert``
~~~~~~~~~~~~~~~~~~~~~~~~

About
""""""""""""""""""""""""
Tool for conversion between supported languages

Usage
""""""""""""""""""""""""

.. code-block:: bash

    serialixcli convert [-h] from_path from_format dest_path dest_format

    positional arguments:
    from_path    path to the file to be converted
    from_format  format of the file to be converted
    dest_path    desired path to converted file
    dest_format  desired file format

Example
"""""""""""""""""""""""""
Convert the existing file with name ``userlist.json`` in ``json`` format to new ``userlist.yaml`` file in ``yaml`` format

.. code-block:: bash

    $ serialixcli convert userlist.json json userlist.yaml yaml
    successfully converted "userlist.json" from "json" to "yaml" and saved the result to "userlist.yaml"
