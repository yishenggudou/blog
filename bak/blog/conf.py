# -*- coding: utf-8 -*-
#
# java all documentation build configuration file, created by
# sphinx-quickstart on Thu Mar 22 11:16:23 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import distutils.sysconfig

site_package_path = distutils.sysconfig.get_python_lib()
sys.path.insert(0, os.path.join(site_package_path, 'sphinxcontrib/unicode_ids'))

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_DIR)
sys.path.insert(0, os.path.join(PROJECT_DIR, 'libs'))
os.environ["PATH"] = "{0}:{1}".format(PROJECT_DIR, os.environ["PATH"])
# -- General configuration ------------------------------------------------
# If your documentation needs a minimal Sphinx version, state it here.
#

# needs_sphinx = '1.0'
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.extlinks',
    "sphinxcontrib.plantuml",
    "sphinxcontrib.httpdomain",
    'matplotlib.sphinxext.only_directives',
    'matplotlib.sphinxext.plot_directive',
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    'numpydoc',
    'nbsphinx',
    'sphinx.ext.inheritance_diagram',
    'unicode_ids',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md']

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

# The master toctree document.
master_doc = 'index'
import datetime

# General information about the project.
project = u'timger'
copyright = u'{0}, timger'.format(datetime.datetime.now().year)
author = u'timger'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.0.1'
# The full version, including alpha/beta/rc tags.
release = u'0.0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'timger'
html_favicon = "7ffecc813fcf64fad5cec4e987d5435b.ico"
# -- Options for LaTeX output ---------------------------------------------


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'manual', u'manual Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'manual', u'manual Documentation',
     author, 'manual', 'some desc',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
try:
    import releasenotes

    extensions += ['releasenotes']
except:
    pass

# --  recommonmark config ----------------
from recommonmark.transform import AutoStructify

extensions += ['sphinx_markdown_tables']

# --  latex config ----------------


latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '12pt',
    'pointsize': '10pt',
    # 'classoptions': ',english',
    'inputenc': '',
    'utf8extra': '',

    # Additional stuff for the LaTeX preamble.
    'preamble': '''
\usepackage{xeCJK}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
\setCJKmainfont[BoldFont=SimHei, ItalicFont=STKaiti]{SimSun}
\setCJKmonofont[Scale=0.9]{SimSun}
\setCJKfamilyfont{song}[BoldFont=SimSun]{SimSun}
\setCJKfamilyfont{sf}[BoldFont=SimSun]{SimSun}
'''
}

# --  planuml config ----------------
plantuml_theme = "azusa-color"
plantuml_jar_path = os.path.join(PROJECT_DIR, "plantuml.jar")
# plantuml = "java -jar " + "-Iplantuml_themes/{1}.pu {0}".format(plantuml_jar_path, plantuml_theme)
plantuml_output_format = "svg"
plantuml_latex_output_format = "eps"

# extensions += ['sphinxcontrib.SphinxRest', ]
# rest_api_source_root = os.path.join(PROJECT_DIR, "_static", "apis")
# rest_api_domain = "http://odc.alibaba.net"
# rest_api_http_request_example_title = "Request Example"
# rest_api_http_response_example_title = "Response Example"

extensions += ['plantweb.directive', ]


def maybe_skip_member(app, what, name, obj, skip, options):
    print(app, what, name, obj, skip, options)
    if name in ['debug_value', "get_json_object"]:
        return True


# xx


# language = 'de'
# language = 'tr'
# PROJECT


# theme

from better import better_theme_path

html_theme_path = [better_theme_path]
html_theme = 'better'

extensions += ['sphinx_sitemap']
html_baseurl = 'http://timger.com.cn/docs/blog/'


def setup(app):
    app.add_config_value(
        'recommonmark_config', {
            # 'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            'enable_eval_rst': True,
            'enable_math': True,
            'enable_inline_math': True,
            'enable_auto_doc_ref': True,
        }, True)
    app.add_stylesheet('https://timger-blog.oss-cn-beijing.aliyuncs.com/default.css')
    app.add_javascript('https://timger-blog.oss-cn-beijing.aliyuncs.com/gitment.browser.js.1.js')
    app.add_javascript('https://timger-blog.oss-cn-beijing.aliyuncs.com/fix.js')
    app.add_stylesheet('https://timger-blog.oss-cn-beijing.aliyuncs.com/fix.css')