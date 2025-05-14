# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os.path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = "IBEX Developer's Manual"
copyright = ""
author = "ISIS Experiment Controls"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

nitpicky = True

myst_enable_extensions = [
    "dollarmath",
    "strikethrough",
    "colon_fence",
    "linkify",
    "html_image",
    "attrs_block",
]
suppress_warnings = ["myst.strikethrough", "myst.header"]

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
    # Redirects
    "sphinx_reredirects",
    # Mermaid diagrams
    "sphinxcontrib.mermaid",
    # Graphvis diagrams
    "sphinx.ext.graphviz",
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
    "css/custom.css",
]

autoclass_content = "both"
myst_heading_anchors = 7
myst_linkify_fuzzy_links = False
html_last_updated_fmt = ""
html_show_copyright = False

html_search_scorer = os.path.join(os.path.dirname(__file__), "searchscorer.js")

spelling_lang = "en_GB"
spelling_filters = ["enchant.tokenize.MentionFilter"]
spelling_warning = True
spelling_show_suggestions = True
spelling_suggestion_limit = 3

redirects = {
    "client/GUI-Getting-Started": "GUI-Building.html",
    "client/eclipse/Creating-the-IBEX-Developer-Version-of-Eclipse": "../compiling/Building-the-GUI.html#gui-build-install-eclipse",  # noqa E501
    "client/eclipse/Dictionary-setup": "Common-Eclipse-Issues.html#adding-a-dictionary-to-eclipse-s-spelling-checker",  # noqa E501
    "client/getting_started/GUI-Development-Workflow": "../../processes/git_and_github/Git-workflow.html",  # noqa E501
}
