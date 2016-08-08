# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
import  time, os

class BaSpider(scrapy.Spider):
    name = "ba"
    allowed_domains = ["gov.cn"]
    start_urls = (
        'http://gsxt.saic.gov.cn/',
        # 'http://qyxy.baic.gov.cn/beijing',
    )

    # 初始化，这里要调用无头浏览器
    def __init__(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:8080/wd/hub', desired_capabilities={
            'takeScreenshot': False,
            'javascriptEnabled': True,
            "phantomjs.page.settings.userAgent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",

        })

    # 解析数据，然后获取到地方链接
    def parse(self, response):
        self.driver.get(response.url)
        aa = self.driver.page_source
        body = Selector(text=aa)
        urls = body.xpath('//div[@id="right"]/ul[@class="map"]/li/a/@href').extract()

        # 获取到地方链接后，通过无头浏览器打开.
        for url in urls:
            print url
        #     self.driver.get(url)
        #     aa = self.driver.page_source
        #     # body = Selector(text=aa)
        #     print "current crawl url: " + url
        #     self.driver.get(url)
        #     current_handle = self.driver.current_window_handle
        #     try:
        #         self.driver.find_element_by_partial_link_text(u'经营异常名录').click()
        #     except Exception, e:
        #         print 'error'
        #         pass
        #     all_handler = self.driver.window_handles
        #     for handler in all_handler:
        #         if handler != current_handle:
        #             self.driver.switch_to_window(handler)
        #     self.driver.current_window_handle
        #     aa = self.driver.page_source
        #     body = Selector(text=aa)
        # self.driver.quit()
        #
        #
        #     # a1 = body.xpath('//div[@style="height:600px;"]/div/ul/li[1]/text').extract()
        #     # for i in a1:
        #     #     print i
        #     # print aa
        # self.driver.close()