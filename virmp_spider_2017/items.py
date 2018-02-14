# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, MapCompose, Join, TakeFirst

class ProgramDetailItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    total_annual_cases = scrapy.Field(output_processor=TakeFirst())
    avg_daily_cases = scrapy.Field(output_processor=TakeFirst())
    avg_daily_outpatient_cases = scrapy.Field(output_processor=TakeFirst())
    avg_daily_inpatient_cases = scrapy.Field(output_processor=TakeFirst())
    avg_daily_surgeries = scrapy.Field(output_processor=TakeFirst())
    avg_daily_ER_cases = scrapy.Field(output_processor=TakeFirst())

# clean_text = Compose(MapCompose(lambda v: v.strip()), Join())
# clean_text = TakeFirst()
# to_int = Compose(TakeFirst(), int)

# class ProgramDetailLoader(ItemLoader):
#     default_item_class = ProgramDetailItem
#     name = clean_text
#     total_annual_cases = to_int
#     avg_daily_cases = to_int
#     avg_daily_outpatient_cases = to_int
#     avg_daily_inpatient_cases = to_int
#     avg_daily_surgeries = to_int
#     avg_daily_ER_cases = to_int
