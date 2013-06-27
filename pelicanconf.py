#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jin Zhang'
SITENAME = u'Jin Zhang'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Github', 'http://github.com/jinzhangg'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-svbtle'

# AUTHOR_BIO = 'Python, Django, Flask Developer'
AUTHOR_BIO = 'Site under construction'
SUMMARY_MAX_LENGTH = 100

FILES_TO_COPY = (('CNAME', 'CNAME'),)

ARTICLE_URL = 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'
