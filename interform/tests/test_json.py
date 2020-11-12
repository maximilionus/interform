import json

import pytest

from interform import JSON_Format

from .core import BaseConfigTest, local_file_path,\
    default_local_file_dict, default_cfg_path


@pytest.mark.json
class Test_Create_DefDict(BaseConfigTest):
    """
    Create local file on `local_file_path`
    and get default config values from `default_local_file_dict`
    """
    def setup(self):
        self.config = JSON_Format(
            local_file_path,
            default_local_file_dict
        )


@pytest.mark.json
class Test_Create_DefPath(BaseConfigTest):
    """
    Read existing file on `local_file_path`
    and get default config values from file on `default_cfg_path`
    """
    def setup(self):
        with open(default_cfg_path, 'w') as f:
            json.dump(default_local_file_dict, f)

        self.config = JSON_Format(
            local_file_path,
            default_cfg_path
        )
