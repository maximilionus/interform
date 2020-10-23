from os import path
from logging import getLogger


logger = getLogger(__name__)


class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update({kwargs})


class BaseConfigurationFile:
    """ Basic implementation of config file interaction layer """
    def __init__(self, file_path: str, create_if_not_found=True):
        self.configuration_file_path = file_path

        if create_if_not_found:
            # TODO: Create dirs and file
            pass

        self.refresh()

    def refresh(self):
        """ Refresh configuration file values from json """
        self.__dict__.update(**self.read_as_namespace().__dict__)

    def commit(self) -> bool:
        """ Commit all changes from object to json configuration file """
        def recursive_commit(dict_obj: dict, dict_file: dict) -> bool:
            """ Recursively commit all changes from object dict to configuration file

            Args:
                dict_obj (dict)
                dict_file (dict)

            Returns:
                bool: Was anything commited to `dict_file`
            """
            was_commited = False

            for key_file, value_file in dict_file.items():
                if type(value_file) == dict:
                    was_commited ^= recursive_commit(dict_obj[key_file], dict_file[key_file])

                elif value_file != dict_obj[key_file]:
                    dict_file[key_file] = dict_obj[key_file]
                    was_commited = True
                    logger.debug(f"Commited {key_file}:{value_file} to configuration file")

            return was_commited

        config_file_dict = self.read_as_dict()
        object_dict = namespace_to_dict(self)

        commit_result = recursive_commit(object_dict, config_file_dict)
        if commit_result:
            self.write_to_file(config_file_dict)
            logger.debug("Successfully applied all object changes to local configuration file")

        return commit_result

    def is_exist(self) -> bool:
        """ Check configuration file existence.

        Returns:
            bool:
                True - Config file exists.
                False - Config file doesn't exist.
        """
        return True if path.isfile(self.configuration_file_path) else False

    def create_file(self):
        """ Create new configuration file """
        self.write_to_file(self.config_file_dict)
        logger.info("Successfuly generated new configuration file")

    def write_to_file(self):
        pass

    def read_as_dict(self) -> dict:
        pass

    def read_as_namespace(self) -> object:
        pass


def namespace_to_dict(namespace_from: Namespace, dict_to={}) -> dict:
    for k, v in namespace_from.__dict__.items():
        if type(v) == Namespace:
            dict_to[k] = {}
            namespace_to_dict(v, dict_to[k])
        else:
            dict_to.update({k: v})

    return dict_to
