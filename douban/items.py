# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    name = scrapy.Field()
    # 评分
    grade = scrapy.Field()
    image_url = scrapy.Field()
    # 下载图片
    images = scrapy.Field()
    image_urls = scrapy.Field()
