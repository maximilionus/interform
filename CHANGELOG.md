# serialix Changelog

This project uses a [semantic versioning](https://semver.org/) scheme as the base for naming all the releases


## Stable Releases


### **2.1.2** : 2022.02.28

### Changed
- Enhanced package description text

### Fixed
- Solved not critical security issues with setup script


### **2.1.1** : 2022.02.24

#### Changed
- `serialix.core.BaseLang`: `parser_write_kwargs`, `parser_read_kwargs`, `dictionary` properties are now secured from wrong data type assignment


### **2.1.0** : 2022.02.03

#### Added
- New class `Serialix` can be imported straight from package root and now will be a preferred way of creating instance of `serialix` for any supported language instead of using `*_Language` classes directly.
- `NotImplementedError` exception will now be raised when trying to execute any R/W-related action in class, inherited from `serialix.core.BaseLang` without defined `_core__read_file_to_dict` and `_core__write_dict_to_file` methods.
- New 'get version' feature in built-in CLI toolset. Can be accessed with `--version` or `-V` argument passed to cli.

#### Changed
- Extended the range of dependencies versions lock.

### Removed
- `serialix.core.parse_dict_values()` function were cut due to uselessness and security reasons.


### **2.0.1** : 2022.01.15

> This QOL *(Quality Of Life)* update is focused on updating the external packages version locks and enhancing the overall package quality with documentation, unit-testing and other features updated.

#### Changed
- Updated the YAML language parser ([`ruamel.yaml`](https://pypi.org/project/ruamel.yaml/)) support to the latest version `0.17.20`
- Updated the [`ujson`](https://pypi.org/project/ujson/) support up to the latest `5.1.0` version


### **2.0.0** : 2020.11.28

#### Changed
- Project renamed to ``serialix``


### **1.3.2** : 2020.11.29

#### Notification
⚠ `interform` will be renamed to `serialix` from version **2.0.0**


### **1.3.1** : 2020.11.28

#### Fixed
- Docstrings for `serialix.core.BaseLang`


### **1.3.0** : 2020.11.28

#### Added
- Command Line Interface *(CLI)* toolset with documentation
  - Format converter tool


### **1.2.0** : 2020.11.26

#### Added
- Keyword argument `auto_file_creation` to all `*_Format` classes which will allow to disable the automatic local file creation on `*_Format` object initialization

#### Changed
- In `*_Format` classes, instead of only `.create_file()` method, all directories generation now placed in `write_dict_to_file()` method. This change will affect all 'write to file' actions and prevent all path related issues.


### **1.1.2** : 2020.11.25

#### Fixed
- `.values` method in all `*_Format` classes will now return expected value. Before the fix, this method returned the values of bound to object default dictionary.


### **1.1.1** : 2020.11.24

#### Fixed
- `.reload()` method return now works properly in all `*_Format` classes


### **1.1.0** : 2020.11.23

#### Added
- Support for `TOML` language
- Feature to pass custom arguments to parser on read and write actions with `parser_write_kwargs` and `parser_read_kwargs`

#### Fixed
- Fixed new key creation from main object issue

#### Changed
- Method of handling import requests in init script
- `_core__write_dict_to_file` and `_core__read_file_to_dict` are no more static methods in `.core.BaseLang` and inherited classes
- Enhanced documentation

#### Removed
- Advanced `JSON_Format` parser arguments removed


### **1.0.0** : 2020.11.18

> First public release of this package


## Development Releases

### **2.2.0dev**: nightly
#### Changed
- Deps versions range now locked to the last available versions *(`<=x.y.z`)* instead of full *MAJOR* range *(`<=x`)*


### **2.2.0a1** : 2022.03.16

#### Fixed
- Docstrings for `serialix.serialix.Serialix` class and all the parents

#### Changed
- All variables in `serialix.meta` now public. Changes will not affect the `serialix.__init__`, I.e. - project version and author can still be accessed like `serialix.__version__` and `serialix.__author__` respectively
- Enhanced docstrings for the entire project


### **2.1.1a1** : 2022.02.13

#### Changed
- `serialix.core.BaseLang`: `parser_write_kwargs`, `parser_read_kwargs`, `dictionary` properties are now secured from wrong data type assignment


### **2.1.0a2** : 2022.02.02

### Added
- New 'get version' feature in built-in CLI toolset. Can be accessed with `--version` or `-V` argument passed to cli.

### Removed
- `serialix.core.parse_dict_values()` function were cut due to uselessness and security reasons


### **2.1.0a1** : 2022.02.01

#### Added
- New class `Serialix` can be imported straight from package root and now will be a preferred way of creating instance of `serialix` for any supported language instead of using `*_Language` classes directly
- `NotImplementedError` exception will now be raised when trying to execute any R/W-related action in class, inherited from `serialix.core.BaseLang` without defined `_core__read_file_to_dict` and `_core__write_dict_to_file` methods

#### Changed
- Extended the range of dependencies versions lock


### **2.0.1a1** : 2022.01.14

#### Changed
- Updated the YAML language parser ([`ruamel.yaml`](https://pypi.org/project/ruamel.yaml/)) support to the latest version *(0.17.20)*
- Updated the [`ujson`](https://pypi.org/project/ujson/) supported version up to the latest `5.1.0`


### **1.3.0a1** : 2020.11.27

#### Added
- Command Line Interface *(CLI)* toolset with documentation
  - Format converter tool


### **1.2.0a2** : 2020.11.25

#### Changed
- In `*_Format` classes, instead of only `.create_file()` method, all directories generation now placed in `write_dict_to_file()` method. This change will affect all 'write to file' actions and prevent all path related issues.


### **1.2.0a1** : 2020.11.25

#### Added
- Keyword argument `auto_file_creation` to all `*_Format` classes which will allow to disable the automatic local file creation on `*_Format` object initialization

#### Changed
- ~~`.create_file()` method in all `*_Format` classes will now automatically create all detected dirs in path to local file~~


### **1.1.0a2** : unreleased

#### Added
- Feature to pass custom arguments to parser on read and write actions with `parser_write_kwargs` and `parser_read_kwargs`

#### Changed
- `_core__write_dict_to_file` and `_core__read_file_to_dict` are no more static methods in `.core.BaseLang` and inherited classes
- Enhanced documentation


### **1.1.0a1** : 2020.11.22

#### Added
- Support for `TOML` language

#### Fixed
- Fixed new key creation from main object issue

#### Changed
- Method of handling import requests in init script


---------

<details>
<summary>Pre-Release Development Changelog</summary>

> In this part of changelog you can track the progress of development before the public `1.0.0` version release.


## 2020.11.18

### Changed
- Changed version to `1.0.0`
- `.core.BaseLang` methods inheritance modified a bit
- Github workflows prepared for release state

### Fixed
- Documentation folder name for github page build
- Link to documentation page in main `README.rst`

### Removed
- Posfix for documentation display version


## 2020.11.17

### Added
- `.core.BaseLang`
  - `refresh()` and `reload()` now will return `bool` value
- Root makefile target to publish the package

### Fixed
- `.core.*`
  - `BaseLang.copy()` and `recursive_dicts_merge()` copy was fixed with `copy.deepcopy()` module to remove all references to original dictionary
- `ModuleNotFoundError` exception on importing `serialix` without external package installed

### Changed
- Version changed to `1.0.0dev1` for test release purpose
  - Changed to `1.0.0dev2`
- Replaced all `"` quotation marks with `'`
- Enhanced the docstrings for `.core`
- Enhanced docs structure
- Makefile usage added to `release.yml` workflow


## 2020.11.16

### Added
- README to `./examples/` dir

### Fixed
- `.core.recursive_dicts_merge()` was not merging anything

### Changed
- Docs version postfix = `_predocs`. Will be removed on release.
- Enhanced docs
- Docs makefile now will create `_static` dir on run, if it doesn't exist

### Removed
- `:ref:` from docs. Replaced with html links.


## 2020.11.15

### Added
- Project root makefile containing options to build the package and documentation

### Changed
- Project classifiers `Development Status` to `5 - Production/Stable`

### Removed
- `XML` and `INI` support cutted due to unfinished state. Realisation code moved to repo branch `dev/lang_support`


## 2020.11.14

### Added
- Started implementation of `INI` dif language support with full tests support
- Created and almost finished function `.core.parse_dict_values()`

### Changed
- Enhanced main package `__init__`
- README and docs 'Supported Languages' changed
- Changed 'about' info in README and docs

## Removed
- Variable converting in `.tests.core` due to `.core.parse_dict_values()` is almost ready to implement


## 2020.11.13

### Added
- Docstrings at the beginning of each `.langs` module, describing its purpose.

### Changed
- Renamed the `.configs` subpackage to `.langs`
- Renamed `.core.BaseInterchange` to `.core.BaseLang`
- Renamed `.tests.BaseConfigTest` to `.tests.BaseLangTest`
- Renamed the variable `.tests.*::self.config` to `.tests.*::self.language_object`
- Modified `.core.BaseLang` docstrings
- Enhanced the 'about' description in README and docs


## 2020.11.12

### Added
- Support for `XML` language with unit testing suite

### Changed
- Renamed some variables in tests core
- Added information about `XML` language to `README.rst` and docs
- Adjusted `setup.py` to support new `XML` language feature


## 2020.11.10

### Added
- New `safe_mode` feature to `.core.BaseConfiguration.refresh()` with tesing suite modifications
- Links to *docs* and *bug tracker* to `setup.py` script
- What version of `configurio` is docs for and revision time in index page

### Changed
- Project version to `1.0.0` (Preparing for the release)
- Enhanced *installation guide* section in docs


## 2020.11.09

### Added
- Basic documentation *(WIP)*
- `.core.BaseConfiguration`
  - Added iterator support
- Created simple example usage of this package as a CLI tool

### Fixed
- Optional argument `default_config` in `.core.BaseConfiguration` is now really optional. Yeah.
- Methods `pop()` and `popitem()` in `.core.BaseConfiguration` now will return values as expected.

### Changed
- `.core.BaseConfiguration`
  - `refresh()` now will merge all changes to config dictionary without overwriting the nested dicts
  - Renamed `reset_to_file()` method to `reload()`


## 2020.11.04

### Added
- `Yaml` support *(<=1.2)* with [`ruamel.yaml`](https://pypi.org/project/ruamel.yaml/) module. `PyYaml` support dropped. Tests added.
- `.core.BaseConfiguration` additions:
  - `dict` methods to work with `__configuration_dict`
  - Added getters and setters for `__configuration_dict` and `__default_local_file_dict`
- Custom markers `yaml` and `json` to PyTest configuration
- `test` bundle to `setup.py`'s `extras_require` with all necessary for testing packages

### Fixed
- Existing files will no longer be overwritten with values from the default dictionary on object initialization

### Changed
- Unit tests suite modified to current changes and enhanced
- `.core.BaseConfiguration.__init__()`:
  - `default_config` argument is now optional
  - `create_if_not_found` argument removed

### Removed
- Got rid of the object model access and switched to dict support
- Useless version range lock from `requirements-dev.txt` and `setup.py`
- Removed logging module support
- `.core.BaseConfiguration` removals:
  - `reset_file_to_defaults()` method
  - `__repr__()` method


## 0.0.2-dev2 : 2020.11.05
> This version was the last attempt to create object model configuration files. I decided to give up this idea, because the realisation of this feature was awful.

### Added
- Feature to extend the current configuration object with dictionaries
- Create nested attributes in object without any dicts usage
  - Example:
    ```python
    >>> cfg = Configuration()
    >>> cfg.test.nested.d = "yes"
    >>> cfg.test.nested.d
    'yes'
    ```

### Changed
- Split configuration files controllers by type in submodule `.configs`
- Enhanced unit tests coverage
- Moved unit tests to project directory
- Renamed some methods to more friendly variants

### Fixed
- `.core.BaseController.clear()` implementation fixed
- `.core.Namespace.__getitem__()` behaviour fixed


## 0.0.2-dev1 : 2020.11.01

### Added
- `clear` method to `.core.BaseController`
- proto for new function `.core.dict_to_namespace()`

### Changed
- Fully refactored the config system
  - New way of interacting with configurations: `Configuration` and `Controller`
  - Values now will be stored in `Configuration` class
  - All methods now located in `*Controller` classes
- Updated unit tests to new code

</details>
