# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KararItem  (scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    application_number = scrapy.Field()
    application_title = scrapy.Field()
    application_date = scrapy.Field()
    deciding_unit = scrapy.Field()
    decision_result = scrapy.Field()
    official_gazette_no = scrapy.Field()
    have_press_releases = scrapy.Field()
    alleged_violation = scrapy.Field()
    right_liberty_at_stake = scrapy.Field()
    application_title = scrapy.Field()
    application_topic = scrapy.Field()
    accessed_timestamp = scrapy.Field()
    kunye = scrapy.Field()
    karar_text = scrapy.Field()
class KararBilgiFormuItem(scrapy.Item):
    result = scrapy.Field()
    solution = scrapy.Field()




