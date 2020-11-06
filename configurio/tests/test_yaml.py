import pytest
from ruamel.yaml import YAML

from configurio import YAML_Configuration

from .core import BaseConfigTest, configuration_file_path,\
    default_configuration_dict, default_cfg_json_path


yaml = YAML()


@pytest.mark.yaml
class Test_Create_DefDict(BaseConfigTest):
    """
    Create configuration file on `configuration_file_path`
    and get default config values from `default_configuration_dict`
    """
    def setup(self):
        self.config = YAML_Configuration(
            configuration_file_path,
            default_configuration_dict
        )


@pytest.mark.yaml
class Test_Create_DefPath(BaseConfigTest):
    """
    Read existing file on `configuration_file_path`
    and get default config values from file on `default_cfg_json_path`
    """
    def setup(self):
        with open(default_cfg_json_path, 'w') as f:
            yaml.dump(default_configuration_dict, f)

        self.config = YAML_Configuration(
            configuration_file_path,
            default_cfg_json_path
        )
