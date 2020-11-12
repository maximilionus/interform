from ruamel.yaml import YAML

from ..core import BaseInterchange


yaml = YAML()


class YAML_Format(BaseInterchange):
    """YAML Data Interchange Format (DIF) realisation

    :param file_path: Path to preferred local file destination
        If the file does not exist at the specified path, it will be created
    :type file_path: str
    :param default_dictionary: Default local file path ``str`` or ``dict``
        that will be used for local file start values and , defaults to {}
    :type default_dictionary: Union[str, dict], optional
    :param force_overwrite_file: Whether the file needs to be overwritten if it already exists, defaults to False
    :type force_overwrite_file: bool, optional
    :raises ValueError: If provided data type in argument ``default_dictionary`` is not
        the path ``str`` or ``dict``, this exception will be raised

    .. note::
        Methods ``.clear()``, ``.copy()``, ``.fromkeys()``, ``.get()``, ``.items()``, ``.keys()``, ``values()``,
        ``pop()``, ``popitem()``, ``setdefault()``, ``update()`` are bound to the attribute ``dictionary``,
        so executing:

        >>> this_object.update({"check": True})

        Is equal to:

        >>> this_object.dictionary.update({"check": True})
    """
    @staticmethod
    def _core__read_file_to_dict(file_path: str) -> dict:
        """Method for reading custom local files from path ``str`` as dictionary

        :param file_path: Path to local file in ``yaml`` format
        :type file_path: str
        :return: Parsed local file dictionary
        :rtype: dict
        """
        with open(file_path, 'rt') as f:
            config_dict = yaml.load(f)

        return config_dict

    @staticmethod
    def _core__write_dict_to_file(file_path: str, dictionary: dict):
        """Method to write dictionaries into custom local path ``str``

        :param file_path: Path to local file in ``yaml`` format
        :type file_path: str
        :param dictionary: Dictionary which will be written in ``file_path``
        :type dictionary: dict
        """
        with open(file_path, 'wt') as f:
            yaml.dump(dictionary, f)
