"""
``INI`` language support.

Work in progress.
"""
from configparser import ConfigParser

from ..core import BaseLang


class INI_Format(BaseLang):
    # TODO

    def __dict_from_ini(self, ini_obj) -> dict:
        # TODO: Needs to be tested
        parser = ConfigParser()
        parser.read(self.__parsed_file)

        return {section: dict(parser.items(section)) for section in parser.sections()}
