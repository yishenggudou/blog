#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

"""
http://docs.getpelican.com/en/3.6.3/settings.html
https://docs.getpelican.com/en/3.1.1/settings.html
"""
AUTHOR = u'timger'
SITENAME = u'\u6765\u4e16\u505a\u674e\u767d'
SITEURL = ''
FEED_DOMAIN = SITEURL

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']
PAGE_EXCLUDES = []
OUTPUT_SOURCES = True
OUTPUT_SOURCES_EXTENSION = '.text'

DEFAULT_CATEGORY = u'默认'

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

DOCUTILS_SETTINGS = {}

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = ('feeds/all.atom.xml')
CATEGORY_FEED_ATOM = ('feeds/{slug}.atom.xml')
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RELATIVE_URLS = True

# Blogroll
LINKS = (
    # ('Pelican', 'http://getpelican.com/'),
    # ('Python.org', 'http://python.org/'),
    # ('Jinja2', 'http://jinja.pocoo.org/'),

)

# Social widget
SOCIAL = (('sina', 'https://weibo.com/zhanghaibo'),
          ('twitter', 'https://twitter.com/yishenggudou'),
          ('youtube', 'https://www.youtube.com/channel/UC-JrBqbEaj6fxZ7uIVs8GjA?view_as=subscriber'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = 'pelican-blueidea'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored.
IGNORE_FILES = [".ipynb_checkpoints"]

# jinja2
JINJA_ENVIRONMENT = {'trim_blocks': True, 'lstrip_blocks': True}
# JINJA_FILTERS = {'urlencode': urlencode_filter}

# markdown

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
