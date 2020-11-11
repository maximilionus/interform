from importlib.util import find_spec

from .meta import *
from .configs.json import JSON_Configuration
from .configs.ini import INI_Configuration


if find_spec('ruamel.yaml') is not None:
    from .configs.yaml import YAML_Configuration

if find_spec('xmltodict') is not None:
    from .configs.xml import XML_Configuration
