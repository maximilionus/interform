import json
from logging import getLogger

from ..core import BaseConfiguration


logger = getLogger(__name__)


class JSON_Configuration(BaseConfiguration):
    @staticmethod
    def _core__read_file_to_dict(file_path: str) -> dict:
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
    def _core__write_dict_to_file(file_path: str, dictionary: dict):
        """Write dictionaries into custom configuration path `str`

        :param file_path: Path to configuration file
        :type file_path: str
        :param dictionary: Dictionary which will be written in `file_path`
        :type dictionary: dict
        """
        with open(file_path, 'wt') as f:
            json.dump(dictionary, f, indent=4)
        logger.debug("Successful write to file action")
