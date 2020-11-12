from importlib.util import find_spec

from .meta import *
from .configs.json import JSON_Format
from .configs.ini import INI_Format


if find_spec('ruamel.yaml') is not None:
    from .configs.yaml import YAML_Format

if find_spec('xmltodict') is not None:
    from .configs.xml import XML_Format
