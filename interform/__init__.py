"""
Here is the main initialization code that makes
it easier to access the main features of the
other submodules and subpackages
"""
from importlib.util import find_spec as __find_spec

from .meta import *
from .langs.json import JSON_Format

try:
    __find_spec('ruamel.yaml')
except Exception:
    pass
else:
    from .langs.yaml import YAML_Format
