import unittest

from ..fixtures import create_json_config_object, remove_temp_dir


class TestJSONConfiguration(unittest.TestCase):
    def setUp(self):
        self.config_obj = create_json_config_object()

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

        file_dict = self.config_obj.read_file_as_dict()

        self.assertEqual(
            file_dict["Person_1"]["name"],
            person_name
        )
