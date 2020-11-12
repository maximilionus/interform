from configparser import ConfigParser

from ..core import BaseInterchange


class INI_Format(BaseInterchange):
    # TODO

    def __dict_from_ini(self, config_parser) -> dict:
        # TODO: Needs to be tested
        parser = ConfigParser()
        parser.read(self.__parsed_file)

        return {section: dict(parser.items(section)) for section in parser.sections()}
