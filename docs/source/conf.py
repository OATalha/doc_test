# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os, sys
sys.path.insert(0, os.path.abspath('./'))


project = 'One Animation Pipeline Docs#'
copyright = '2022, One Animation RnD Team'
author = 'One Animation RnD Team'
release = '0.0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'repoget',
    'autoapi.extension',
    'sphinx.ext.autodoc.typehints',
    'sphinx.ext.coverage',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

repoget_clonedir = os.path.abspath('../_repos/')
repoget_cleanup_clonedir = True

autoapi_dirs = list(filter(
    lambda x: repoget_clonedir in x and os.path.isdir(x),
    sys.path))

autoapi_keep_files = True
autoapi_add_toctree_entry = False
autoapi_python_class_content = 'both'
autoapi_python_use_implicit_namespaces = False
autoapi_template_dir = '_templates/autoapi/'
suppress_warnings = ['autoapi']

apigen_dir = 'api'
apigen_cleanup = False

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

autodoc_typehints = 'both'

autosectionlabel_prefix_document = True

todo_include_todos = True

templates_path = ['_templates']
exclude_patterns = ['autoapi/templates', 'api']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
