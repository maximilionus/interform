from configparser import ConfigParser

from ..core import BaseConfiguration


class INI_Configuration(BaseConfiguration):
    # TODO
    def __dict_from_ini(self, config_parser) -> dict:
        # TODO: Needs to be tested
        parser = ConfigParser()
        parser.read(self.configuration_file_path)

        return {section: dict(parser.items(section)) for section in parser.sections()}
