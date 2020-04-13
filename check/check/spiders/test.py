import scrapy
import re
from scrapy.linkextractors import LinkExtractor
import pymongo


class web(scrapy.Spider):  # scrapy.Spider which provides a start_requests()
    name = 'test'
      # name of the Spider

    def __init__(self, filename=None):
        if filename:
            with open("ram.xml", 'r') as f:
                self.start_urls = f.readlines()

    def parse(self, response):              # response get the source code into response variable
        #links = response.css('a').extract()    # a is tag
        links = response.xpath("//a/@href").extract()
        print("__________________________++++++++++++++++++++++++++++++++++++")
        pass
        # we suppose to yield instead of return bcz behid the scene scrapy use generator
        yield {'link': links}
