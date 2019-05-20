# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class DoubanPipeline(object):
    def __init__(self):
        # 获取连接
        self.db_client = pymongo.MongoClient('192.168.127.81')
        # 创建数据库
        self.db = self.db_client['douban']
        # 创建集合
        self.db_collection = self.db['movies']

    def open_spider(self, spider):
        # 清空集合
        self.db_collection.remove({})

    def process_item(self, item, spider):
        # 插入一个文档
        self.db_collection.insert_one(dict(item))
        return item

    # 关闭连接
    def close_spider(self, spider):
        self.db_client.close()


class DoubanImagesPipeline(ImagesPipeline):
    # 生成下载图片的request
    def get_media_requests(self, item, info):
        return [Request(x) for x in item.get(self.images_urls_field, [])]

    # 指定文件名
    def file_path(self, request, response=None, info=None):
        # 图片名
        image_name = request.url.split("/")[-1]
        # 文件名
        return '/movie/%s' % image_name
