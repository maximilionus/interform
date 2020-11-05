from typing import Union
from logging import getLogger
from os import path, makedirs, remove


logger = getLogger(__name__)


class BaseConfiguration:
    def __init__(self, file_path: str, default_config: Union[str, dict], create_if_not_found=True):
        """Configuration object

        :param file_path: path to preferred configuration file destination
        If the file does not exist at the specified path, it will be created
        :type file_path: str
        :param default_config: default configuration file path `str` or dictionary
        that will be used by `create_file()` and `reset_file()` methods
        :type default_config: Union[str, dict]
        :param create_if_not_found: create all non-existent directories from provided
        in `file_path` path, defaults to True
        :type create_if_not_found: bool, optional
        :raises ValueError: If provided data type in argument `default_config` is not
        the path `str` or `dict`, this exception will be raised
        """
        self.__configuration_dict = {}

        self.configuration_file_path = file_path

        if isinstance(default_config, dict):
            self.__default_configuration = default_config
        elif path.isfile(default_config):
            self.__default_configuration = self._core__read_file_to_dict(default_config)
        else:
            raise ValueError("'default_config' argument should be a dictionary or a path to file string. Provided value is {0}"
                             .format(default_config))

        if create_if_not_found:
            if not path.exists(file_path):
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

    def __repr__(self):
        return self.__configuration_dict.__repr__()

    def clear(self):
        self.__configuration_dict.clear()

    def copy(self):
        return self.__configuration_dict.copy()

    def fromkeys(self, type, iterable, value):
        self.__configuration_dict.fromkeys(type, iterable, value)

    def get(self, key, default):
        return self.__configuration_dict.get(key, default)

    def items(self):
        return self.__configuration_dict.items()

    def keys(self):
        return self.__configuration_dict.keys()

    def values(self):
        return self.__default_configuration.values()

    def pop(self, k, d=None):
        self.__configuration_dict.pop(k, d)

    def popitem(self, k, d=None):
        self.__configuration_dict.popitem(k, d)

    def setdefault(self, key, default):
        self.__configuration_dict.setdefault(key, default)

    def update(self, d: dict):
        self.__configuration_dict.update(d)

    def refresh(self):
        """
        Refresh configuration file values from json.
        Note that user-added attributes will stay in object after refresh
        """
        self.__configuration_dict.update(self.read_file_as_dict())

    def reset_to_file(self):
        """Reset object's attributes to values from bound `confuration_object`"""
        self.clear()
        self.refresh()

    def commit(self):
        """Commit all changes from object to json configuration file"""
        self.write_dict_to_file(self.__configuration_dict)
        logger.debug("Successfully applied all object changes to local configuration file")

    def is_exist(self) -> bool:
        """Check configuration file existence

        :return: Does the file exist
        :rtype: bool
        """
        return True if path.isfile(self.configuration_file_path) else False

    def create_file(self) -> bool:
        """Create new configuration file from default dictionary

        :return: Was the file created successfully
        :rtype: bool
        """
        self.write_dict_to_file(self.__default_configuration)
        logger.info("Successfuly generated new configuration file")

        return True

    def delete_file(self):
        """Delete configuration file"""
        remove(self.configuration_file_path)

    def reset_file_to_defaults(self):
        """
        Reset configuration file to default values from `self.__default_configuration` var.
        Please note that object will not be reset after executing this method. To reset object dict -
        use `.reset_to_file()` method.
        """
        self.write_dict_to_file(self.__default_configuration)

    def write_dict_to_file(self, dictionary: dict):
        """Write dict from `dictionary` argument to configuration file bound to this object

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
        """Template for reading custom configuration files from path `str` as dictionary

        :param file_path: Path to configuration file
        :type file_path: str
        :return: Parsed configuration file dictionary
        :rtype: dict
        """
        pass

    @staticmethod
    def _core__write_dict_to_file(file_path: str, dictionary: dict):
        """Template for writing dictionaries into custom configuration path `str`

        :param file_path: Path to configuration file
        :type file_path: str
        :param dictionary: Dictionary which will be written in `file_path`
        :type dictionary: dict
        """
        pass


def create_directories(path_to_use: str, path_is_dir=False):
    """Create all directories from path

    :param path_to_use: The path to be created
    :type path_to_use: str
    :param path_is_dir: Is `path_to_use` ends with directory, defaults to False
    :type path_is_dir: bool, optional
    """
    path_to_use = path_to_use if path_is_dir else path.dirname(path_to_use)

    if not path.exists(path_to_use) and len(path_to_use) > 0:
        makedirs(path_to_use)
