import pytest

from configurio.core import create_directories

from . import core


core.change_path_to_testsdir()


@pytest.fixture(scope="class", autouse=True)
def dir_control():
    create_directories(core.temp_dir_path)
    yield "class"
    core.remove_temp_dir()
