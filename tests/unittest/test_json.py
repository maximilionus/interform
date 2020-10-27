from configerz import JSON_Configuration

from ..fixtures import BaseConfigTest, configuration_file_path,\
    default_configuration, default_configuration_file_path


class Test_DefaultFromDict(BaseConfigTest):
    def setUp(self):
        self.config_obj = JSON_Configuration(
            configuration_file_path,
            default_configuration,
            True
        )


class Test_DefaultFromFile(BaseConfigTest):
    def setUp(self):
        self.config_obj = JSON_Configuration(
            configuration_file_path,
            default_configuration_file_path,
            True
        )
