from typing import Any
from os import path, makedirs, remove


class BaseConfiguration:
    """Configuration object

    :param file_path: Path to preferred configuration file destination
        If the file does not exist at the specified path, it will be created
    :type file_path: str
    :param default_config: Default configuration file path ``str`` or dictionary
        that will be used by ``create_file()`` and ``reset_file()`` methods, defaults to {}
    :type default_config: Union[str, dict]
    :param force_overwrite_file: Should a file be overwritten if it already exists, defaults to False
    :type force_overwrite_file: bool, optional
    :raises ValueError: If provided data type in argument ``default_config`` is not
        the path ``str`` or ``dict``, this exception will be raised

    :note: Methods ``.clear()``, ``.copy()``, ``.fromkeys()``, ``.get()``, ``.items()``, ``.keys()``, ``values()``,
        ``pop()``, ``popitem()``, ``setdefault()``, ``update()`` are bound to the attribute ``dictionary``,
        so executing:

        >>> this_object.update({"check": True})

        Is equal to:

        >>> this_object.configuration.update({"check": True})
    """
    def __init__(self, file_path: str, default_config: {}, force_overwrite_file=False):
        self.__configuration_dict = {}

        self.configuration_file_path = file_path

        if isinstance(default_config, dict):
            self.__default_configuration_dict = default_config
        elif path.isfile(default_config):
            self.__default_configuration_dict = self._core__read_file_to_dict(default_config)
        else:
            raise ValueError("'default_config' argument should be a dictionary or a path to file string. Provided value is {0}"
                             .format(default_config))

        if not self.is_file_exist() or force_overwrite_file:
            create_directories(self.configuration_file_path)
            self.create_file()

        self.refresh()

    def __getitem__(self, key):
        return self.__configuration_dict[key]

    def __setitem__(self, key, value):
        self.__configuration_dict[key] = value

    def __delitem__(self, key):
        self.__configuration_dict.__delitem__(key)

    def __len__(self):
        return len(self.__configuration_dict)

    def clear(self):
        """ Clear the ``configuration`` dictionary """
        self.__configuration_dict.clear()

    def copy(self) -> dict:
        """Get the copy of ``configuration`` dictionary

        :return: ``configuration`` dictionary copy
        :rtype: dict
        """
        return self.__configuration_dict.copy()

    def get(self, key, default=None) -> Any:
        """Get key from ``configuration`` dictionary

        :param key: Key name
        :type key: str
        :param default: Default value, if key was not found
        :type default: Any
        :return: Value of requested ``key``, or ``default`` value
            if key wasn't found, defaults to None.
        :rtype: Any
        """
        return self.__configuration_dict.get(key, default)

    def items(self) -> list:
        """Get items of the ``configuration`` dictionary

        :return: Items of the ``configuration`` dictionary ((key, value) pairs)
        :rtype: list
        """
        return self.__configuration_dict.items()

    def keys(self) -> list:
        """Get keys of the ``configuration`` dictionary

        :return: Keys of the ``configuration`` dictionary (, key)
        :rtype: list
        """
        return self.__configuration_dict.keys()

    def values(self) -> list:
        """Get values of the ``configuration`` dictionary

        :return: Values of the ``configuration`` dictionary (, value)
        :rtype: list
        """
        return self.__default_configuration_dict.values()

    def pop(self, key: Any, default=None) -> Any:
        """Pop key from ``configuration`` dictionary

        :param key: Key name
        :type key: Any
        :param default: Default value, if key was not found, defaults to None
        :type default: Any, optional
        :return: Value of requested ``key``, or ``default`` value
            if key wasn't found, defaults to None.
        :rtype: Any
        """
        self.__configuration_dict.pop(key, default)

    def popitem(self) -> Any:
        """Pop item from ``configuration`` dictionary in LIFO order.

        :param key: Key name
        :type key: Any
        :param default: Default value, if key was not found, defaults to None
        :type default: Any, optional
        :return: Value of requested ``key``, or ``default`` value
            if key wasn't found, defaults to None.
        :rtype: Any
        """
        self.__configuration_dict.popitem()

    def setdefault(self, key: Any, default=None) -> Any:
        """
        If key is in the ``configuration`` dictionary, return its value.
        If not, insert key with a value of ``default`` and return ``default``

        :param key: Name of the key
        :type key: Any
        :param default: Default value, defaults to None
        :type default: Any, optional
        :return: If key is in the dictionary, return its value, else:
            returns ``defalut``
        :rtype: Any
        """
        self.__configuration_dict.setdefault(key, default)

    def update(self, dictionary: dict):
        """Update ``configuration`` dictionary with another dictionary

        :param dictionary: Dictionary, that will be merged to
            ``configuration`` dictionary
        :type dictionary: dict
        """
        self.__configuration_dict.update(dictionary)

    @property
    def dictionary(self) -> dict:
        """Full access to the configuration dictionary

        :return: Configuration dictionary
        :rtype: dict
        """
        return self.__configuration_dict

    @dictionary.setter
    def dictionary(self, dictionary: dict):
        self.__configuration_dict = dictionary

    @property
    def dictionary_default(self) -> dict:
        """Full access to the default configuration dictionary

        :return: Configuration dictionary
        :rtype: dict
        """
        return self.__default_configuration_dict

    @dictionary_default.setter
    def dictionary_default(self, dictionary: dict):
        self.__default_configuration_dict = dictionary

    def commit(self):
        """Commit all changes from ``dictionary`` to json configuration file"""
        self.write_dict_to_file(self.__configuration_dict)

    def refresh(self):
        """
        Refresh ``dictionary`` values from json.
        Note that user-added keys will stay in ``dictionary`` after refresh
        """
        self.__configuration_dict.update(self.read_file_as_dict())

    def reset_to_file(self):
        """Reset the ``dictionary`` attribute to values from bound ``confuration_object``"""
        self.clear()
        self.refresh()

    def reset_to_defaults(self):
        """
        Reset the `dictionary` attribute to values from ``dictionary_default`` attribute.
        Note that local configuration file will stay untouched.
        """
        self.__configuration_dict = self.__default_configuration_dict.copy()

    def create_file(self) -> bool:
        """Create new configuration file from default dictionary

        :return: Was the file created successfully
        :rtype: bool
        """
        self.write_dict_to_file(self.__default_configuration_dict)

        return True

    def delete_file(self) -> bool:
        """Delete local configuration file

        :return: Was the file removed.
            False will be returned only if the configuration file does not exist at the time of deletion.
        :rtype: bool
        """
        if self.is_file_exist():
            remove(self.configuration_file_path)
            return True
        else:
            return False

    def is_file_exist(self) -> bool:
        """Check configuration file existence

        :return: Does the file exist
        :rtype: bool
        """
        return True if path.isfile(self.configuration_file_path) else False

    def write_dict_to_file(self, dictionary: dict):
        """Write dict from ``dictionary`` argument to configuration file bound to this object

        :param config: Configuration dictionary
        :type config: dict
        """
        self._core__write_dict_to_file(self.configuration_file_path, dictionary)

    def read_file_as_dict(self) -> dict:
        """Read configuration file bound to this object as dictionary

        :return: Parsed configuration file
        :rtype: dict
        """
        return self._core__read_file_to_dict(self.configuration_file_path)

    @staticmethod
    def _core__read_file_to_dict(file_path: str) -> dict:
        """Template for reading custom configuration files from path ``str`` as dictionary

        :param file_path: Path to configuration file
        :type file_path: str
        :return: Parsed configuration file dictionary
        :rtype: dict
        """
        pass

    @staticmethod
    def _core__write_dict_to_file(file_path: str, dictionary: dict):
        """Template for writing dictionaries into custom configuration path ``str``

        :param file_path: Path to configuration file
        :type file_path: str
        :param dictionary: Dictionary which will be written in ``file_path``
        :type dictionary: dict
        """
        pass


def create_directories(path_to_use: str, path_is_dir=False):
    """Create all directories from path

    :param path_to_use: The path to be created
    :type path_to_use: str
    :param path_is_dir: Is ``path_to_use`` ends with directory, defaults to False
    :type path_is_dir: bool, optional
    """
    path_to_use = path_to_use if path_is_dir else path.dirname(path_to_use)

    if not path.exists(path_to_use) and len(path_to_use) > 0:
        makedirs(path_to_use)
