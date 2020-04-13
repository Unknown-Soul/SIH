import scrapy
import re
from scrapy.linkextractors import LinkExtractor


class web(scrapy.Spider):   #scrapy.Spider which provides a start_requests()
    name = 'quotes'  # name of the Spider
    start_urls = [                     # these 2 parameter should always remain same
        # 'https://deepweblinks.net/email-services/'
        # 'https://onion.live',
        # 'https://www.deeponionweb.com/onion-live/',
        # 'https://darkweblink.com/',
        # 'https://www.reddit.com/r/onions/'
        'http://bitmailendavkbec.onion/',
        'http://torbox3uiot6wchz.onion/',
        'http://protonirockerxow.onion/'
    ]

    def parse(self, response):              # response get the source code into response variable
        # links = response.css('a').extract()    # a is tag
        #links = response.xpath("//a/@href").extract()

        # we suppose to yield instead of return bcz behid the scene scrapy use generator
        # yield {'link': links}


#second way
        links = LinkExtractor(canonicalize=True,).extract_links(response)
        regex = re.compile(r"^https?\:\/\/[\w\-\.]+\.onion")
        for i in links:
            if regex.match(i.url):
                print i.url
                yield {'link': i.url}

# https://www.data-blogger.com/2016/08/18/scraping-a-website-with-python-scrapy/
# http://doc.scrapy.org/en/latest/topics/link-extractors.html
