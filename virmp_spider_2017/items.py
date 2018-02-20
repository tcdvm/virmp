# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, MapCompose, Join, TakeFirst

def process_address(address_lines):
    new_lines = []
    for line in address_lines:
        line = line.replace('<br>', ', ')
        new_lines.append(line)
    return ", ".join(new_lines)

def strip_filter(category):
    stripped = category.strip()
    if stripped:
        return stripped
    else:
        return None

def strip_comma(number):
    return number.strip().replace(',', '')

def strip_comma_tofloat(salary):
    stripped = salary.strip()
    stripped = stripped.replace(',', '')
    return float(stripped)

class ProgramDetailItem(scrapy.Item):
    # Define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    # Program Details URL
    program_details_url = scrapy.Field(output_processor=TakeFirst())
    # Address & contact info
    address = scrapy.Field(output_processor=Compose(process_address))
    phone = scrapy.Field(output_processor=TakeFirst())
    fax = scrapy.Field(output_processor=TakeFirst())
    contact = scrapy.Field(output_processor=TakeFirst())
    contact_email = scrapy.Field(output_processor=TakeFirst())
    # Caseload - don't convert to floats - do that in python to calculate averages
    total_annual_cases = scrapy.Field(output_processor=Compose(TakeFirst(), strip_comma))
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
    # Registered/Licensed/Certified Veterinary Technicians
    tech_direct_support = scrapy.Field(output_processor=TakeFirst())
    tech_assigned_to_ER = scrapy.Field(output_processor=TakeFirst())
    tech_assigned_to_ICU = scrapy.Field(output_processor=TakeFirst())
    # Outcomes assessment
    avg_num_interns_started_past_5_years = scrapy.Field(output_processor=TakeFirst())
    avg_num_interns_completed_past_5_years = scrapy.Field(output_processor=TakeFirst())
    num_interns_applied_residency_past_5_years = scrapy.Field(output_processor=TakeFirst())
    num_interns_accepted_residency_past_5_years = scrapy.Field(output_processor=TakeFirst())
    # Diplomate Table
    ABVP_FT = scrapy.Field(output_processor=TakeFirst())
    ABVP_PT = scrapy.Field(output_processor=TakeFirst())
    ABVT_FT = scrapy.Field(output_processor=TakeFirst())
    ABVT_PT = scrapy.Field(output_processor=TakeFirst())
    ACLAM_FT = scrapy.Field(output_processor=TakeFirst())
    ACLAM_PT = scrapy.Field(output_processor=TakeFirst())
    ACPV_FT = scrapy.Field(output_processor=TakeFirst())
    ACPV_PT = scrapy.Field(output_processor=TakeFirst())
    ACT_FT = scrapy.Field(output_processor=TakeFirst())
    ACT_PT = scrapy.Field(output_processor=TakeFirst())
    ACVAA_FT = scrapy.Field(output_processor=TakeFirst())
    ACVAA_PT = scrapy.Field(output_processor=TakeFirst())
    ACVB_FT = scrapy.Field(output_processor=TakeFirst())
    ACVB_PT = scrapy.Field(output_processor=TakeFirst())
    ACVCP_FT = scrapy.Field(output_processor=TakeFirst())
    ACVCP_PT = scrapy.Field(output_processor=TakeFirst())
    ACVD_FT = scrapy.Field(output_processor=TakeFirst())
    ACVD_PT = scrapy.Field(output_processor=TakeFirst())
    ACVECC_FT = scrapy.Field(output_processor=TakeFirst())
    ACVECC_PT = scrapy.Field(output_processor=TakeFirst())
    ACVIM_CARD_FT = scrapy.Field(output_processor=TakeFirst())
    ACVIM_CARD_PT = scrapy.Field(output_processor=TakeFirst())
    ACVIM_INTMET_FT = scrapy.Field(output_processor=TakeFirst())
    ACVIM_INTMET_PT = scrapy.Field(output_processor=TakeFirst())
    ACVIM_LA_FT = scrapy.Field(output_processor=TakeFirst())
    ACVIM_LA_PT = scrapy.Field(output_processor=TakeFirst())
    ACVIM_NEUR_FT = scrapy.Field(output_processor=TakeFirst())
    ACVIM_NEUR_PT = scrapy.Field(output_processor=TakeFirst())
    ACVIM_ONC_FT = scrapy.Field(output_processor=TakeFirst())
    ACVIM_ONC_PT = scrapy.Field(output_processor=TakeFirst())
    ACVM_FT = scrapy.Field(output_processor=TakeFirst())
    ACVM_PT = scrapy.Field(output_processor=TakeFirst())
    ACVN_FT = scrapy.Field(output_processor=TakeFirst())
    ACVN_PT = scrapy.Field(output_processor=TakeFirst())
    ACVO_FT = scrapy.Field(output_processor=TakeFirst())
    ACVO_PT = scrapy.Field(output_processor=TakeFirst())
    ACVP_FT = scrapy.Field(output_processor=TakeFirst())
    ACVP_PT = scrapy.Field(output_processor=TakeFirst())
    ACVPM_FT = scrapy.Field(output_processor=TakeFirst())
    ACVPM_PT = scrapy.Field(output_processor=TakeFirst())
    ACVR_FT = scrapy.Field(output_processor=TakeFirst())
    ACVR_PT = scrapy.Field(output_processor=TakeFirst())
    ACVR_ONC_FT = scrapy.Field(output_processor=TakeFirst())
    ACVR_ONC_PT = scrapy.Field(output_processor=TakeFirst())
    ACVS_FT = scrapy.Field(output_processor=TakeFirst())
    ACVS_PT = scrapy.Field(output_processor=TakeFirst())
    ACVSMR_FT = scrapy.Field(output_processor=TakeFirst())
    ACVSMR_PT = scrapy.Field(output_processor=TakeFirst())
    ACZM_FT = scrapy.Field(output_processor=TakeFirst())
    ACZM_PT = scrapy.Field(output_processor=TakeFirst())
    AVDC_FT = scrapy.Field(output_processor=TakeFirst())
    AVDC_PT = scrapy.Field(output_processor=TakeFirst())

# clean_text = Compose(MapCompose(lambda v: v.strip()), Join())
# clean_text = TakeFirst()
# to_int = Compose(TakeFirst(), int)

# class ProgramDetailLoader(ItemLoader):
#     default_item_class = ProgramDetailItem
#     program_categories_in = 
