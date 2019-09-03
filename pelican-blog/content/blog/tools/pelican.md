Title: Write blog with pelican
Date: 2019-09-03 20:00
Category: tool
Tags: python, pelican, tool
Summary: use pelican writer you blog

# 背景

很早前了解pelican。一直也没有认真写啊一博客,
博客搬家又搬家,跟我毅力有关.我承认自己是一个没有毅力的人.也跟文笔不行有关,
我总喜欢简单说明.不喜欢长篇大论. 最近因为公司团队的气氛,我学习了一些关于细节的思考.
我觉得有必要把对于细节的思考记录下来,又开始弄了下博客,

我承认我是一个爱瞎折腾的人,也没折腾出啥名堂.希望这次能够坚持.

前段时间迷上了`sphinx` 基于 sphinx 做了个静态博客,但是主题和功能还是不如pelican来的丰富
还是切到pelican上,顺便仔细看了下pelican的文档我觉得还是改到pelican来比较好,
当然之前的研究还是有用的, 基于 github 的评论部分还是可以延续下去

## 简介

pelican当前用的版本是 4.4.1 
你如果看 [pelican](https://github.com/getpelican/pelican) 的仓库,严格来说,代码不算多.

![](/docs/blog/static/15675262963787.jpg)

主要基于jinja模板做了变量渲染相关,以及rst 和 markdown 的解析.


Pelican is a static site generator, written in Python.

1. Write content in reStructuredText or Markdown using your editor of choice
2. Includes a simple command line tool to (re)generate site files
3. Easy to interface with version control systems and web hooks
4. Completely static output is simple to host anywhere

Features
Pelican currently supports:

1. Chronological content (e.g., articles, blog posts) as well as static pages
2. Integration with external services (e.g., Google Analytics and Disqus)
3. Site themes (created using Jinja2 templates)
4. Publication of articles in multiple languages
5. Generation of Atom and RSS feeds
6. Syntax highlighting via Pygments
7. Importing existing content from WordPress, Dotclear, and other services
8. Fast rebuild times due to content caching and selective output writing
9. Check out Pelican's documentation for further information.

# 用法

用法整体文档 在 [4.4.1](http://docs.getpelican.com/en/4.1.1/quickstart.html)

## 生成

```bash
pip install pelican markdown
mkdir -p ~/projects/yoursite
cd ~/projects/yoursite
pelican-quickstart
```

然后就可以改配置文件了

## 配置

配置主要包含:

1. 文件路径的规则
2. 各种文件的目录
3. 站点地图
4. 主题
5. 插件

具体可以参加官方文档,我就不细列了,下面是我的配置文件

```python
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
```

## 截图


![](/docs/blog/static/15675235665790.jpg)




https://docs.getpelican.com/en/4.1.1/content.html#internal-pygments-options

