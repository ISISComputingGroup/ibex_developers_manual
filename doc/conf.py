# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

project = "IBEX Developer's Manual"
copyright = ""
author = "ISIS Experiment Controls"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

nitpicky = True

myst_enable_extensions = ["dollarmath", "strikethrough", "colon_fence", "linkify"]
suppress_warnings = ["myst.strikethrough"]

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    # and making summary tables at the top of API docs
    "sphinx.ext.autosummary",
    # This can parse google style docstrings
    "sphinx.ext.napoleon",
    # For linking to external sphinx documentation
    "sphinx.ext.intersphinx",
    # Add links to source code in API docs
    "sphinx.ext.viewcode",
]
napoleon_google_docstring = True
napoleon_numpy_docstring = False

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "ISISComputingGroup",  # Username
    "github_repo": "ibex_developers_manual",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/doc/",  # Path in the checkout to the docs root
}

html_title = "IBEX Developer's Manual"
html_short_title = "Dev Manual"
html_theme = "sphinx_rtd_theme"
html_logo = "logo.svg"
html_theme_options = {
    "logo_only": False,
    "style_nav_header_background": "#343131",
}
html_favicon = "favicon.ico"
html_static_path = ["_static"]
html_css_files = [
    'css/custom.css',
]

autoclass_content = "both"
myst_heading_anchors = 1
html_last_updated_fmt = ""
