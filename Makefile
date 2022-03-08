.PHONY: build prepare_vars clean_required_files clean help

PYTHON = python
REQUIRED_PROJECT_FILES = "serialix setup.py README.rst requirements-dev.txt"


build: prepare_vars
	@echo "Building the documentation with Sphinx"

	@echo "Obtaining project from $(branch) branch"
	@git restore --source "$(branch)" "$(REQUIRED_PROJECT_FILES)"

	@echo "Installing all project dependencies"
	@$(PYTHON) -m pip install -U -r ./requirements-dev.txt -r ./requirements.txt

	@echo "Documentation build begin"
	@make -C ./docs html


prepare_vars:
	@if [ -z ${branch} ]; then\
		branch="master";\
	fi


clean_required_files:
	@rm -rf "$(REQUIRED_PROJECT_FILES)"
	@echo "Required project files successfully removed"


clean: clean_required_files
	@rm -rf ./docs/_build
	@echo "Documentation build folder successfully removed"


help:
	@printf "\
	Documentation makefile\n\n\
	Commands:\n\
		build                - build Sphinx documentation in html format\n\
		clean                - clean all temporary and cache files\n\
		clean_required_files - clean files required for the documentation build\n\
		help                 - display this help message\n\
	"
