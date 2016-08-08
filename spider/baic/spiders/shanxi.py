# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
import time
from baic.items import BaicRecordItem
from baic import settings
class SXSpider(scrapy.Spider):
    # 山西
    name = "sxdetail"
    allowed_domains = ["gov.cn"]
    start_urls = (
        'http://gsxt.fc12319.com/exceptionInfoSelect.jspx',
    )
    # 初始化，这里要调用无头浏览器
    def __init__(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:8080/wd/hub', desired_capabilities={
            'takeScreenshot': False,
            'javascriptEnabled': True,

        })
        self.pageinfo = webdriver.Remote(command_executor='http://127.0.0.1:8080/wd/hub', desired_capabilities={
            'takeScreenshot': False,
            'javascriptEnabled': True,

        })

    def parse(self, response):
        self.driver.get(response.url)
        try:
            next_page = self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li[12]/a')
            # 点击信息栏，从企业名称进入企业详细信息栏
            # self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/ul/li[1]/a').click()

        except Exception, e:
            print e
        while next_page:
            page_info = self.driver.page_source.encode('utf8')
            response = Selector(text=page_info)

            urls = response.xpath('//div[@style="height:600px;"]/div/ul/li/a/@href').extract()
            # urls = response.xpath('//div[@style="height:600px;"]/div/ul/li/a/text()').extract()
            for url in urls:
                url = settings.base_url + url
                # print url
                yield  self.select_page_info(url)
                time.sleep(4)
            #
            self.driver.find_element_by_xpath('//div[@class="fenye"]/ul/li[12]/a').click()
            self.driver.current_window_handle
            time.sleep(2)

        self.driver.close()
        self.pageinfo.close()

            # 点击了，但是浏览器还是留在原来位置，这里要做切换，切换到企业详细信息栏
            # current_windows = self.driver.current_window_handle
            # all_windows = self.driver.window_handles
            # for window in all_windows:
            #     if window != current_windows:
            #         self.driver.switch_to_window(window)  # 找到handler 然后切换

            # # 进入企业详细信息栏了，但是有很多tab，省份不同，默认的tab位置还不同，所以这里统一做一次点击 进入【登记信息】栏
            # self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/ul/li[1]').click()
            #
            # # 浏览器是进去了，但是我们程序还留在原来的页面，这里切换到新的window
            # self.driver.current_window_handle

    def select_page_info(self, pageinfo_url):
        # 获取到网页的URL，打开新链接， 获取网页源码
        self.pageinfo.get(pageinfo_url)
        self.pageinfo.current_window_handle
        page_info = self.pageinfo.page_source.encode('utf8')
        response = Selector(text=page_info)
        # 找到了网页源码，开始解析网页，获取需要的item.
        url = self.pageinfo.current_url
        city = u'山西'
        register_ID = response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[2]/td[1]/text()').extract()
        register_name = response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[2]/td[2]/text()').extract()
        type = response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[3]/td[1]/text()').extract()
        representative =response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[3]/td[2]/text()').extract()
        capital = response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[4]/td[1]/text()').extract()
        establishment = response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[4]/td[2]/text()').extract()
        lodgment =response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[5]/td[1]/text()').extract()
        Operating_start = response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[6]/td[1]/text()').extract()
        Operating_end = response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[6]/td[2]/text()').extract()
        Business_scope = response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[7]/td[1]/text()').extract()
        reg_authority = response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[8]/td[1]/text()').extract()
        Approved_date = response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[8]/td[2]/text()').extract()
        status = response.xpath('//div[@id="jibenxinxi"]/table[@class="detailsList"]/tbody/tr[9]/td[1]/text()').extract()

        #
        # baicinfos = []
        baicinfo = BaicRecordItem()
        baicinfo["url"] = [url]
        baicinfo["city"] = [city]
        try:
            baicinfo["register_ID"] = register_ID
            baicinfo["register_name"] = register_name
            baicinfo["type"] = type
            baicinfo["representative"] = representative
            baicinfo["capital"] = capital
            baicinfo["establishment"] = establishment
            baicinfo["lodgment"] = lodgment
            baicinfo["Operating_start"] = Operating_start
            baicinfo["Operating_end"] = Operating_end
            baicinfo["Business_scope"] = Business_scope
            baicinfo["reg_authority"] = reg_authority
            baicinfo["Approved_date"] = Approved_date
            baicinfo["status"] = status

            return baicinfo

        except Exception:
            pass
        # for i in baicinfo:
        #     print i + ': ' + baicinfo[i][0]# .strip()
        # print "*" * 20
        # baicinfos.append(baicinfo)


            




