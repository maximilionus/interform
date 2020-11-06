from ruamel.yaml import YAML

from ..core import BaseConfiguration


yaml = YAML()


class YAML_Configuration(BaseConfiguration):
    @staticmethod
    def _core__read_file_to_dict(file_path: str) -> dict:
        """Read custom configuration files from path `str` as dictionary

        :param file_path: Path to configuration file
        :type file_path: str
        :return: Parsed configuration file dictionary
        :rtype: dict
        """
        with open(file_path, 'rt') as f:
            config_dict = yaml.load(f)

        return config_dict

    @staticmethod
    def _core__write_dict_to_file(file_path: str, dictionary: dict):
        """Write dictionary into custom configuration path `str`

        :param file_path: Path to configuration file
        :type file_path: str
        :param dictionary: Dictionary which will be written in `file_path`
        :type dictionary: dict
        """
        with open(file_path, 'wt') as f:
            yaml.dump(dictionary, f)
