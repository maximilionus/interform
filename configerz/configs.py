import json
from logging import getLogger
from configparser import ConfigParser

from .core import BaseController, Namespace

try:
    import yaml
except ImportError:
    yaml = None

logger = getLogger(__name__)


class Configuration(Namespace):
    """ Configuration main object """
    pass


class JSON_Controller(BaseController):
    @staticmethod
    def _read_file_to_dict(file_path: str) -> dict:
        """Read custom configuration files from path `str` as json dictionary

        :param file_path: Path to configuration file
        :type file_path: str
        :return: Parsed configuration file dictionary
        :rtype: dict
        """
        with open(file_path, 'rt') as f:
            config_dict = json.load(f)

        return config_dict

    @staticmethod
    def _read_file_to_namespace(file_path: str) -> Namespace:
        """Read custom configuration files from path `str` as Namespace

        :param file_path: Path to configuration file
        :type file_path: str
        :return: Namespace object with parsed configuration file
        :rtype: Namespace
        """
        with open(file_path, 'rt') as f:
            namespace = json.load(f, object_hook=lambda d: Namespace(**d))

        return namespace

    @staticmethod
    def _write_dict_to_file(file_path: str, dictionary: dict):
        """Write dictionaries into custom configuration path `str`

        :param file_path: Path to configuration file
        :type file_path: str
        :param dictionary: Dictionary which will be written in `file_path`
        :type dictionary: dict
        """
        with open(file_path, 'wt') as f:
            json.dump(dictionary, f, indent=4)
        logger.debug("Successful write to file action")


class INI_Controller(BaseController):
    # TODO
    def __dict_from_ini(self, config_parser) -> dict:
        # TODO: Needs to be tested
        parser = ConfigParser()
        parser.read(self.configuration_file_path)

        return {section: dict(parser.items(section)) for section in parser.sections()}


if yaml is not None:

    class YAML_Controller(BaseController):
        pass
