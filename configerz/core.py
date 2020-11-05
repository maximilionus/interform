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
        return self.__configuration_dict.__len__()

    @property
    def dictionary(self) -> dict:
        return self.__configuration_dict

    def refresh(self) -> bool:
        """
        Refresh configuration file values from json.
        Note that user-added attributes will stay in object after refresh

        :return: Refresh action status
        :rtype: bool
        """
        self.__configuration_dict.update(self.read_file_as_dict())

        return True

    def clear(self) -> bool:
        """Remove all attributes from bound `confuration_object`

        :return: Status of clear action
        :rtype: bool
        """
        for k in list(self.__configuration_dict.keys()):
            del(self.__configuration_dict.__dict__[k])

        return True

    def reset_to_file(self) -> bool:
        """Reset object's attributes to values from bound `confuration_object`

        :return: Status of reset action
        :rtype: bool
        """
        self.clear()
        self.refresh()

        return True

    def reset_to_defaults(self) -> bool:
        # TODO
        pass

    def commit(self) -> bool:
        """Commit all changes from object to json configuration file

        :return: Was the changes committed
        :rtype: bool
        """
        self.write_dict_to_file(self.__configuration_dict)
        logger.debug("Successfully applied all object changes to local configuration file")

        return True

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

    def delete_file(self) -> bool:
        """Delete configuration file

        :return: Was the file removed successfully
        :rtype: bool
        """
        remove(self.configuration_file_path)

        return True

    def reset_file_to_defaults(self) -> bool:
        """
        Reset configuration file to default values from `self.__default_configuration` var.
        Please note that object will not be reset after executing this method. To reset object -
        use `.reset()` method.

        :return: Was the file reset successfully
        :rtype: bool
        """
        self.write_dict_to_file(self.__default_configuration)

        return True

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
