# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QtItem(scrapy.Item):
    ttname = scrapy.Field()
    ttprice = scrapy.Field()
    ttsqft = scrapy.Field()
    ttbhk = scrapy.Field()
