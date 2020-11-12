Installation Guide
===================================

Before Installation
-----------------------------------

About Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``interform`` module comes with support for various languages parsers. Yet, not all of this parsers are natively available in python. By default, ``interform`` will not install any external packages, so if your language is not in :ref:`general-supported-langs` -> **Native Support**, you will have to specify the installation mode for ``interform`` with this command:

.. code-block:: bash

    pip install interform[mode]

Where ``mode`` is one of the listed in `Installation Modes`_ options:

Installation Modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:``ujson``:
    Replace the built-in ``json`` parser with `ujson package <https://pypi.org/project/ujson/>`_

:``yaml``:
    Support for the ``YAML`` language *(version <= 1.2)* with `ruamel.yaml package <https://pypi.org/project/ruamel.yaml/>`_

:``xml``:
    Support for the ``XML`` language with built-in python modules and `xmltodict package <https://github.com/martinblech/xmltodict>`_

:``full``:
    Install ``interform`` with support for all external parsers listed above

:``test``:
    Full installation with unit testing support (via `pytest <https://pypi.org/project/pytest/>`_ package)

Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For example, to install the ``interform`` with ``ujson`` parser:

.. code-block:: bash

    pip install interform[ujson]

Install with pip
--------------------------------------

How to install the ``interform`` from **PyPI**:

#. Run

    .. code-block:: bash

        pip install interform

Install from Github
--------------------------------------
``pip`` also supports installs from git repositories, so you can install this package directly from github.

To do this, run:

.. code-block:: bash

    pip install git+https://github.com/maximilionus/interform.git

.. note::

    Installing via this link will download and install the latest available version of ``interform`` package. To install the specific version of package you should add ``@vX.X.X`` to the end of git repo link. So, for example, you can install version *1.0.0* like this:

    .. code-block:: bash

        pip install git+https://github.com/maximilionus/interform.git@v1.0.0

Install from source
--------------------------------------
How to install ``interform`` from source files:

.. warning::
    Due to how the ``setup.py`` deals with external dependencies, you can't install this package properly by running setup directly from file:

    .. code-block:: bash

        python setup.py install

#. Download source files from `github releases <https://github.com/maximilionus/interform/releases>`_
#. Inside of the downloaded directory, run:

    .. code-block:: bash

        pip install .

.. note::
    If you want to install ``interform`` with support for any external package(-s), you can also specify it like this:

    .. code-block:: bash

        pip install .[mode]
