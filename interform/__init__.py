"""
Here is the main initialization code that makes
it easier to access the main features of the
other submodules and subpackages
"""
from importlib.util import find_spec as __find_spec

from .meta import *
from .langs.json import JSON_Format
from .langs.ini import INI_Format

if __find_spec('ruamel.yaml') is not None:
    from .langs.yaml import YAML_Format

if __find_spec('xmltodict') is not None:
    from .langs.xml import XML_Format
