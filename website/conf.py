# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'bootstrap'
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
#
# html_theme_options = {
#     # Navigation bar title. (Default: ``project`` value)
#     'navbar_title': "zfit",
#
#     # Tab name for entire site. (Default: "Site")
#     # 'navbar_site_name': "Docs",
#     'navbar_site_name': "Overview",
#
#     # A list of tuples containing pages or urls to link to.
#     # Valid tuples should be in the following forms:
#     #    (name, page)                 # a link to a page
#     #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
#     #    (name, "http://example.com", True) # arbitrary absolute url
#     # Note the "1" or "True" value above as the third argument to indicate
#     # an arbitrary url.
#     # 'navbar_links': [
#     #     ("Getting started", "getting_started"),
#     #     ("Intro", "introduction"),
#     #     ("Project", "project"),
#     #     ("API", "user_api"),
#     #     # ("Dev API", "full_api"),
#     #     # ("Link", "http://example.com", True),
#     # ],
#
#     # Render the next and previous page links in navbar. (Default: true)
#     'navbar_sidebarrel': False,
#
#     # Render the current pages TOC in the navbar. (Default: true)
#     'navbar_pagenav': True,
#
#     # Tab name for the current pages TOC. (Default: "Page")
#     # 'navbar_pagenav_name': "Page",
#
#     # Global TOC depth for "site" navbar tab. (Default: 1)
#     # Switching to -1 shows all levels.
#     'globaltoc_depth': -1,
#
#     # Include hidden TOCs in Site navbar?
#     #
#     # Note: If this is "false", you cannot have mixed ``:hidden:`` and
#     # non-hidden ``toctree`` directives in the same page, or else the build
#     # will break.
#     #
#     # Values: "true" (default) or "false"
#     'globaltoc_includehidden': "true",
#
#     # HTML navbar class (Default: "navbar") to attach to <div> element.
#     # For black navbar, do "navbar navbar-inverse"
#     # 'navbar_class': "navbar navbar-inverse",
#     'navbar_class': "navbar",
#
#     # Fix navigation bar to top of page?
#     # Values: "true" (default) or "false"
#     'navbar_fixed_top': "true",
#
#     # Location of link to source.
#     # Options are "nav" (default), "footer" or anything else to exclude.
#     # 'source_link_position': "nav",
#     'source_link_position': 'footer',
#
#     # Bootswatch (http://bootswatch.com/) theme.
#     #
#     # Options are nothing (default) or the name of a valid theme
#     # such as "cosmo" or "sandstone".
#     #
#     # The set of valid themes depend on the version of Bootstrap
#     # that's used (the next config option).
#     #
#     # Currently, the supported themes are:
#     # - Bootstrap 2: https://bootswatch.com/2
#     # - Bootstrap 3: https://bootswatch.com/3
#     'bootswatch_theme': "flatly",
#
#     # Choose Bootstrap version.
#     # Values: "3" (default) or "2" (in quotes)
#     'bootstrap_version': "2",
# }
import atexit
from pathlib import Path

import pygit2

html_favicon = "images/zfit-favicon.png"
# type: ignore


import os
import shutil
import sys

project_dir = Path(__file__).parents[0]
zfit_tutorials_path = project_dir.joinpath('_tmp', 'zfit-tutorials')
atexit.register(lambda path=zfit_tutorials_path: shutil.rmtree(path))
# shutil.rmtree(zfit_tutorials_path)
pygit2.clone_repository("https://github.com/zfit/zfit-tutorials", zfit_tutorials_path)

jupyter_execute_notebooks = "cache"
if jupyter_execute_notebooks == "cache":
    jupyter_cache_path = project_dir.joinpath('.cache', 'myst-nb')
    jupyter_cache_path.mkdir(parents=True, exist_ok=True)
    jupyter_cache = str(jupyter_cache_path)
from pkg_resources import get_distribution

# -- Project information -----------------------------------------------------
project = "zfit"
package = "zfit"
repo_name = "zfit"
copyright = "2021, zfit"
author = "zfit"

# -- Generate API ------------------------------------------------------------
sys.path.insert(0, os.path.abspath("."))


# -- General configuration ---------------------------------------------------
master_doc = "index.md"
source_suffix = {
    ".ipynb": "myst-nb",
    ".md": "myst-nb",
    ".rst": "restructuredtext",
}

# The master toctree document.
master_doc = "index"
modindex_common_prefix = [
    f"{package}.",
]

extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_panels",
    "sphinx_thebe",
    "sphinx_togglebutton",
]
exclude_patterns = [
    "**.ipynb_checkpoints",
    "*build",
    "adr*",
    "tests",
]

# General sphinx settings
add_module_names = False
autodoc_insert_signature_linebreaks = False
graphviz_output_format = "svg"
html_copy_source = True  # needed for download notebook button
html_show_copyright = False
html_show_sourcelink = False
html_show_sphinx = False
html_sourcelink_suffix = ""
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": f"https://github.com/zfit/poster",
    "repository_branch": "master",
    "path_to_docs": "website",
    "use_download_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com",
        "notebook_interface": "jupyterlab",
        "thebe": True,
        "thebelab": True,
    },
    "theme_dev_mode": True,
}
html_title = "zfit"
pygments_style = "sphinx"
todo_include_todos = False
viewcode_follow_imported_members = True

# Cross-referencing configuration
default_role = "py:obj"
primary_domain = "py"
nitpicky = True  # warn if cross-references are missing


intersphinx_mapping = {

    "iminuit": ("https://iminuit.readthedocs.io/en/stable", None),
    "jax": ("https://jax.readthedocs.io/en/stable", None),
    "matplotlib": ("https://matplotlib.org", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "pwa": ("https://pwa.readthedocs.io", None),
    "python": ("https://docs.python.org/3", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "sympy": ("https://docs.sympy.org/latest", None),
}

# Settings for autosectionlabel
autosectionlabel_prefix_document = True

# Settings for copybutton
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. "  # doctest

# Settings for linkcheck
linkcheck_anchors = False

# Settings for myst_nb
execution_timeout = -1
nb_output_stderr = "remove"
nb_render_priority = {
    "html": (
        "application/vnd.jupyter.widget-view+json",
        "application/javascript",
        "text/html",
        "image/svg+xml",
        "image/png",
        "image/jpeg",
        "text/markdown",
        "text/latex",
        "text/plain",
    )
}
nb_render_priority["doctest"] = nb_render_priority["html"]


# Settings for myst-parser
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "dollarmath",
    "smartquotes",
]
myst_update_mathjax = False

# Settings for Thebe cell output
thebe_config = {
    "repository_url": html_theme_options["repository_url"],
    "repository_branch": html_theme_options["repository_branch"],
}
