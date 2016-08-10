# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
import time


class TJSpider(scrapy.Spider):
    # 天津
    name = "tj"
    allowed_domains = ["gov.cn"]
    start_urls = (
        'http://tjcredit.gov.cn/platform/saic/exclist.ftl',
    )

    # 初始化，这里要调用无头浏览器
    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:8080/wd/hub',
            desired_capabilities={
                'takeScreenshot': False,
                'javascriptEnabled': True,
            })

    def parse(self, response):
        self.driver.get(response.url)
        # name = response.xpath('//div[@id="mainContent"]/div/ul/li[1]/a/text()').extract()
        # date1   = response.xpath('//div[@id="mainContent"]/div/ul/li[2]/text()').extract()
        # jigou = response.xpath('//div[@id="mainContent"]/div/ul/li[3]/text()').extract()
        # date2 = response.xpath('//div[@id="mainContent"]/div/ul/li[4]/text()').extract()
        # for i in xrange(len(name)):
        #     print name[i]
        #     print date1[i]
        #     print jigou[i]
        #     print date2[i]
        #     print "*"*20
        # print response.body
        # next_page = response.xpath('//table[@class="ccjcList"]/tr/th').extract()


        # print next_page
        try:
            next_page = self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li/a[@onclick="nextPage()"]')
        except Exception as e:
            print e
        while next_page:

            # while
                # body = Selector(text=aa)
            try:
                self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li/a[@onclick="nextPage()"]').click()
            except Exception, e:
                print e
                pass
            self.driver.current_window_handle
            aa = self.driver.page_source
            body = Selector(text=aa)
            name = body.xpath('//div[@id="mainContent"]/div/ul/li[1]/a/text()').extract()
            date1 = body.xpath('//div[@id="mainContent"]/div/ul/li[2]/text()').extract()
            jigou = body.xpath('//div[@id="mainContent"]/div/ul/li[3]/text()').extract()
            date2 = body.xpath('//div[@id="mainContent"]/div/ul/li[4]/text()').extract()
            for i in xrange(len(name)):
                print name[i]
                print date1[i]
                print jigou[i]
                print date2[i]
                print "*" * 20
                print "=" * 20
                time.sleep(5)
            next_page = self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li/a[@onclick="nextPage()"]')
        pass
