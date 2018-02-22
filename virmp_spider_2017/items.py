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

def yes_or_no(answer_array):
    # print(answer_array)
    if len(answer_array) != 2:
        return "Error"
    
    # If first item (yes) is "-blank", then return "No primary case responsibility"
    if answer_array[0]:
        return "No"
    else:
        return "Yes"

def checked(checkmark):
    # print(checkmark)
    # If '' then it matched with "checkmark.gif" which is yes
    if (checkmark == 'checkmark'):
        return "Yes"
    elif (checkmark == 'checkmark-blank'):
        return "No"
    else:
        return "Error"

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

    # Clinical Experience and Responsibilities
    first_opinion = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    primary_surgeon = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    complex_cases = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    daily_patient_rounds = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    direct_supervision_percentage = scrapy.Field(output_processor=TakeFirst())

    # Didactic training
    weekly_teaching_rounds = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    presentation = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    professional_meeting_opportunity = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    financial_support_for_meeting = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    publication_requirement = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    
    # Facilities
    current_medical_textbooks = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    computer_with_internet = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    search_engines = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    icu = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())

    # Equipment
    arthroscopy = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    basic_clinical_laboratory_equipment= scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    blood_gas_analysis = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    blood_pressure_monitoring = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    bone_plating_equipment = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    ct_scan = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    diagnostic_laboratory = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    digital_radiography = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    echocardiography = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    electrocardiography = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    endoscopy = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    laparoscopy = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    mri = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    nuclear_medicine = scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    physical_therapy_equipment= scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())
    ultrasound= scrapy.Field(input_processor=Compose(TakeFirst(), checked), output_processor=TakeFirst())

    # Scheduling
    daytime_primary_emergency = scrapy.Field(output_processor=TakeFirst())
    overnight_primary_emergency = scrapy.Field(output_processor=TakeFirst())
    first_opinion_clinics = scrapy.Field(output_processor=TakeFirst())
    elective_time = scrapy.Field(output_processor=TakeFirst())
    satellite_clinic = scrapy.Field(output_processor=TakeFirst())

    # Orientation/Supervision/Mentoring
    formal_orientation_required = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    vet_mentor = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    written_evals = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())
    orientation_manual = scrapy.Field(input_processor=Compose(yes_or_no), output_processor=TakeFirst())



# clean_text = Compose(MapCompose(lambda v: v.strip()), Join())
# clean_text = TakeFirst()
# to_int = Compose(TakeFirst(), int)

# class ProgramDetailLoader(ItemLoader):
#     default_item_class = ProgramDetailItem
#     program_categories_in = 
