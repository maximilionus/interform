# serialix documentation


## About

On this branch you can find the source files of the `serialix` documentation. The [`Sphinx`](https://www.sphinx-doc.org/en/master/) tool was chosen as the engine for this documentation. The complex documentation build process was reduced to simply executing one command in shell then sitting and waiting for the result while drinking coffee ☕.


## Makefile
The main thing on this branch is the [`Makefile`](./Makefile). It provides everything. Not going to describe here how and why everything works in it, just run the command below to show a list of available commands and their description.

```bash
$ make help
Documentation makefile

Commands:
    build - build Sphinx documentation in html format
    pull  - clone main project files that required for documentation build
    clean - clean all temporary and cache files
    help  - display this help message

Optional arguments:
    from_branch=<STR> - build documentation from specified git branch
                        defaults to "master"
    from_dir=<STR>    - build documentation from specified directory

    - usage example:
        make <command> opt_arg_name="value"
```
The main thing you should know is that before working with `make` on your local machine you'd need to ensure that [`gnumake`](https://www.gnu.org/software/make/) is installed and probably want to create a virtual environment for python *([`venv`](https://docs.python.org/3/library/venv.html), [`virtualenv`](https://virtualenv.pypa.io/en/latest/), etc.)* to avoid installing all project deps system-wide.
