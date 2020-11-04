# Configerz Changelog


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
