import unittest
from os import path
from shutil import rmtree

from configerz import JSON_Configuration


class TestJSONConfiguration(unittest.TestCase):
    def setUp(self):
        self.temp_dir_path = './temp/'
        self.configuration_file_path = path.join(self.temp_dir_path, 'test_config.json')
        self.default_configuration = {
            "Person_1": {
                "name": "X",
                "age": 256
            },
            "TestKey": "Yes"
        }

        self.config_obj = JSON_Configuration(self.configuration_file_path, self.default_configuration, True)

    def tearDown(self):
        if path.isdir(self.temp_dir_path):
            rmtree(self.temp_dir_path)

    def test_delete_file(self):
        result = self.config_obj.delete_file()
        self.assertEqual(result, True)

    def test_create_file(self):
        result = self.config_obj.create_file()
        self.assertEqual(result, True)

    def test_modify_and_commit(self):
        person_name = "Jeff"

        self.config_obj.Person_1.name = person_name
        self.config_obj.commit()

        file_dict = self.config_obj.read_file_as_dict()

        self.assertEqual(
            file_dict["Person_1"]["name"],
            person_name
        )
