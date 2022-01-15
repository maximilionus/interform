# serialix documentation


## About

On this branch you can find the source files of the `serialix` documentation. The [`Sphinx`](https://www.sphinx-doc.org/en/master/) tool was chosen as the engine for this documentation. The complex documentation build process was reduced to simply executing one command in shell then sitting and waiting for the result while drinking coffee.


## Makefile
The main thing on this branch is the [`Makefile`](./Makefile). It provides everything. Not going to describe here how and why everything works in it, just run the command below to show a list of available commands and their description.

```bash
$ make help
```
The main thing you should know is that before working with `Makefile` on your local machine you'd probably want to create a virtual environment *(`venv`, `virtualenv`, etc.)* to avoid the unforeseen consequences.
