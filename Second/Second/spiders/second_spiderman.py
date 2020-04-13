import scrapy
import re
from scrapy.linkextractors import LinkExtractor


class web(scrapy.Spider):
    name = 'second_spiderman'  # name of the Spider
    start_urls = [                     # these 2 parameter should always remain same
        'https://deepweblinks.net/email-services/'
        'https://onion.live'
    ]

    def parse_item(self, response):
        questions = response.xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            yield item
