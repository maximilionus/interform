.PHONY: build pull clean help

PYTHON ?= python

REQUIRED_PROJECT_FILES = "serialix setup.py README.rst requirements-dev.txt"
CACHE_PATHS = "*.egg-info ./dist ./build"

ifndef from_branch
	override from_branch="master"
endif


build: pull
	@echo "[ Initializing the documentation builder ]"

	@echo "[ Installing all project dependencies ]"
	@$(PYTHON) -m pip install -U -r ./requirements-dev.txt -r ./requirements.txt

	@echo "[ Documentation build is starting now ]"
	@make -C ./docs html


pull:
ifndef from_dir
	@echo "[ Obtaining project from '$(from_branch)' branch ]"
	@git restore --source "$(from_branch)" "$(REQUIRED_PROJECT_FILES)"
else
	@echo "[ Obtaining project from '$(from_dir)' directory ]"
	$(eval PROJ_DIR := $(shell pwd))
	@cd $(from_dir); \
		cp -rv --target-directory="$(PROJ_DIR)" "$(REQUIRED_PROJECT_FILES)"
endif


clean:
	@echo "[ Removing pulled main project files ]"
	@rm -rfv "$(REQUIRED_PROJECT_FILES)"
	@echo "[ Removing cache files ]"
	@rm -rfv $(CACHE_PATHS)
	@echo "[ Removing documentation build folder ]"
	@rm -rfv ./docs/_build
	@echo "[ All cache, temp and built files removed ]"


help:
	@printf "\
	Documentation makefile\n\n\
	Commands:\n\
	    build - build Sphinx documentation in html format\n\
	    pull  - clone main project files that required for documentation build\n\
	    clean - clean all temporary and cache files\n\
	    help  - display this help message\n\
	\n\
	Optional arguments:\n\
	    from_branch=<STR> - build documentation from specified git branch\n\
	                        defaults to \"master\"\n\
	    from_dir=<STR>    - build documentation from specified directory\n\
	\n\
	    - usage example:\n\
	        make <command> opt_arg_name=\"value\"\n\
	"
