from configerz import JSON_Configuration

from ..fixtures import BaseConfigTest, configuration_file_path,\
    default_configuration_dict, default_cfg_json_path


class Test_Create_1(BaseConfigTest):
    """
    Create configuration file on temp path
    and read values from `default_configuration_dict`
    """
    def setUp(self):
        self.config_obj = JSON_Configuration(
            configuration_file_path,
            default_configuration_dict,
            True
        )


class Test_Create_2(BaseConfigTest):
    """
    Create configuration file on temp path
    and read values from file on `default_cfg_json_path`
    """
    def setUp(self):
        self.config_obj = JSON_Configuration(
            configuration_file_path,
            default_cfg_json_path,
            True
        )
