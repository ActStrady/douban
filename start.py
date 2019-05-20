#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time : 2019/5/20 11:32
# @Author : ActStrady@tom.com
# @FileName : start.py
# @GitHub : https://github.com/ActStrady/douban
from scrapy import cmdline

cmdline.execute('scrapy crawl selenium_movies'.split())
