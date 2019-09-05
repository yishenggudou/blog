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
SITEURL = '/docs/blog/'
FEED_DOMAIN = SITEURL

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']
PAGE_EXCLUDES = []
OUTPUT_SOURCES = False
OUTPUT_SOURCES_EXTENSION = '.text'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
# ARTICLE_URL 为模板中的路径
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
# ARTICLE_SAVE_AS 为保存文件的路径, 需要和上面一致
PAGE_URL = 'pages/{slug}'
# 页面的访问路径
PAGE_SAVE_AS = 'pages/{slug}/index.html'
# 页面实际生产的路径

DEFAULT_CATEGORY = u'默认'

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

DOCUTILS_SETTINGS = {}

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_DOMAIN = "http://timger.com.cn/docs/blog/"
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
    ('linux-v011-learn', 'https://linux-v011-learn.readthedocs.io/zh_CN/latest/'),
    ('pyvm', 'https://pyvm.readthedocs.io/zh_CN/latest/'),
    ('scala-design-patterns', 'https://scala-design-patterns.readthedocs.io/zh_CN/latest/'),
    ('cython-algorithms', 'https://cython-algorithms.readthedocs.io/zh_CN/latest/'),
    ('npms', 'https://www.npmjs.com/settings/yishenggudou/packages'),
    ('pypi', 'https://pypi.org/user/haibo.zhang/'),
    ('maven', 'https://mvnrepository.com/artifact/com.github.yishenggudou'),
    ('travis-ci', 'https://travis-ci.org/yishenggudou')
)
# 会在底部出现

# Social widget
SOCIAL = (
    ('weibo', 'https://weibo.com/zhanghaibo'),
    ('twitter', 'https://twitter.com/yishenggudou'),
    ('youtube', 'https://www.youtube.com/channel/UC-JrBqbEaj6fxZ7uIVs8GjA?view_as=subscriber'),
    ('facebook', 'https://www.facebook.com/yishenggudou'),
    ('segmentfault', 'https://segmentfault.com/u/timger'),
    ('zhihu', 'https://www.zhihu.com/people/timger')
)

# 社交账号

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = 'theme'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['pelican-ipynb.markup', 'assets', 'sitemap', 'gravatar', 'tag_cloud', 'render_math']

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
import hashlib

JINJA_FILTERS = {
    'md5': lambda x: hashlib.md5(x.encode('utf-8')).hexdigest()
}
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

# static
SITEURL = "http://timger.com.cn/docs/blog/"
STATIC_PATHS = ['static', 'docs', 'slides', 'pdfs', 'images']

#
DEFAULT_METADATA = {
    'status': 'draft',
}
