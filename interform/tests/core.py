from shutil import rmtree
from os import path, chdir

from interform.core import BaseInterchange


temp_dir_path = './temp/'

local_file_path = path.join(temp_dir_path, 'test_config.txt')
default_cfg_path = path.join(temp_dir_path, 'default_config.json')

default_local_file_dict = {
    "root": {
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
}


def remove_temp_dir():
    if path.isdir(temp_dir_path):
        rmtree(temp_dir_path)


def change_path_to_testsdir():
    """ Change working directory to `/tests/` """
    chdir(path.dirname(__file__))


class BaseConfigTest():
    """
    Base class for all tests.
    `setup_method()` method should be overwritten with valid config object initialization.
    """
    def setup(self):
        self.config = BaseInterchange()

    def test_delete_file(self):
        """
        Delete local file and check
        is the functions output works correctly
        """
        expect_success = self.config.delete_file()
        expect_fail = not self.config.delete_file()

        assert expect_success and expect_fail

    def test_create_file(self):
        """ Create local file """
        self.config.create_file()

        assert self.config.is_file_exist()

    def test_file_read(self):
        assert self.config.read_file_as_dict()["root"]["Person_1"]["name"] == default_local_file_dict["root"]["Person_1"]["name"]

    def test_commit_changes(self):
        person_name = "Jeff"
        self.config["root"]['Person_1']['name'] = person_name
        self.config.commit()

        read_dict = self.config.read_file_as_dict()

        assert read_dict["root"]["Person_1"]["name"] == person_name

    def test_clear_dict(self):
        """ Clear the `dictionary` attribute """
        self.config.clear()

        assert len(self.config) == 0

    def test_refresh_safe(self):
        """
        Refresh `dictionary` from local file in safe mode
        and check for nested dictionary existance inside.
        """
        self.config["root"]['nested_dict_refresh_test'] = {"will_stay": "cia"}
        self.config.commit()
        self.config["root"]['nested_dict_refresh_test']["will_stay_too"] = "wait..."
        self.config.refresh()

        assert self.config["root"]['nested_dict_refresh_test'].get("will_stay", None) is not None and \
               self.config["root"]['nested_dict_refresh_test'].get("will_stay_too", None) is not None

    def test_refresh_unsafe(self):
        self.config["root"]['nested_dict_refresh_test'] = {"will_stay": "cia"}
        self.config.commit()
        self.config["root"]['nested_dict_refresh_test']["will_be_lost"] = "what!?"
        self.config.refresh(safe_mode=False)

        assert self.config["root"]['nested_dict_refresh_test'].get("will_be_lost", None) is None and \
               self.config["root"]['nested_dict_refresh_test'].get("will_stay", None) is not None

    def test_reload_dict(self):
        """ Reset `dictionary` to values from bound local file """
        self.config["root"]['tobereset'] = False
        self.config.reload()

        assert self.config.get('tobereset', True)

    def test_access_dashed_attribute(self):
        assert self.config["root"]["dash-split"]["wow-man"] == default_local_file_dict["root"]["dash-split"]["wow-man"]

    def test_add_dashed_attribute(self):
        self.config["root"]["dash-split"]["second-dashed"] = "ok guys, bye"
        self.config.commit()

        assert self.config["root"]["dash-split"]["second-dashed"] == \
               self.config.read_file_as_dict()["root"]["dash-split"]["second-dashed"]

    def test_add_one_attribute(self):
        """
        Add one new attribute to `dictionary`, commit changes
        and assert the local file to `dictionary`
        """
        key_name = "Masvingo"

        self.config["root"]['city'] = key_name
        self.config.commit()

        assert self.config["root"]['city'] == self.config.read_file_as_dict()["root"]["city"]

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

        self.config["root"]['items'] = dct
        self.config.commit()

        assert int(self.config["root"]['items']['sugar']['carbon']) == int(self.config.read_file_as_dict()["root"]["items"]["sugar"]["carbon"])

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

        self.config["root"]['users'] = dct
        self.config.commit()

        file_dict = self.config.read_file_as_dict()["root"]["users"]

        print(file_dict["jerre_1829"]["status"])
        print(self.config["root"]['users']['jerre_1829']['status'])

        assert int(self.config["root"]['users']['jerre_1829']['status']) == int(file_dict["jerre_1829"]["status"]) and \
               int(self.config["root"]['users']['wolfrm4882']['status']) == int(file_dict["wolfrm4882"]["status"])

    def test_modify_default_dict(self):
        """Modify the default dictionary, reset `dictionary` to defaults and assert values"""
        self.config.dictionary_default["root"].update({"new_values": [256, 45, 154]})
        self.config.reset_to_defaults()

        assert self.config["root"].get('new_values', None) == self.config.dictionary_default["root"]['new_values']
