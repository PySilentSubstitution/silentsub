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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'PySilSub'
copyright = '2022, Joel T. Martin'
author = 'Joel T. Martin'

# The full version, including alpha/beta/rc tags
release = '0.1.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax"
    ]

nbsphinx_prompt_width = 150

# Show docs in order of definition
autodoc_class_signature = 'separated'
autodoc_member_order = 'bysource'
autodoc_typehints_description_target = 'all'
#autodoc_typehints_format = 'short'
autodoc_typehints = 'description'
#autodoc_type_aliases = {
#    'PrimaryInput': 'pysilsub.devices.PrimaryInput',
#    'PrimaryWeights': 'pysilsub.devices.PrimaryWeights',
#    'PrimarySettings': 'pysilsub.devices.PrimarySettings',
#    'DeviceInput': 'pysilsub.devices.DeviceInput'
#}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_logo = '../../logo/photoreceptor_characters.png'
html_theme_options = {
    'github_user': 'PySilentSubstitution',
    'github_repo': 'pysilsub',
        'extra_nav_links': {
        'PyPi': 'https://pypi.org/project/pysilsub/',
        'Paper': 'https://jov.arvojournals.org/article.aspx?articleid=2791309'
    },
    'description': 'A Python toolbox for performing the method of silent substitution.'
}
#    ,
#    'extra_nav_links': {'PyPi': 'https://pypi.org/project/pyplr/', 
#    'bioRxiv preprint':'https://www.biorxiv.org/content/10.1101/2021.06.02.446731v1'},
#    
#}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
