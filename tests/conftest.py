from configerz.core import create_directories

from . import core

core.change_path_to_testsdir()
create_directories(core.temp_dir_path)
