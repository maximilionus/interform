import json
from logging import getLogger
from configparser import ConfigParser

from .core import BaseConfiguration, Namespace


logger = getLogger(__name__)


class JSON_Configuration(BaseConfiguration):
    def write_to_file(self, config: dict):
        with open(self.configuration_file_path, 'wt') as f:
            json.dump(config, f, indent=4)
        logger.debug("Successful write to file action")

    def read_file_as_dict(self) -> dict:
        with open(self.configuration_file_path, 'rt') as f:
            config = json.load(f)

        return config

    def read_file_as_namespace(self) -> Namespace:
        with open(self.configuration_file_path, 'rt') as f:
            namespace = json.load(f, object_hook=lambda d: Namespace(**d))

        return namespace


class INI_Configuration(BaseConfiguration):
    def write_to_file(self, config: dict):
        pass

    def read_file_as_dict(self) -> dict:
        pass

    def read_file_as_namespace(self) -> dict:
        pass

    def __dict_from_ini(self, config_parser) -> dict:
        # TODO: Needs to be tested
        parser = ConfigParser()
        parser.read(self.configuration_file_path)

        return {section: dict(parser.items(section)) for section in parser.sections()}
