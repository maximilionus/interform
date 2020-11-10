Installation Guide
===================================

Before Installation
-----------------------------------

About Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For example, I will install the ``configurio`` with ``ujson`` parser:

.. code-block:: bash

    pip install configurio[ujson]

Install with pip
--------------------------------------

How to install the ``configurio`` from **PyPI**:

#. Run

    .. code-block:: bash

        pip install configurio

Install from Github
--------------------------------------
``pip`` also supports installs from git repositories, so you can install this package directly from github.

To do this, run:

.. code-block:: bash

    pip install git+https://github.com/maximilionus/configurio.git

.. note::

    Installing via this link will download and install the latest available version of ``configurio`` package. To install the specific version of package you should add ``@vX.X.X`` to the end of git repo link. So, for example, you can install version *1.0.0* like this:

    .. code-block:: bash

        pip install git+https://github.com/maximilionus/configurio.git@v1.0.0

Install from source
--------------------------------------
How to install ``configurio`` from source files:

.. warning::
    Due to how the ``setup.py`` deals with external dependencies, you can't install this package properly by running setup directly from file:

    .. code-block:: bash

        python setup.py install

#. Download source files from `github releases <https://github.com/maximilionus/configurio/releases>`_
#. Inside of the downloaded directory, run:

    .. code-block:: bash

        pip install .

.. note::
    If you want to install ``configurio`` with support for any external package(-s), you can also specify it like this:

    .. code-block:: bash

        pip install .[mode]
