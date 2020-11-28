Basic Usage
======================

.. contents::
    :local:

About
----------------------
In this section you can find a quickstart guide to ``serialix`` package, that will show you the basics of how this tool can be used. For more code examples you can see `the examples directory on Github <https://github.com/maximilionus/serialix/tree/master/examples>`_.


Quickstart
----------------------
``serialix`` supports various data interchange languages (`full list <general.html#supported-languages>`__). This quickstart guide will be based on ``json`` language.

Imports
~~~~~~~~~~~~~~~~~~~~~~
Let's import the json language class from ``serialix`` package

.. code-block:: python
    :linenos:

    from serialix import JSON_Format

.. note::
    Detailed ``JSON_Format`` documentation `can be found here <serialix.langs.html#module-serialix.langs.json>`__

Preparation
~~~~~~~~~~~~~~~~~~~~~~

Default values
""""""""""""""""""""""
Next step we will define the default dictionary, that will be used later. Keys and values in it are absolutely random and meaningless 🙂.

.. code-block:: python
    :linenos:
    :lineno-start: 2

    def_dict = {
        "version": 5,
        "app_name": "Test"
    }


.. note::
    Specifying the default dictionary **is optional** and not required in your code, but this will allow us to specify values that will be written to a local file on creation and can be used for a "factory reset" feature later.

Parser Settings
""""""""""""""""""""""
.. versionadded:: 1.1.0

Let's also prepare some options for ``json`` parser

.. code-block:: python
    :linenos:
    :lineno-start: 6

    parser_write_kwargs = {
        "indent": 4
    }

``parser_write_kwargs`` variable is dictionary with keyword arguments that will be further passed to arguments of ``JSON_Format`` object to specify the additional params for DIF language parser on write action. At this moment we will only include the ``indent`` argument for `json parser <https://docs.python.org/3/library/json.html>`__, that will enable the pretty printing for output.

Creating Object
~~~~~~~~~~~~~~~~~~~~~~
Now we're moving to the main part - creating an object that will be used for further interaction with the local file.

.. code-block:: python
    :linenos:
    :lineno-start: 6

    config = JSON_Format(
        'settings.json',                          # Path to preferred local file location.
        def_dict,                                 # Default configuration dictionary that will
                                                  # be parsed into the local file on creation.
        parser_write_kwargs = parser_write_kwargs # Arguments, that will be passed to parser on write action
    )

If no exceptions were raised then everything is ready. Now, if you check the file on the path, that we specified in line ``3`` of step `Default values`_, you can see there's a ``json`` format dictionary built from our ``def_dict``.

.. code:: json

    {
        "version": 5,
        "app_name": "Test"
    }

.. note::
    If ``default_dictionary`` argument wasn't specified on object initialization then the local file still will be created. Its content will depend on how each language handles storing an empty dictionary. In our case, local file will look like this:

    .. code-block:: json

        {
        }

    .. versionadded:: 1.2.0
        You can also disable the automatic local file creation on object initialization by passing the keyword argument ``auto_file_creation=False`` to ``JSON_Format`` object.

Reading
~~~~~~~~~~~~~~~~~~~~~~
The local file and object are ready. Now we can access any value from this file. Let's try this out:

.. code-block:: python
    :linenos:
    :lineno-start: 11

    # Lets print the value of the key "version".
    # All keys can be directly accessed right from the object

    app_version = config["version"]                       # Getting the key 'version' from dictionary
    print("Application version: {}".format(app_version))  # Output should be:
                                                          # 'Application version: 5'

Creating and modifying
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Accessing the values is a good thing, but we're here not only for this, right? Next step we'll modify the value of one exising key and add the new key to object.

.. code-block:: python
    :linenos:
    :lineno-start: 17

    # Let's change the value of the key "app_name" to something new
    config["app_name"] = "Super Secret Tool"

    # And we'll also add the new key with dictionary value
    config["our_new_key"] = {
        "type": "msg",
        "id": 34724889325,
        "text": "wassup?"
    }

.. note::
    As you may already noticed, the way of interacting with ``serialix`` objects is quite same to dictionaries. That's right, ``serialix`` provides quick access to the bound dictionary keys and methods. This dictionary contains the parsed from local file keys and values and can be directly accessed through ``.dictionary`` object property:

    .. code:: python

        >>> config.dictionary
        {'version': 5,
         'app_name': 'Super Secret Tool',
         'our_new_key': {'type': 'msg', 'id': 34724889325, 'text': 'wassup?'}}

Removing
~~~~~~~~~~~~~~~~~~~~~~
Now lets try to remove one key from dictionary. To remove any key you can use the python's `del() <https://docs.python.org/3/tutorial/datastructures.html#the-del-statement>`__ statement.

.. code-block:: python
    :linenos:
    :lineno-start: 33

    # Let's delete the "text" key from our nested dictionary "our_new_key"
    del(config["our_new_key"]["text"])

Saving changes
~~~~~~~~~~~~~~~~~~~~~~
New key added, existing changed and even removed - but the local file still contains only the default values. It's not a bug, it's a feature. ``serialix`` will never automatically save any user-made changes to a local file without a direct command to do so. So let's send it.

.. code-block:: python
    :linenos:
    :lineno-start: 26

    # This method will commit all changes from object to local file
    config.commit()

Now our ``settings.json`` file will look like this:

.. code:: json

    {
        "version": 5,
        "app_name": "Super Secret Tool",
        "our_new_key": {
            "type": "msg",
            "id": 34724889325
        }
    }

Refreshing from file
~~~~~~~~~~~~~~~~~~~~~~
Now let's consider the situation that our local file (``settings.json``) was modified by some other application. ``serialix`` will never automatically refresh values of object, so you have to do it yourself.

Let's modify the ``settings.json`` file with any text editor and add the new key ``"custom_key"`` with value ``"hello?"``. Now our local file will look like this:

.. code:: json

    {
        "version": 5,
        "app_name": "Super Secret Tool",
        "our_new_key": {
            "type": "msg",
            "id": 34724889325
        },
        "custom_key": "hello?"
    }

To get this key inside of our ``config`` object we'll have to refresh it with special method:

.. code-block:: python
    :linenos:
    :lineno-start: 28

    # This method will refresh object's dictionary with dictionary parsed from the local file.
    config.refresh()

    # After refreshing, "custom_key" key will be added to object and can be accessed
    print(config["custom_key"])  # Output: 'hello?'

.. note::
    In some cases you should better use the ``.reload()`` method instead. Refreshing with ``.refresh()`` will save the changes that already made to object and add the new one from local file, but this feature is much slower than simply reloading the file. Therefore, if you are sure that no uncommitted changes have been made to the object, it is better to use the ``.reload()``.

Factory Reset
~~~~~~~~~~~~~~~~~~~~~~
If you are not happy with all the changes made and want to return everything to the default state, here's a method ``.reset_to_defaults()``` specially for you. This method will reset bound dictionary to values from ``def_dict`` variable that we specified at the beginning of this guide.

.. code-block:: python
    :linenos:
    :lineno-start: 40

    # Reset to bound dictionary to defaults
    config.reset_to_defaults()

    # And again, don't forget to commit the changes to local file
    config.commit()


Conclusion
---------------------

That's it, now you're ready for basic usage of ``serialix``. Public API of this package is fully documented with `docstrings <https://www.python.org/dev/peps/pep-0257/>`__, so you can get detailed information about any method, function, class, module or anything `here <serialix.html>`__
