# serialix documentation


## About

On this branch you can find the source files of the `serialix` documentation. The [`Sphinx`](https://www.sphinx-doc.org/en/master/) tool was chosen as the engine for this documentation. The complex documentation build process was reduced to simply executing one command in shell then sitting and waiting for the result while drinking coffee.


## Makefile
The main thing on this branch is the [`make.sh`](./make.sh). It provides everything. Not going to describe here how and why everything works in it, just run the command below to show a list of available commands and their description.

```bash
$ ./make.sh help
Documentation makefile
---
Commands:
    build       - build Sphinx documentation in html format
                  warning: 'gnumake' is required
    clean       - clean all temporary, cache and built files
                  note: '.venv' directory will NOT be removed
    help        - display this help message

Env. variables:
    from_branch - build documentation from specified git branch.
                  defaults to "master"

    - usage example:
        env_variable_name="value" ./make.sh <command>
```
The main thing you should know is that before working with `make.sh` on your local machine you'd need to ensure that [`gnumake`](https://www.gnu.org/software/make/) is installed and probably want to create a virtual environment for python *([`venv`](https://docs.python.org/3/library/venv.html), [`virtualenv`](https://virtualenv.pypa.io/en/latest/), etc.)* to avoid installing all project deps systemwide.
