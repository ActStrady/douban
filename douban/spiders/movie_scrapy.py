#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time : 2019/5/20 9:28
# @Author : ActStrady@tom.com
# @FileName : movie_scrapy.py
# @GitHub : https://github.com/ActStrady/douban

"""
1. 豆瓣电影页面使用selenium + scrapy结合来实现
2. 直接请求后台服务器来实现
"""

from scrapy import Spider, Request
from douban.items import DoubanItem


class SeleniumMovies(Spider):
    """
    使用selenium + scrapy结合来实现
    """
    # 爬虫名
    name = 'selenium_movies'

    # 初始请求
    def start_requests(self):
        url = 'https://movie.douban.com/explore#' \
              '!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
        yield Request(url)

    # 默认的解析函数
    def parse(self, response):
        movie_list = response.xpath("//div[@class='list']/a[@class='item']")
        item = DoubanItem()
        for movie in movie_list:
            name = movie.xpath("./p/text()").extract_first().strip()
            item['name'] = name
            grade = movie.xpath("./p/strong/text()").extract_first().strip()
            item['grade'] = grade
            image_url = movie.xpath("./div/img/@src").extract_first().strip()
            item['image_url'] = image_url
            yield item
