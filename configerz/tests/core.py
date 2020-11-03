from shutil import rmtree
from os import path, chdir

import pytest

from configerz.core import Configuration
from configerz.core import BaseController


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
    "TestKey": "Yes",
    "dash-split": {
        "wow-man": "yeah, cool"
    }
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
        self.config = Configuration()
        self.controller = BaseController()

    def test_delete_file(self):
        """ Delete local configuration file """
        assert self.controller.delete_file()

    def test_create_file(self):
        """ Create local configuration file """
        assert self.controller.create_file()

    def test_file_read(self):
        # TODO
        pytest.skip("Not finished")

    def test_file_write(self):
        # TODO
        pytest.skip("Not finished")

    def test_modify_file(self):
        """
        Modify configuration object attribute value and commit changes to local file.
        Then check if the content of file is equal to the content of modified attribute.
        """
        person_name = "Jeff"
        self.config.Person_1.name = person_name
        self.controller.commit()

        read_dict = self.controller.read_file_as_dict()

        assert read_dict["Person_1"]["name"] == person_name

    def test_reset_file_to_defaults(self):
        """ Reset local file to values from bound default configuration """
        self.controller.reset_file_to_defaults()

        assert self.controller.read_file_as_dict()["Person_1"]["name"] == default_configuration_dict["Person_1"]["name"]

    def test_clear_object(self):
        """ Clear all object's attributes """
        self.controller.clear()

        assert len(vars(self.config)) == 0

    def test_refresh_object(self):
        """ Read all attributes from local file """
        self.controller.refresh()

        assert len(vars(self.config)) > 0

    def test_reset_object_to_file(self):
        """ Reset all object's attributes to values from bound configuration file """
        self.config.tobereset = True
        self.controller.reset_to_file()

        try:
            self.config.tobereset
        except AttributeError:
            return True
        else:
            return False

    def test_access_dashed_attribute_like_dict(self):
        assert self.config["dash-split"]["wow-man"] == default_configuration_dict["dash-split"]["wow-man"]

    def test_add_dashed_attribute_like_dict(self):
        self.config["dash-split"]["second-dashed"] = 515
        self.controller.commit()

        assert self.config["dash-split"]["second-dashed"] == \
               self.controller.read_file_as_dict()["dash-split"]["second-dashed"]

    def test_add_one_attribute(self):
        """
        Add one new attribute to object, commit changes
        and check assert the local file to object
        """
        key_name = "Masvingo"

        self.config.city = key_name
        self.controller.commit()

        assert self.config.city == self.controller.read_file_as_dict()["city"]

    def test_add_nested_dicts(self):
        """
        Add nested dictionary to object, commit changes and assert
        local file values to object
        """
        dct = {
            "sugar": {
                "carbon": 12,
            }
        }

        self.config.items = dct
        self.controller.commit()

        assert self.config.items.sugar.carbon == self.controller.read_file_as_dict()["items"]["sugar"]["carbon"]

    def test_add_nested_objects(self):
        self.config.lalilulelo.text = 'hello'
        self.controller.commit()

        assert self.config.lalilulelo.text == \
               self.controller.read_file_as_dict()['lalilulelo']['text']

    def test_add_multiple_dicts(self):
        """
        Add multiple dicts to object, commit changes
        and assert the result with local file
        """
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

        file_dict = self.controller.read_file_as_dict()["users"]

        assert self.config.users.jerre_1829.status == file_dict["jerre_1829"]["status"] and \
               self.config.users.wolfrm4882.status == file_dict["wolfrm4882"]["status"]
