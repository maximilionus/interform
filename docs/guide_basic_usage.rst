Basic Usage
======================

About
----------------------
In this section you can find a quickstart guide to ``interform`` package, that will show you the basics of how this tool can be used. For more code examples you can see `the examples directory on Github <https://github.com/maximilionus/interform/tree/master/examples>`_.


Guide
----------------------
``interform`` supports various data interchange languages (:ref:`full list <general-supported-langs>`). This quickstart guide will be based on ``json`` language and executed directly in python interpreter.

1. Let's open the interpreter and import the json language class from ``interform`` package

.. code:: python

    >>> from interform import JSON_Format

2. Next step we will define the default dictionary, that will be used in next step.

.. code:: python

    >>> def_cfg = {
        "version": 5,
        "rand_key": "da"
    }


.. note::
    Specifying the default dictionary is an optional step and not required in your code if you don't need it, but this will allow us to specify the values, that will be written in local file on creation
