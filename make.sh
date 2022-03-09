#!/bin/bash

set -e

PYTHON=python
readonly REQUIRED_PROJECT_FILES="serialix setup.py README.rst requirements-dev.txt"
readonly CACHE_PATHS="*.egg-info ./dist ./build"


display_help() {
    printf "\
Documentation makefile\n---
Commands:
    build       - build Sphinx documentation in html format
                  warning: 'gnumake' is required
    clean       - clean all temporary, cache and built files
                  note: '.venv' directory will NOT be removed
    help        - display this help message

Env. variables:
    from_branch - build documentation from specified git branch.
                  defaults to \"master\"

    - usage example:
        env_variable_name=\"value\" ./make.sh <command>
"
}

do_clean() {
	echo "[ Removing pulled main project files ]"
    rm -rfv $REQUIRED_PROJECT_FILES
    echo "[ Removing cache files ]"
    rm -rfv $CACHE_PATHS
	echo "[ Removing documentation build folder ]"
    rm -rfv ./docs/_build
    echo "[ All cache, temp and built files removed ]"
}

build_documentation() {
    echo "[ Initializing the documentation builder ]"

    if [[ -z ${from_dir+x} ]]; then
        echo "[ Obtaining project from '$from_branch' branch ]"
        git restore --source "$from_branch" $REQUIRED_PROJECT_FILES
    else
        # TODO realisation of build from dir feature
        #echo "[ Obtaining project from '$from_dir' directory ]"
        echo "Not implemented yet :("; exit 1
    fi

    echo "[ Installing all project dependencies ]"
    $PYTHON -m pip install -U -r ./requirements-dev.txt -r ./requirements.txt

    echo "[ Documentation build is starting now ]"
    make -C ./docs html
}


# Prepare variables
if [[ -z ${from_branch+x} ]]; then
    from_branch="master"
fi


# Handle arguments
case "$1" in
    help|h )
    display_help
    ;;

    build )
    build_documentation
    ;;

    clean )
    do_clean
    ;;

    * )
    # No valid arguments passed action
    display_help
    ;;
esac
