from configparser import ConfigParser

import pytest

from interform import INI_Format

from .core import BaseLangTest, local_file_path,\
    default_local_file_dict, default_cfg_path


@pytest.mark.ini
class Test_Create_DefDict(BaseLangTest):
    """
    Create local file on `local_file_path`
    and get default config values from `default_local_file_dict`
    """
    def setup(self):
        self.language_object = INI_Format(
            local_file_path,
            default_local_file_dict
        )


@pytest.mark.ini
class Test_Create_DefPath(BaseLangTest):
    """
    Read existing file on `local_file_path`
    and get default config values from file on `default_cfg_path`
    """
    def setup(self):
        ini_parser = ConfigParser()
        ini_parser.read_dict(default_local_file_dict)

        with open(default_cfg_path, 'w') as f:
            ini_parser.write(f)

        self.language_object = INI_Format(
            local_file_path,
            default_cfg_path
        )
