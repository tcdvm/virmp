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
        self.logger.info("============" + response.xpath('//strong/text()').extract_first())

        loader = ItemLoader(item=ProgramDetailItem(), response=response)
        # Get name of place
        loader.add_xpath('name', '//strong/text()')
        # Get caseload info
        loader.add_xpath('total_annual_cases', '//table[@id="caseload"]/tr[2]/td[1]/text()')
        loader.add_xpath('avg_daily_cases', '//table[@id="caseload"]/tr[2]/td[2]/text()')
        loader.add_xpath('avg_daily_outpatient_cases', '//table[@id="caseload"]/tr[2]/td[3]/text()')
        loader.add_xpath('avg_daily_inpatient_cases', '//table[@id="caseload"]/tr[2]/td[4]/text()')
        loader.add_xpath('avg_daily_surgeries', '//table[@id="caseload"]/tr[2]/td[5]/text()')
        loader.add_xpath('avg_daily_ER_cases', '//table[@id="caseload"]/tr[2]/td[6]/text()')
        # Get number of positions
        loader.add_xpath('number_of_positions', '//*[contains(text(),"Position")]/text()')
        # Get program categories (to exclude any internship that is multi-category)
        loader.add_xpath('program_categories', '//p[contains(.,"Program Categories")]/text()')
        # Get Salary
        loader.add_xpath('salary', '//p[contains(.,"Salary")]/text()', re=r"(\d+,?\d+)")
        # Get faculty and residents in direct support of program
        loader.add_xpath('faculty_support', '//p[contains(.,"Number of Faculty/Clinicians in Direct Support of Program")]/text()[1]', re=r'(\d+)') 
        loader.add_xpath('resident_support', '//p[contains(.,"Number of Faculty/Clinicians in Direct Support of Program")]/text()[3]', re=r'(\d+)') 

        yield loader.load_item()

        # yield program_detail