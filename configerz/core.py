from typing import Union
from logging import getLogger
from os import path, makedirs, remove


logger = getLogger(__name__)


class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update({**kwargs})

    def __setattr__(self, name, value):
        if isinstance(value, dict):
            # Convert dict to namespace
            value = dict_to_namespace(value)

        super().__setattr__(name, value)

    def __getattr__(self, key):
        if key not in vars(self):
            # Create nested attributes
            setattr(self, key, {})

        return super().__getattribute__(key)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)


class Configuration(Namespace):
    """ Configuration main object """
    pass


class BaseController:
    def __init__(self, confuration_object: object, file_path: str, default_config: Union[str, dict], create_if_not_found=True):
        """Controller class. Controllers contains realisation of all methods that are
        used to work with configuration objects: apply changes, refresh, reset, create, eg.

        :param confuration_object: `Configuration` class object, that this controller
        will use for further actions
        :type confuration_object: object
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
        self.__confuration_object = confuration_object
        self.configuration_file_path = file_path

        if isinstance(default_config, dict):
            self.__default_configuration = default_config
        elif path.isfile(default_config):
            self.__default_configuration = self._core__read_file_to_dict(default_config)
        else:
            raise ValueError("'default_config' argument should be a dictionary or a path to file string. Provided value is {0}"
                             .format(default_config))

        if create_if_not_found:
            create_directories(self.configuration_file_path)
            self.create_file()

        self.refresh()

    def refresh(self) -> bool:
        """
        Refresh configuration file values from json.
        Note that user-added attributes will stay in object after refresh

        :return: Refresh action status
        :rtype: bool
        """
        self.__confuration_object.__dict__.update(**self.read_file_as_namespace().__dict__)

        return True

    def clear(self) -> bool:
        """Remove all attributes from bound `confuration_object`

        :return: Status of clear action
        :rtype: bool
        """
        for k in list(self.__confuration_object.__dict__.keys()):
            del(self.__confuration_object.__dict__[k])

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
        object_dict = namespace_to_dict(self.__confuration_object)
        self.write_dict_to_file(object_dict)
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

    def read_file_as_namespace(self) -> Namespace:
        """Read the configuration file bound to this object as Namespace

        :return: Namespace object with parsed configuration file
        :rtype: Namespace
        """
        return self._core__read_file_to_namespace(self.configuration_file_path)

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
    def _core__read_file_to_namespace(file_path: str) -> Namespace:
        """Template for reading custom configuration files from path `str` as Namespace

        :param file_path: Path to configuration file
        :type file_path: str
        :return: Namespace object with parsed configuration file
        :rtype: Namespace
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


def namespace_to_dict(namespace_from: Namespace, dict_to={}) -> dict:
    """Recursively convert `Namespace` object to dictionary

    :param namespace_from: `Namespace` object that will be converted
    :type namespace_from: Namespace
    :param dict_to: Final dictionary variable, that will be used for
        recursive scan. No need to specify it, defaults to {}
    :type dict_to: dict, optional
    :return: Dictionary with all keys and values from `namespace_from` object
    :rtype: dict
    """
    for k, v in vars(namespace_from).items():
        if isinstance(v, Namespace):
            dict_to[k] = {}
            namespace_to_dict(v, dict_to[k])
        else:
            dict_to.update({k: v})

    return dict_to


def dict_to_namespace(dict_from: dict, namespace_to=Namespace()) -> Namespace:
    """Recursively convert any dictionary to `Namespace` object

    :param dict_from: Dictionary, that needs to be converted
    :type dict_from: dict
    :param namespace_to: Optional argument, used by this function recursive calls to itself.
        No need to specify it, defaults to Namespace()
    :type namespace_to: Namespace, optional
    :return: `Namespace` object with all dict_from values,
        accessible as object's attributes
    :rtype: Namespace
    """
    namespace_to_dict = vars(namespace_to) if isinstance(namespace_to, Namespace) else namespace_to

    for k, v in dict_from.items():
        if isinstance(v, dict):
            namespace_to_dict[k] = Namespace()
            dict_to_namespace(v, namespace_to_dict[k])
        else:
            namespace_to_dict.update({k: v})

    return namespace_to


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


def getkey(configuration_object: Configuration, key_name: str, default=None) -> Union[str, Namespace]:
    """Safely extract key from configuration object

    :param configuration_object: `Configuration` class object to read values from
    :type configuration_object: Configuration
    :param key_name: Name of the key that function will search for in `configuration_object`
    :type key_name: str
    :param default: If key doesn't exist in `configuration_object` - return value will be replaced
        with this argument, defaults to None
    :type default: Any, optional
    :return: Return the value of `key_name` in `configuration_object` or `default` if `key_name` was
        not found in `configuration_object`
    :rtype: Union[str, Namespace]
    """
    return vars(configuration_object).get(key_name, default)
