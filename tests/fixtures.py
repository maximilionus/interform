from os import path
from shutil import rmtree

from configerz import JSON_Configuration


temp_dir_path = './temp/'
configuration_file_path = path.join(temp_dir_path, 'test_config.json')
default_configuration = {
    "Person_1": {
        "name": "X",
        "age": 256
    },
    "TestKey": "Yes"
}


def remove_temp_dir():
    if path.isdir(temp_dir_path):
        rmtree(temp_dir_path)


def create_json_config_object() -> object:
    return JSON_Configuration(configuration_file_path, default_configuration, True)
