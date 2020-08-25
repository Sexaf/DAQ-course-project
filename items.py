import scrapy

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    serial_number = scrapy.Field()
    movie_name = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()
    evaluate = scrapy.Field()
    describe = scrapy.Field()
