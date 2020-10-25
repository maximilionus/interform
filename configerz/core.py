from os import path, makedirs, remove
from logging import getLogger


logger = getLogger(__name__)


class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update({**kwargs})


class BaseConfiguration:
    """ Basic implementation of config file interaction layer """
    def __init__(self, file_path: str, default_config: {}, create_if_not_found=True):
        self.configuration_file_path = file_path

        if type(default_config) == dict:
            self.default_configuration = default_config
        elif path.isfile(default_config):
            self.default_configuration = self.read_custom_file_as_dict(default_config)
        else:
            raise TypeError(f"'default_config' argument type should be a dictionary or an existing path to file. Passed argument type is: {type(default_config)}")

        # On commit() method scan this vars will be ignored
        # By default it contains class-related variables
        self.__commit_exclude_vars = []
        self.__commit_exclude_vars.extend(list(self.__dict__))

        if create_if_not_found:
            create_directories(self.configuration_file_path)
            self.create_file()

        self.refresh()

    def refresh(self) -> bool:
        """ Refresh configuration file values from json """
        self.__dict__.update(**self.read_file_as_namespace().__dict__)

        return True

    def commit(self) -> bool:
        """ Commit all changes from object to json configuration file """
        object_dict = namespace_to_dict(self, exclude_list=self.__commit_exclude_vars)
        self.write_to_file(object_dict)
        logger.debug("Successfully applied all object changes to local configuration file")

        return True

    def is_exist(self) -> bool:
        """ Check configuration file existence.

        Returns:
            bool: Does the file exist
        """
        return True if path.isfile(self.configuration_file_path) else False

    def create_file(self) -> bool:
        """ Create new configuration file from default dictionary """
        self.write_to_file(self.default_configuration)
        logger.info("Successfuly generated new configuration file")

        return True

    def delete_file(self) -> bool:
        """ Delete configuration file

        Returns:
            bool: True on successful file removal
        """
        remove(self.configuration_file_path)

        return True

    def reset_file(self) -> bool:
        """
        Reset configuration file to default values from `self.default_configuration` var.
        Please note that object will not be reset after executing this method. To reset object -
        use `.refresh()` method.

        Returns:
            bool: True on successful file reset
        """
        self.write_to_file(self.default_configuration)

        return True

    def write_to_file(self, config: dict):
        """ Template for write to config file method """
        pass

    def read_file_as_dict(self) -> dict:
        """ Template for reading configuration file as dictionary

        Returns:
            dict: Parsed configuration
        """
        pass

    def read_file_as_namespace(self) -> Namespace:
        """ Template for reading configuration file as Namespace object

        Returns:
            Namespace: Parsed configuration
        """
        pass

    @staticmethod
    def read_custom_file_as_dict(file_path: str) -> dict:
        """ Template for reading custom configuration files from path as dictionary

        :param file_path: path to configuration file
        :type file_path: str
        :return: parsed configuration file dictionary
        :rtype: dict
        """
        pass


def namespace_to_dict(namespace_from: Namespace, dict_to={}, exclude_list=[]) -> dict:
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

    if not path.exists(path_to_use):
        makedirs(path_to_use)
