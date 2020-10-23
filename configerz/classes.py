import json
from logging import getLogger

from .core import BaseConfigurationFile, Namespace


logger = getLogger(__name__)


class JSON_ConfigurationFile(BaseConfigurationFile):
    def write_to_file(self, config: dict):
        with open(self.configuration_file_path, 'wt') as f:
            json.dump(config, f, indent=4)
        logger.debug("Successful write to file action")

    def read_as_dict(self) -> dict:
        with open(self.configuration_file_path, 'rt') as f:
            config = json.load(f)

        return config

    def read_as_namespace(self) -> Namespace:
        with open(self.configuration_file_path, 'rt') as f:
            namespace = json.load(f, object_hook=lambda d: Namespace(**d))

        return namespace
