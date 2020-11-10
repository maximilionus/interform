from ..core import BaseConfiguration

try:
    import ujson as json
except ImportError:
    import json


class JSON_Configuration(BaseConfiguration):
    """Configuration object

    :param file_path: Path to preferred configuration file destination
        If the file does not exist at the specified path, it will be created
    :type file_path: str
    :param default_config: Default configuration file path ``str`` or ``dict``
        that will be used for local file start values and , defaults to {}
    :type default_config: Union[str, dict], optional
    :param force_overwrite_file: Whether the file needs to be overwritten if it already exists, defaults to False
    :type force_overwrite_file: bool, optional
    :raises ValueError: If provided data type in argument ``default_config`` is not
        the path ``str`` or ``dict``, this exception will be raised

    .. note::
        Methods ``.clear()``, ``.copy()``, ``.fromkeys()``, ``.get()``, ``.items()``, ``.keys()``, ``values()``,
        ``pop()``, ``popitem()``, ``setdefault()``, ``update()`` are bound to the attribute ``dictionary``,
        so executing:

        >>> this_object.update({"check": True})

        Is equal to:

        >>> this_object.configuration.update({"check": True})
    """
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
        """Write dictionary into custom configuration path `str`

        :param file_path: Path to configuration file
        :type file_path: str
        :param dictionary: Dictionary which will be written in `file_path`
        :type dictionary: dict
        """
        with open(file_path, 'wt') as f:
            json.dump(dictionary, f, indent=4)
