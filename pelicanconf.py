#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
THEME = 'theme'
AUTHOR = 'rafi59'
SITENAME = 'Blog de rafi59'
SITEURL = ''
STATIC_PATHS = ['images']
PIWIK_ID = '1'
PIWIK_URL = 'stats.rafi59.codelib.re/'
GITHUB_URL = 'github.com/Rafi594'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
