.PHONY: build build_sdist build_wheel publish help

PYTHON ?= python


build: build_sdist build_wheel


build_sdist:
	@echo "[ Building project sdist ]"
	@$(PYTHON) setup.py build sdist


build_wheel:
	@echo "[ Building project wheel ]"
	@$(PYTHON) setup.py build bdist_wheel


publish:
	twine upload dist/*


help:
	@printf "\
	Main project makefile\n\n\
	Commands:\n\
		build       - build project source distribution and wheel\n\
		build_dist  - build project source distribution\n\
		build_wheel - build project wheel distribution\n\
		publish     - upload build package from dist/* to PyPI\n\
		help        - display this help message\n\
	"
