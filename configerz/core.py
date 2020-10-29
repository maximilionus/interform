from typing import Union
from logging import getLogger
from os import path, makedirs, remove


logger = getLogger(__name__)


class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update({**kwargs})


class BaseConfiguration:
    """ Basic implementation of config file interaction layer """
    def __init__(self, file_path: str, default_config: Union[str, dict], create_if_not_found=True):
        """Object initialization

        :param file_path: path to preferred configuration file destination.
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
        self.configuration_file_path = file_path

        if type(default_config) == dict:
            self.default_configuration = default_config
        elif path.isfile(default_config):
            self.default_configuration = self._read_file_to_dict(default_config)
        else:
            raise ValueError("'default_config' argument should be a dictionary or a path to file string. Provided value is {0}"
                             .format(type(default_config)))

        # On commit() method scan this vars will be ignored
        # By default it contains class-related variables
        self.__commit_exclude_vars = []
        self.__commit_exclude_vars.extend(list(self.__dict__))

        if create_if_not_found:
            create_directories(self.configuration_file_path)
            self.create_file()

        self.refresh()

    def refresh(self) -> bool:
        """Refresh configuration file values from json

        :return: refresh action status
        :rtype: bool
        """
        self.__dict__.update(**self.fread_namespace().__dict__)

        return True

    def commit(self, safe=True) -> bool:
        """ Commit all changes from object to json configuration file """
        # TODO: Object scan and fix should be here
        object_dict = namespace_to_dict(self, exclude_list=self.__commit_exclude_vars)
        self.fwrite_dict(object_dict)
        logger.debug("Successfully applied all object changes to local configuration file")

        return True

    def is_exist(self) -> bool:
        """Check configuration file existence

        :return: does the file exist
        :rtype: bool
        """
        return True if path.isfile(self.configuration_file_path) else False

    def create_file(self) -> bool:
        """Create new configuration file from default dictionary

        :return: was the file created successfully
        :rtype: bool
        """
        self.fwrite_dict(self.default_configuration)
        logger.info("Successfuly generated new configuration file")

        return True

    def delete_file(self) -> bool:
        """Delete configuration file

        :return: was the file removed successfully
        :rtype: bool
        """
        remove(self.configuration_file_path)

        return True

    def reset_file(self) -> bool:
        """
        Reset configuration file to default values from `self.default_configuration` var.
        Please note that object will not be reset after executing this method. To reset object -
        use `.refresh()` method.

        :return: was the file reset successfully
        :rtype: bool
        """
        self.fwrite_dict(self.default_configuration)

        return True

    def fwrite_dict(self, dictionary: dict):
        """Write dict from `dictionary` argument to configuration file bound to this object

        :param config: configuration dictionary
        :type config: dict
        """
        self._write_dict_to_file(self.configuration_file_path, dictionary)

    def fread_dict(self) -> dict:
        """Read configuration file bound to this object as dictionary

        :return: parsed configuration file
        :rtype: dict
        """
        return self._read_file_to_dict(self.configuration_file_path)

    def fread_namespace(self) -> Namespace:
        """Read the configuration file bound to this object as Namespace

        :return: namespace object with parsed configuration file
        :rtype: Namespace
        """
        return self._read_file_to_namespace(self.configuration_file_path)

    @staticmethod
    def _read_file_to_dict(file_path: str) -> dict:
        """Template for reading custom configuration files from path `str` as dictionary

        :param file_path: path to configuration file
        :type file_path: str
        :return: parsed configuration file dictionary
        :rtype: dict
        """
        pass

    @staticmethod
    def _read_file_to_namespace(file_path: str) -> Namespace:
        """Template for reading custom configuration files from path `str` as Namespace

        :param file_path: path to configuration file
        :type file_path: str
        :return: namespace object with parsed configuration file
        :rtype: Namespace
        """
        pass

    @staticmethod
    def _write_dict_to_file(file_path: str, dictionary: dict):
        """Template for writing dictionaries into custom configuration path `str`

        :param file_path: path to configuration file
        :type file_path: str
        :param dictionary: dictionary which will be written in `file_path`
        :type dictionary: dict
        """
        pass


def namespace_to_dict(namespace_from: Namespace, dict_to={}, exclude_list=[]) -> dict:
    """Recursively convert `Namespace` object to dictionary

    :param namespace_from: namespace object that will be converted
    :type namespace_from: Namespace
    :param dict_to: final dictionary variable, that will be used for
    recursive scan. No need to specify it, defaults to {}
    :type dict_to: dict, optional
    :param exclude_list: contains `str`'s with names of attributes, that will be excluded
    from `dict_to` on scan. This argument is used to exclude private and public
    class-related attributes and leave only configuration file related attributes in `dict_to`, defaults to []
    :type exclude_list: list, optional
    :return: dictionary with all keys and values from `namespace_from` object
    :rtype: dict
    """
    for k, v in namespace_from.__dict__.items():
        if type(v) == Namespace:
            dict_to[k] = {}
            namespace_to_dict(v, dict_to[k], exclude_list)
        elif k in exclude_list:
            continue
        else:
            dict_to.update({k: v})

    return dict_to


def create_directories(path_to_use: str, path_is_dir=False):
    """ Create all directories from path

    :param path_to_use: the path to be created
    :type path_to_use: str
    :param path_is_dir: is `path_to_use` ends with directory, defaults to False
    :type path_is_dir: bool, optional
    """
    path_to_use = path_to_use if path_is_dir else path.dirname(path_to_use)

    if not path.exists(path_to_use) and len(path_to_use) > 0:
        makedirs(path_to_use)
