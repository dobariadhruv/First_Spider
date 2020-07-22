# import scrapy
# class qt_spider(scrapy.spider):
from scrapy.spiders import Spider
from ..items import QtItem


class QuoteSpider(Spider):
    name = 'acres'
    start_urls = ['any_url']

    def parse(self, response):
        items = QtItem()

        all_div_names = response.xpath('//article')

        for bks in all_div_names:
            name = bks.xpath('//span[@class="css-fwbz9r"]/text()').extract()
            price = bks.xpath('//h2[@class="css-yr18fa"]/text()').extract()
            sqft = bks.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "css-ebj250", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "css-1ty8tu4", " " ))]/text()').extract()
            bhk = bks.xpath('//a[@class="css-163eyf0"]/text()').extract()

            items['ttname'] = name
            items['ttprice'] = price
            items['ttsqft'] = sqft
            items['ttbhk'] = bhk

        yield items
