from datetime import datetime

from interform.meta import __version__ as interform_version


# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'interform'
copyright = '2020, maximilionus'
author = 'maximilionus'

# The full version, including alpha/beta/rc tags
release = interform_version

# Time of docs build
docs_build_time = datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S UTC+0000")

rst_epilog = """
.. |docs_build_time| replace:: {}
""".format(
    docs_build_time
)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages'
]

templates_path = ['_templates']
html_static_path = ['_static']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_theme = 'sphinx_rtd_theme'
html_logo = ''  # TODO
