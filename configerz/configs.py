import json
from logging import getLogger
from configparser import ConfigParser

from .core import BaseConfiguration, Namespace


logger = getLogger(__name__)


class JSON_Configuration(BaseConfiguration):
    @staticmethod
    def _read_file_to_dict(file_path: str) -> dict:
        with open(file_path, 'rt') as f:
            config_dict = json.load(f)

        return config_dict

    @staticmethod
    def _read_file_to_namespace(file_path: str) -> Namespace:
        with open(file_path, 'rt') as f:
            namespace = json.load(f, object_hook=lambda d: Namespace(**d))

        return namespace

    @staticmethod
    def _write_dict_to_file(file_path: str, dictionary: dict):
        with open(file_path, 'wt') as f:
            json.dump(dictionary, f, indent=4)
        logger.debug("Successful write to file action")


class INI_Configuration(BaseConfiguration):
    # TODO
    def __dict_from_ini(self, config_parser) -> dict:
        # TODO: Needs to be tested
        parser = ConfigParser()
        parser.read(self.configuration_file_path)

        return {section: dict(parser.items(section)) for section in parser.sections()}
