from shutil import rmtree
from os import path, chdir


temp_dir_path = './temp/'

configuration_file_path = path.join(temp_dir_path, 'test_config.txt')
default_cfg_json_path = path.join(temp_dir_path, 'default_config.json')

default_configuration_dict = {
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
    chdir(path.dirname(__file__))


class BaseConfigTest():
    """
    Base class for all configuration file tests.
    `setup_method()` method should be overwritten with valid config object initialization.
    """
    def setup(self):
        self.config = None
        self.controller = None

    def test_delete_file(self):
        assert self.controller.delete_file()

    def test_create_file(self):
        assert self.controller.create_file()

    # TODO: read_file and write_file

    def test_modify_file(self):
        person_name = "Jeff"
        self.config.Person_1.name = person_name
        self.controller.commit()

        read_dict = self.controller.fread_dict()

        assert read_dict["Person_1"]["name"] == person_name

    def test_reset_file(self):
        self.controller.reset_file()

        assert self.controller.fread_dict()["Person_1"]["name"] == default_configuration_dict["Person_1"]["name"]

    def test_clear_object(self):
        self.controller.clear()

        assert len(vars(self.config)) == 0

    def test_refresh_object(self):
        self.controller.refresh()

        assert len(vars(self.config)) > 0

    def test_add_one_key(self):
        key_name = "Masvingo"

        self.config.city = key_name
        self.controller.commit()

        assert self.config.city == self.controller.fread_dict()["city"]

    def test_add_nested_dicts(self):
        dct = {
            "sugar": {
                "carbon": 12,
            }
        }

        self.config.items = dct
        self.controller.commit()

        assert self.config.items.sugar.carbon == self.controller.fread_dict()["items"]["sugar"]["carbon"]

    def test_add_multiple_dicts(self):
        dct = {
            "jerre_1829": {
                "status": 1
            },
            "wolfrm4882": {
                "status": 2
            }
        }

        self.config.users = dct
        self.controller.commit()

        file_dict = self.controller.fread_dict()["users"]

        assert self.config.users.jerre_1829.status == file_dict["jerre_1829"]["status"] and \
               self.config.users.wolfrm4882.status == file_dict["wolfrm4882"]["status"]
