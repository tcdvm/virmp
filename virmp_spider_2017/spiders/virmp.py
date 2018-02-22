#-*- coding: utf-8 -*-
import logging
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from virmp_spider_2017.items import ProgramDetailItem


class VirmpSpider(scrapy.Spider):
    name = 'virmp'
    allowed_domains = ['www.virmp.org']
    start_urls = ['https://www.virmp.org/Program/List?categoryIDs=12&institution=&stateID=']

    def parse(self, response):
        # self.logger.info('hi')
        self.logger.info(response.xpath('//title').extract())
        # self.logger.info(response.xpath('//strong').extract_first())
        for url in response.xpath('//table[@id="searchtable"]/*/td[2]/a/@href').extract():
            detailpage = response.urljoin(url)
            yield scrapy.Request(detailpage, callback=self.parseDetails)

        # next_page_url = response.xpath("//a[contains(text(), '>')]/@href").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
    
    def parseDetails(self, response):
        self.logger.info("\n============" + response.xpath('//strong/text()').extract_first() + "===============")

        # Initialize loader
        loader = ItemLoader(item=ProgramDetailItem(), response=response)

        # Get name of place
        loader.add_xpath('name', '//strong/text()')

        # Program Details URL
        loader.add_value('program_details_url', response.url)

        # Get addresses, phone numbers
        loader.add_css('address', 'p.addressblock', re=r'</strong><br>(.*)<br>(United States|Canada)')
        loader.add_css('phone', 'p.addressblock', re=r'.*<br>(.*)\s+\(V\)')
        loader.add_css('fax', 'p.addressblock', re=r'.*<br>(.*)\s+\(F\)')

        # Get number of positions
        loader.add_xpath('number_of_positions', '//*[contains(text(),"Position")]/text()')

        # Get program categories (to exclude any internship that is multi-category)
        loader.add_xpath('program_categories', '//p[contains(.,"Program Categories")]/text()')

        # Program Contact
        loader.add_xpath('contact', '//p[contains(.,"Authorized Administrative Official")]/text()[1]')
        loader.add_xpath('contact_email', '//a[contains(.,"(email)")]/@href', re=r'mailto:(.*)')

        # Get Salary
        loader.add_xpath('salary', '//p[contains(.,"Salary")]/text()', re=r"(\d+,?\d+)")

        # Get caseload info
        loader.add_xpath('total_annual_cases', '//table[@id="caseload"]/tr[2]/td[1]/text()')
        loader.add_xpath('avg_daily_cases', '//table[@id="caseload"]/tr[2]/td[2]/text()')
        loader.add_xpath('avg_daily_outpatient_cases', '//table[@id="caseload"]/tr[2]/td[3]/text()')
        loader.add_xpath('avg_daily_inpatient_cases', '//table[@id="caseload"]/tr[2]/td[4]/text()')
        loader.add_xpath('avg_daily_surgeries', '//table[@id="caseload"]/tr[2]/td[5]/text()')
        loader.add_xpath('avg_daily_ER_cases', '//table[@id="caseload"]/tr[2]/td[6]/text()')

        # Get faculty and residents in direct support of program
        loader.add_xpath('faculty_support', '//p[contains(.,"Number of Faculty/Clinicians in Direct Support of Program")]/text()[1]', re=r'(\d+)') 
        loader.add_xpath('resident_support', '//p[contains(.,"Number of Faculty/Clinicians in Direct Support of Program")]/text()[3]', re=r'(\d+)') 

        # Get Diplomates Table
        loader.add_xpath('ABVP_PT', '//table[@id="diplomatetable"]/tr[2]/td[2]/text()')
        loader.add_xpath('ABVP_FT', '//table[@id="diplomatetable"]/tr[2]/td[3]/text()')
        loader.add_xpath('ABVT_FT', '//table[@id="diplomatetable"]/tr[2]/td[5]/text()')
        loader.add_xpath('ABVT_PT', '//table[@id="diplomatetable"]/tr[2]/td[6]/text()')
        loader.add_xpath('ACLAM_FT', '//table[@id="diplomatetable"]/tr[3]/td[2]/text()')
        loader.add_xpath('ACLAM_PT', '//table[@id="diplomatetable"]/tr[3]/td[3]/text()')
        loader.add_xpath('ACPV_FT', '//table[@id="diplomatetable"]/tr[3]/td[5]/text()')
        loader.add_xpath('ACPV_PT', '//table[@id="diplomatetable"]/tr[3]/td[6]/text()')
        loader.add_xpath('ACT_FT', '//table[@id="diplomatetable"]/tr[4]/td[2]/text()')
        loader.add_xpath('ACT_PT', '//table[@id="diplomatetable"]/tr[4]/td[3]/text()')
        loader.add_xpath('ACVAA_FT', '//table[@id="diplomatetable"]/tr[4]/td[5]/text()')
        loader.add_xpath('ACVAA_PT', '//table[@id="diplomatetable"]/tr[4]/td[6]/text()')
        loader.add_xpath('ACVB_FT', '//table[@id="diplomatetable"]/tr[5]/td[2]/text()')
        loader.add_xpath('ACVB_PT', '//table[@id="diplomatetable"]/tr[5]/td[3]/text()')
        loader.add_xpath('ACVCP_FT', '//table[@id="diplomatetable"]/tr[5]/td[5]/text()')
        loader.add_xpath('ACVCP_PT', '//table[@id="diplomatetable"]/tr[5]/td[6]/text()')
        loader.add_xpath('ACVD_FT', '//table[@id="diplomatetable"]/tr[6]/td[2]/text()')
        loader.add_xpath('ACVD_PT', '//table[@id="diplomatetable"]/tr[6]/td[3]/text()')
        loader.add_xpath('ACVECC_FT', '//table[@id="diplomatetable"]/tr[6]/td[5]/text()')
        loader.add_xpath('ACVECC_PT', '//table[@id="diplomatetable"]/tr[6]/td[6]/text()')
        loader.add_xpath('ACVIM_CARD_FT', '//table[@id="diplomatetable"]/tr[7]/td[2]/text()')
        loader.add_xpath('ACVIM_CARD_PT', '//table[@id="diplomatetable"]/tr[7]/td[3]/text()')
        loader.add_xpath('ACVIM_INTMET_FT', '//table[@id="diplomatetable"]/tr[7]/td[5]/text()')
        loader.add_xpath('ACVIM_INTMET_PT', '//table[@id="diplomatetable"]/tr[7]/td[6]/text()')
        loader.add_xpath('ACVIM_LA_FT', '//table[@id="diplomatetable"]/tr[8]/td[2]/text()')
        loader.add_xpath('ACVIM_LA_PT', '//table[@id="diplomatetable"]/tr[8]/td[3]/text()')
        loader.add_xpath('ACVIM_NEUR_FT', '//table[@id="diplomatetable"]/tr[8]/td[5]/text()')
        loader.add_xpath('ACVIM_NEUR_PT', '//table[@id="diplomatetable"]/tr[8]/td[6]/text()')
        loader.add_xpath('ACVIM_ONC_FT', '//table[@id="diplomatetable"]/tr[9]/td[2]/text()')
        loader.add_xpath('ACVIM_ONC_PT', '//table[@id="diplomatetable"]/tr[9]/td[3]/text()')
        loader.add_xpath('ACVM_FT', '//table[@id="diplomatetable"]/tr[9]/td[5]/text()')
        loader.add_xpath('ACVM_PT', '//table[@id="diplomatetable"]/tr[9]/td[6]/text()')
        loader.add_xpath('ACVN_FT', '//table[@id="diplomatetable"]/tr[10]/td[2]/text()')
        loader.add_xpath('ACVN_PT', '//table[@id="diplomatetable"]/tr[10]/td[3]/text()')
        loader.add_xpath('ACVO_FT', '//table[@id="diplomatetable"]/tr[10]/td[5]/text()')
        loader.add_xpath('ACVO_PT', '//table[@id="diplomatetable"]/tr[10]/td[6]/text()')
        loader.add_xpath('ACVP_FT', '//table[@id="diplomatetable"]/tr[11]/td[2]/text()')
        loader.add_xpath('ACVP_PT', '//table[@id="diplomatetable"]/tr[11]/td[3]/text()')
        loader.add_xpath('ACVPM_FT', '//table[@id="diplomatetable"]/tr[11]/td[5]/text()')
        loader.add_xpath('ACVPM_PT', '//table[@id="diplomatetable"]/tr[11]/td[6]/text()')
        loader.add_xpath('ACVR_FT', '//table[@id="diplomatetable"]/tr[12]/td[2]/text()')
        loader.add_xpath('ACVR_PT', '//table[@id="diplomatetable"]/tr[12]/td[3]/text()')
        loader.add_xpath('ACVR_ONC_FT', '//table[@id="diplomatetable"]/tr[12]/td[5]/text()')
        loader.add_xpath('ACVR_ONC_PT', '//table[@id="diplomatetable"]/tr[12]/td[6]/text()')
        loader.add_xpath('ACVS_FT', '//table[@id="diplomatetable"]/tr[13]/td[2]/text()')
        loader.add_xpath('ACVS_PT', '//table[@id="diplomatetable"]/tr[13]/td[3]/text()')
        loader.add_xpath('ACVSMR_FT', '//table[@id="diplomatetable"]/tr[13]/td[5]/text()')
        loader.add_xpath('ACVSMR_PT', '//table[@id="diplomatetable"]/tr[13]/td[6]/text()')
        loader.add_xpath('ACZM_FT', '//table[@id="diplomatetable"]/tr[14]/td[2]/text()')
        loader.add_xpath('ACZM_PT', '//table[@id="diplomatetable"]/tr[14]/td[3]/text()')
        loader.add_xpath('AVDC_FT', '//table[@id="diplomatetable"]/tr[14]/td[5]/text()')
        loader.add_xpath('AVDC_PT', '//table[@id="diplomatetable"]/tr[14]/td[6]/text()')

        # Get Registered/Licensed/Certified Veterinary Technicians
        loader.add_xpath('tech_direct_support', '//table[@id="vettech"]/tr[2]/td[1]/text()')
        loader.add_xpath('tech_assigned_to_ER', '//table[@id="vettech"]/tr[2]/td[2]/text()')
        loader.add_xpath('tech_assigned_to_ICU', '//table[@id="vettech"]/tr[2]/td[3]/text()')

        # Get Outcomes Assessment
        loader.add_xpath('avg_num_interns_started_past_5_years', '//p[contains(., "Average number of interns who started this program per year for the past 5 years:")]/text()', re=r'(\d+)$')
        loader.add_xpath('avg_num_interns_completed_past_5_years', '//p[contains(., "Average number of interns who completed this program per year for the past 5 years:")]/text()', re=r'(\d+)$')
        loader.add_xpath('num_interns_applied_residency_past_5_years', '//p[contains(.,"Number of interns from this program who applied for a residency in the past 5 years")]/text()', re=r'(\d+)$')
        loader.add_xpath('num_interns_accepted_residency_past_5_years', '//p[contains(.,"Number of interns from this program who accepted a residency in the past 5 years")]/text()', re=r'(\d+)$')

        # Clinical Experience and Responsibilities
        loader.add_xpath('first_opinion', '//li[contains(., "Does the intern have primary case care responsibility for first-opinion and emergency/critical care cases?")]/div/img', re=r'checkmark(.*).gif')
        loader.add_xpath('primary_surgeon', '//li[contains(., "Is the intern the primary surgeon on a broad range of elective and entry-level procedures?")]/div/img', re=r'checkmark(.*).gif')
        loader.add_xpath('complex_cases', '//li[contains(., "Does the intern have primary case care responsibility for complex cases with supervision by a boarded specialist?")]/div/img', re=r'checkmark(.*).gif')
        loader.add_xpath('daily_patient_rounds', '//li[contains(., "Are patient rounds held daily with a boarded specialist in attendance?")]/div/img', re=r'checkmark(.*).gif')
        loader.add_xpath('direct_supervision_percentage', '//li[contains(., "What is the percentage of time the intern will be directly supervised?")]', re='(\d+)%')

        # Didactic training
        loader.add_xpath('weekly_teaching_rounds', '//li[contains(.,"Are teaching rounds held weekly?")]/div/img', re=r'checkmark(.*).gif')
        loader.add_xpath('presentation', '//li[contains(.,"Does the intern deliver a professional presentation or seminar to senior clinicians and peers?")]/div/img', re=r'checkmark(.*).gif')
        loader.add_xpath('professional_meeting_opportunity', '//li[contains(.,"Does the intern have an opportunity to attend a professional meeting?")]/div/img', re=r'checkmark(.*).gif')
        loader.add_xpath('financial_support_for_meeting', '//li[contains(.,"Is financial support provided to attend a professional meeting?")]/div/img', re=r'checkmark(.*).gif')
        loader.add_xpath('publication_requirement', '//li[contains(.,"Is the intern required to complete/submit a publication?")]/div/img', re=r'checkmark(.*).gif')

        # Facilities
        loader.add_xpath('current_medical_textbooks', '//li[contains(.,"Does the intern have access to current medical textbooks?")]/div/img', re=r'checkmark(.*).gif') 
        loader.add_xpath('computer_with_internet', '//li[contains(.,"Is a computer with internet access provided?")]/div/img', re=r'checkmark(.*).gif') 
        loader.add_xpath('search_engines', '//li[contains(.,"Does the intern have access to search engines for scientific literature and online journals?")]/div/img', re=r'checkmark(.*).gif') 
        loader.add_xpath('icu', '//li[contains(.,"Does the primary hospital have an intensive care unit?")]/div/img', re=r'checkmark(.*).gif') 

        # Equipment
        loader.add_xpath('arthroscopy', '//ul/li[contains(., "Arthroscopy")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('basic_clinical_laboratory_equipment', '//ul/li[contains(., "Basic clinical laboratory equipment")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('blood_gas_analysis', '//ul/li[contains(., "Blood Gas Analysis")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('blood_pressure_monitoring', '//ul/li[contains(., "Blood Pressure Monitoring")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('bone_plating_equipment', '//ul/li[contains(., "Bone Plating Equipment")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('ct_scan', '//ul/li[contains(., "CT Scan")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('diagnostic_laboratory', '//ul/li[contains(., "Diagnostic Laboratory")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('digital_radiography', '//ul/li[contains(., "Digital Radiography")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('echocardiography' , '//ul/li[contains(., "Echocardiography")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('electrocardiography', '//ul/li[contains(., "Electrocardiography")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('endoscopy', '//ul/li[contains(., "Endoscopy")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('laparoscopy', '//ul/li[contains(., "Laparoscopy")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('mri', '//ul/li[contains(., "MRI")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('nuclear_medicine', '//ul/li[contains(., "Nuclear Medicine")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('physical_therapy_equipment', '//ul/li[contains(., "Physical Therapy Equipment")]/img', re=r'(checkmark.*)\.gif')
        loader.add_xpath('ultrasound', '//ul/li[contains(., "Ultrasound")]/img', re=r'(checkmark.*)\.gif')

        # Scheduling
        loader.add_xpath('daytime_primary_emergency', '//li[contains(., "Percentage of program intern is assigned to daytime primary emergency")]', re='(\d+)%')
        loader.add_xpath('overnight_primary_emergency', '//li[contains(., "Percentage of program intern is assigned to overnight primary emergency")]', re='(\d+)%')
        loader.add_xpath('first_opinion_clinics', '//li[contains(., "Percentage of program intern is assigned to first opinion (primary care) clinics")]', re='(\d+)%')
        loader.add_xpath('elective_time', '//li[contains(., "Percentage of program intern is provided elective time")]', re='(\d+)%')
        loader.add_xpath('satellite_clinic', '//li[contains(., "Percentage of program intern is required to work at a secondary (satellite) clinic")]', re='(\d+)%')

        # Orientation/Supervision/Mentoring
        loader.add_xpath('formal_orientation_required', '//li[contains(.,"Is a formal orientation program required?")]/div/img', re=r'checkmark(.*).gif')
        loader.add_xpath('vet_mentor', '//li[contains(.,"Does the intern have a mentor who is a veterinarian in the practice?")]/div/img', re=r'checkmark(.*).gif')
        loader.add_xpath('written_evals', '//li[contains(.,"Are written performance evaluations provided?")]/div/img', re=r'checkmark(.*).gif')
        loader.add_xpath('orientation_manual', '//li[contains(.,"Is an internship orientation manual provided?")]/div/img', re=r'checkmark(.*).gif')

        yield loader.load_item()