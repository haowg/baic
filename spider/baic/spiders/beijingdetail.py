# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
import time
class BJSpider(scrapy.Spider):
    # 北京
    name = "bjdetail"
    allowed_domains = ["gov.cn"]
    start_urls = (
        'http://qyxy.baic.gov.cn/dito/ditoAction!ycmlFrame.dhtml?clear=true',
    )
    # 初始化，这里要调用无头浏览器
    def __init__(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:8080/wd/hub', desired_capabilities={
            'takeScreenshot': False,
            'javascriptEnabled': True,

        })

    def parse(self, response):
        # 1.获取网页源码，分析列表，获取列表长度
        urls = response.url
        self.driver.get(urls)
        aa = self.driver.page_source
        response = Selector(text=aa)
        links = response.xpath('/html/body/div/div/div[3]/div[1]/form/table/tbody/tr').extract()
        # print len(links)
        # 2. 获取到列表长度之后，可以根据长度来产生Xpath

        for i in range(1, len(links)-1):
            # 3. 因为该网站默认点击列表时，当前页面会被直接替换成新网页，所以这里需要重新打开一次
            self.driver.get(urls)
            self.driver.current_window_handle
            # 4. 根据这里就产生不同的xpath之后，模拟点击
            #    因为xpath不一样，所以每次点击的位置也就不一样，结果就是查询到不同的公司
            xpath = '/html/body/div/div/div[3]/div[1]/form/table/tbody/tr[2]/td['+ str(i) +']/a'
            # print xpath
            self.driver.find_element_by_xpath(xpath).click()
            self.driver.current_window_handle
            # 5.获取到不同的公司详情URL，接下来就可以分析网页源码，做数据提取，然后入库
            print self.driver.current_url






            print '*' * 9
            time.sleep(5)




        # try:
        #     next_page = self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li/a[@onclick="nextPage()"]')
        # except Exception, e:
        #     print e
        #
        # while next_page:
        #     try:
        #         self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li/a[@onclick="nextPage()"]').click()
        #     except Exception, e:
        #         print e
        #         pass
        #     self.driver.current_window_handle
        #     aa = self.driver.page_source
        #     body = Selector(text=aa)
        #     name = body.xpath('//table[@class="ccjcList"]/tr/td[1]/a/text()').extract()
        #     ID   = body.xpath('//table[@class="ccjcList"]/tr/td[2]/text()').extract()
        #     date = body.xpath('//table[@class="ccjcList"]/tr/td[3]/text()').extract()
        #     for i in xrange(len(name)):
        #         print name[i]
        #         print ID[i]
        #         print date[i]
        #         print "*" * 20
        #
        #     time.sleep(5)
        #     next_page = self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li/a[@onclick="nextPage()"]')
        pass