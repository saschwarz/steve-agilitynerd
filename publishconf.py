#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://steve.agilitynerd.com'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/all.rss'

DISQUS_SITENAME = "steveagilitynerd"
