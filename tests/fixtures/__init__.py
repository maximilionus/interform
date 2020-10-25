from os import path, chdir
from shutil import rmtree


temp_dir_path = './temp/'
configuration_file_path = path.join(temp_dir_path, 'test_config.json')
default_configuration_file_path = "./fixtures/files/default_configuration.json"

default_configuration = {
    "Person_1": {
        "name": "X",
        "age": 256
    },
    "case_415": {
        "path": "~/xxx/xxx/xxx",
        "utime": 1603645369,
        "description": "He was lying on the floor in tears with a keyboard in his hand. "
                       "The light of the monitor illuminated the whole sad sight. "
                       "He was just trying to write unit tests."
    },
    "TestKey": "Yes"
}


def remove_temp_dir():
    if path.isdir(temp_dir_path):
        rmtree(temp_dir_path)


def change_path_to_testsdir():
    """ Change working directory to `/tests/` """
    chdir(path.dirname(path.dirname(__file__)))
