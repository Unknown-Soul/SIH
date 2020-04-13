# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
# connecting mongodb


class SecondPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)

        db = self.conn['mydb']  # creting db
        self.collection = db['link_tb'] # creting table

    def process_item(self, item, spider):
        self.collection.insert(item)  # insert data
        return item
