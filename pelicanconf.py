#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Steve Schwarz'
SITENAME = 'steve.agilitynerd.com'
SITEURL = 'http://127.0.0.1:8000'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# Blogroll
LINKS = ()

# Social widget
# SOCIAL = (('', '#'),)

DEFAULT_PAGINATION = 5

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

THEME = './themes/lesseridea'

SUMMARY_MAX_LENGTH = 30
