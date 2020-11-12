# Interform Changelog


--------------------------
## Early Stage Development

----------
2020.11.13

# Added
- Docstrings at the beginning of each `.langs` module, describing its purpose.

## Changed
- Renamed the `.configs` subpackage to `.langs`
- Renamed `.core.BaseInterchange` to `.core.BaseLang`
- Renamed `.tests.BaseConfigTest` to `.tests.BaseLangTest`
- Renamed the variable `.tests.*::self.config` to `.tests.*::self.language_object`
- Modified `.core.BaseLang` docstrings


----------
2020.11.12

## Added
- Support for `XML` language with unit testing suite

## Changed
- Renamed some variables in tests core
- Added information about `XML` language to `README.rst` and docs
- Adjusted `setup.py` to support new `XML` language feature


----------
2020.11.10

## Added
- New `safe_mode` feature to `.core.BaseConfiguration.refresh()` with tesing suite modifications
- Links to *docs* and *bug tracker* to `setup.py` script
- What version of `configurio` is docs for and revision time in index page

## Changed
- Project version to `1.0.0` (Preparing for the release)
- Enhanced *installation guide* section in docs


----------
2020.11.09

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


----------
2020.11.04

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
