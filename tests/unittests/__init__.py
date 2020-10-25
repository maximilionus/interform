from ..fixtures import change_path_to_testsdir


change_path_to_testsdir()

# Import classes that should be ran in unit test
from .test_json import Test_DefaultFromDict, Test_DefaultFromFile
