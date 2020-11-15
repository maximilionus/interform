.PHONY: build, build_dist, build_wheel, docs, help

PYTHON = python


build: build_dist build_wheel

build_dist:
	@echo "Building project source distribution"
	@$(PYTHON) setup.py build sdist

build_wheel:
	@echo "Building project wheel distribution"
	@$(PYTHON) setup.py build bdist_wheel

docs:
	@echo "Building the documentation html with Sphinx"
	@make -C ./docs html

help:
	@printf "\
	Main project makefile\n\n\
	Commands:\n\
		build - build project source distribution and wheel\n\
		build_dist - build project source distribution\n\
		build_wheel - build project wheel distribution\n\
		docs - build Sphinx documentation in html format\n\
		help - display this help message\n\
	"
