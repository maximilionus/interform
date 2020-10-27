from shutil import rmtree
from os import path, chdir
from unittest import TestCase


temp_dir_path = './temp/'
configuration_file_path = path.join(temp_dir_path, 'test_config.txt')
default_configuration_file_path = "./fixtures/files/default_configuration.txt"

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


class BaseConfigTest(TestCase):
    """
    Base class for all configuration file tests.
    `setUp()` method should be overwritten with valid config object initialization.
    """
    def setUp(self):
        self.config_obj = None  # Should be changed in real test

    def tearDown(self):
        remove_temp_dir()

    def test_delete_file(self):
        result = self.config_obj.delete_file()
        self.assertEqual(result, True)

    def test_create_file(self):
        result = self.config_obj.create_file()
        self.assertEqual(result, True)

    def test_modify_commit_read(self):
        person_name = "Jeff"

        self.config_obj.Person_1.name = person_name
        self.config_obj.commit()

        file_dict = self.config_obj.fread_dict()

        self.assertEqual(
            file_dict["Person_1"]["name"],
            person_name
        )
