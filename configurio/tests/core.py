from shutil import rmtree
from os import path, chdir

from configurio.core import BaseConfiguration


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
        self.config = BaseConfiguration()

    def test_delete_file(self):
        """
        Delete local configuration file and check
        is the functions output works correctly
        """
        expect_success = self.config.delete_file()
        expect_fail = not self.config.delete_file()

        assert expect_success and expect_fail

    def test_create_file(self):
        """ Create local configuration file """
        self.config.create_file()

        assert self.config.is_file_exist()

    def test_file_read(self):
        assert self.config.read_file_as_dict()["Person_1"]["name"] == default_configuration_dict["Person_1"]["name"]

    def test_commit_changes(self):
        person_name = "Jeff"
        self.config['Person_1']['name'] = person_name
        self.config.commit()

        read_dict = self.config.read_file_as_dict()

        assert read_dict["Person_1"]["name"] == person_name

    def test_clear_dict(self):
        """ Clear the `dictionary` attribute """
        self.config.clear()

        assert len(self.config) == 0

    def test_refresh_dict(self):
        """ Refresh `dictionary` from local file """
        self.config.refresh()

        assert len(vars(self.config)) > 0

    def test_reset_dict_to_file(self):
        """ Reset `dictionary` to values from bound configuration file """
        self.config['tobereset'] = False
        self.config.reset_to_file()

        assert self.config.get('tobereset', True)

    def test_access_dashed_attribute(self):
        assert self.config["dash-split"]["wow-man"] == default_configuration_dict["dash-split"]["wow-man"]

    def test_add_dashed_attribute(self):
        self.config["dash-split"]["second-dashed"] = 515
        self.config.commit()

        assert self.config["dash-split"]["second-dashed"] == \
               self.config.read_file_as_dict()["dash-split"]["second-dashed"]

    def test_add_one_attribute(self):
        """
        Add one new attribute to `dictionary`, commit changes
        and assert the local file to `dictionary`
        """
        key_name = "Masvingo"

        self.config['city'] = key_name
        self.config.commit()

        assert self.config['city'] == self.config.read_file_as_dict()["city"]

    def test_add_nested_dicts(self):
        """
        Add nested dictionary to `dictionary`, commit changes and assert
        local file values to `dictionary`
        """
        dct = {
            "sugar": {
                "carbon": 12,
            }
        }

        self.config['items'] = dct
        self.config.commit()

        assert self.config['items']['sugar']['carbon'] == self.config.read_file_as_dict()["items"]["sugar"]["carbon"]

    def test_add_multiple_dicts_with_update(self):
        """
        Add multiple dicts to `dictionary`, commit changes
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

        self.config['users'] = dct
        self.config.commit()

        file_dict = self.config.read_file_as_dict()["users"]

        assert self.config['users']['jerre_1829']['status'] == file_dict["jerre_1829"]["status"] and \
               self.config['users']['wolfrm4882']['status'] == file_dict["wolfrm4882"]["status"]

    def test_modify_default_dict(self):
        """Modify the default dictionary, reset `dictionary` to defaults and assert values"""
        self.config.dictionary_default.update({"new_values": [256, 45, 154]})
        self.config.reset_to_defaults()

        assert self.config.get('new_values', None) == self.config.dictionary_default['new_values']
