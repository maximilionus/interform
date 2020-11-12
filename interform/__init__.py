from importlib.util import find_spec

from .meta import *
from .langs.json import JSON_Format
from .langs.ini import INI_Format


if find_spec('ruamel.yaml') is not None:
    from .langs.yaml import YAML_Format

if find_spec('xmltodict') is not None:
    from .langs.xml import XML_Format
