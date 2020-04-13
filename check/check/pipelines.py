# -*- coding: utf-8 -*-

# Define your item pipelines here

import pymongo
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CheckPipeline(object):

    def process_item(self, item, spider):
        return item
