Installation Guide
===================================

Before Installation
-----------------------------------

About Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``interform`` module comes with support for various languages parsers. Yet, not all of this parsers are natively available in python. By default, ``interform`` will not install any external packages, so if your language is not in `Supported Languages <general.html#supported-languages>`__ -> **Native Support**, you will have to specify the installation mode for ``interform`` with this command:

.. code-block:: bash

    pip install interform[mode]

Where ``mode`` is one of the listed in `Installation Modes`_ options:

Installation Modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:``ujson``:
    Will automatically replace the built-in ``json`` parser with `ujson parser <https://pypi.org/project/ujson/>`__

:``yaml``:
    Support for ``YAML`` language *(version <= 1.2)* with `ruamel.yaml parser <https://pypi.org/project/ruamel.yaml/>`__

:``toml``:
    Support for ``TOML`` language with `toml parser <https://pypi.org/project/toml/>`__

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

#. Download source files from `github releases <https://github.com/maximilionus/interform/releases>`__

For usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
    Due to how the ``setup.py`` deals with external dependencies, you can't install this package properly by running setup directly from file:

    .. code-block:: bash

        python setup.py install

2. Inside of the downloaded directory, run:

    .. code-block:: bash

        pip install .

.. note::
    If you want to install ``interform`` with support for any external package(-s), you can also specify it like this:

    .. code-block:: bash

        pip install .[mode]

For development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2. *(Optional)* Inside of the project folder prepare the virtual environment and activate it
3. Install all dev dependencies with this command

    .. code-block:: bash

        pip install -r requirements-dev.txt
4. You're ready to go. Good luck 👍
