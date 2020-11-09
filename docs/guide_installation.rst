Installation Guide
====================================

Before Installation
----------------------------------

About Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``configurio`` module comes with support for various languages parsers. Yet, not all of this parsers are natively available in python. By default, ``configurio`` will not install any external packages, so if your language is not in :ref:`general-supported-langs` -> **Native Support**, you will have to specify the installation mode for ``configurio`` with this command:

.. code-block:: bash

    pip install configurio[mode]

Where ``mode`` is one of the listed in `Installation Modes`_ options:

Installation Modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:ujson:
    Replace the built-in ``json`` parser with `ujson module <https://pypi.org/project/ujson/>`_

:yaml:
    Support for the ``YAML`` language *(version <= 1.2)* with `ruamel.yaml module <https://pypi.org/project/ruamel.yaml/>`_

Example
~~~~~~~~~~~~~~
For example, I will install the ``configurio`` with ``ujson`` parser:

.. code-block:: bash

    pip install configurio[ujson]

PIP Installation
--------------------------------

How to install the ``configurio`` from **PyPI**:

#. Run

    .. code-block:: bash

        pip install configurio

Source Installation
--------------------------------------

How to install ``configurio`` from source files:

#. Download source files from `github releases <https://github.com/maximilionus/configurio/releases>`_
#. Inside of the downloaded directory, run:

    .. code-block:: bash

        pip install .

:Note:
    If you want to install ``configurio`` with support for any external package(-s), you can also specify it like this:

    .. code-block:: bash

        pip install .[mode]
