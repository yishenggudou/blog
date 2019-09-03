#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

"""
http://docs.getpelican.com/en/4.1.1/settings.html
https://docs.getpelican.com/en/4.1.1/settings.html
https://raw.githubusercontent.com/getpelican/pelican/master/samples/pelican.conf.py
"""
AUTHOR = u'timger'
SITENAME = u'\u6765\u4e16\u505a\u674e\u767d'
SITEURL = ''
FEED_DOMAIN = SITEURL

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']
PAGE_EXCLUDES = []
OUTPUT_SOURCES = False
OUTPUT_SOURCES_EXTENSION = '.text'
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

DEFAULT_CATEGORY = u'默认'

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

DOCUTILS_SETTINGS = {}

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_DOMAIN = "/docs/blog/"
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
    ('about this blog', '/docs/blog/category/pages/about-this-blog.html'),

)

# Social widget
SOCIAL = (
    ('weibo', 'https://weibo.com/zhanghaibo'),
    ('twitter', 'https://twitter.com/yishenggudou'),
    ('youtube', 'https://www.youtube.com/channel/UC-JrBqbEaj6fxZ7uIVs8GjA?view_as=subscriber'),
    ('facebook', 'https://www.facebook.com/yishenggudou'),
    ('segmentfault', 'https://segmentfault.com/u/timger'),
    ('zhihu', 'https://www.zhihu.com/people/timger')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = 'theme'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['pelican-ipynb.markup', 'assets', 'sitemap', 'gravatar', 'tag_cloud']

SITEMAP = {
    'exclude': ['tag/', 'category/'],
    'format': 'xml'
}

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored.
IGNORE_FILES = [".ipynb_checkpoints"]

# jinja2
JINJA_ENVIRONMENT = {'trim_blocks': True, 'lstrip_blocks': True}
# JINJA_FILTERS = {'urlencode': urlencode_filter}

# markdown
# https://python-markdown.github.io/reference/#markdown
# http://jwarby.github.io/jekyll-pygments-themes/languages/javascript.html
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'noclasses': False,
            'css_class': 'highlight ',
            'pygments_style': {

            },
            'use_pygments': True,
            'linenums': True},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

#
PYGMENTS_RST_OPTIONS = {
    'classprefix': 'pgcss',
    'linenos': 'table'
}
