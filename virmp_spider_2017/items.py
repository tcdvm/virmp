# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, MapCompose, Join, TakeFirst

def strip_filter(category):
    stripped = category.strip()
    if stripped:
        return stripped
    else:
        return None

def strip_comma_tofloat(salary):
    stripped = salary.strip()
    stripped = stripped.replace(',', '')
    return float(stripped)

class ProgramDetailItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    # Caseload - don't convert to floats - do that in python to calculate averages
    total_annual_cases = scrapy.Field(output_processor=TakeFirst())
    avg_daily_cases = scrapy.Field(output_processor=TakeFirst())
    avg_daily_outpatient_cases = scrapy.Field(output_processor=TakeFirst())
    avg_daily_inpatient_cases = scrapy.Field(output_processor=TakeFirst())
    avg_daily_surgeries = scrapy.Field(output_processor=TakeFirst())
    avg_daily_ER_cases = scrapy.Field(output_processor=TakeFirst())
    # Number of positions
    number_of_positions  = scrapy.Field(output_processor=TakeFirst())
    # Program categories
    program_categories = scrapy.Field(input_processor=MapCompose(strip_filter))
    # Salaries
    salary = scrapy.Field(input_processor=Compose(TakeFirst(), strip_comma_tofloat), output_processor=TakeFirst())
    # Number of faculty & residents (2 separate numbers in same <p>)
    faculty_support = scrapy.Field(output_processor=TakeFirst())
    resident_support = scrapy.Field(output_processor=TakeFirst())

# clean_text = Compose(MapCompose(lambda v: v.strip()), Join())
# clean_text = TakeFirst()
# to_int = Compose(TakeFirst(), int)

# class ProgramDetailLoader(ItemLoader):
#     default_item_class = ProgramDetailItem
#     program_categories_in = 
