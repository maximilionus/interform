import json

import pytest

from configurio import JSON_Configuration

from .core import BaseConfigTest, configuration_file_path,\
    default_configuration_dict, default_cfg_path


@pytest.mark.json
class Test_Create_DefDict(BaseConfigTest):
    """
    Create configuration file on `configuration_file_path`
    and get default config values from `default_configuration_dict`
    """
    def setup(self):
        self.config = JSON_Configuration(
            configuration_file_path,
            default_configuration_dict
        )


@pytest.mark.json
class Test_Create_DefPath(BaseConfigTest):
    """
    Read existing file on `configuration_file_path`
    and get default config values from file on `default_cfg_path`
    """
    def setup(self):
        with open(default_cfg_path, 'w') as f:
            json.dump(default_configuration_dict, f)

        self.config = JSON_Configuration(
            configuration_file_path,
            default_cfg_path
        )
