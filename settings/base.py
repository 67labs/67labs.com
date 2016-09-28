#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

AUTHOR = u'67 Labs Collective'
SITENAME = u'67labs.com'
SITEURL = ''

PATH = os.path.join(ROOT_PATH, 'content')
THEME = os.path.join(ROOT_PATH, 'pelican-svbhack')
OUTPUT_PATH = os.path.join(ROOT_PATH, 'html')

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Blog', '/blog/'),
    ('About Us', '/pages/about-us.html'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
