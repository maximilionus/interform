# Configerz Changelog

## Dev

### Added

- Feature to extend the current configuration object with dictionaries

### Changed

- Enhanced unit tests coverage

### Fixed

- `.core.BaseController.clear()` implementation fixed

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
