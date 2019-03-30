# -*- coding: utf-8 -*-
import scrapy
from Tengxun.items import TengxunItem


class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['hr.tencent.com']
    # 定义1个基准的url,方便后期拼接290个URL
    url = "https://hr.tencent.com/position.php?start="
    start = 0
    # 拼接初始的url
    start_urls = [url + str(start)]

    # parse函数是第1次从start_urls中初始URL发请求后
    # 得到响应后必须要调用的函数
    def parse(self, response):
        for i in range(0,2891,10):
            # scrapy.Request()
            # 把290页的URL给调度器入队列,然后出队列给下载器
            yield scrapy.Request\
               (self.url + str(i),
                callback=self.parseHtml)

    def parseHtml(self,response):
        # 每个职位的节点对象列表
        baseList = response.xpath('//tr[@class="odd"] | //tr[@class="even"]')
        for base in baseList:
            item = TengxunItem()
            item["zhName"] = base.xpath('./td[1]/a/text()').extract()[0]
            # 链接
            item["zhLink"] = base.xpath('./td[1]/a/@href').extract()[0]
            
            # 类别
            item["zhType"] = base.xpath('./td[2]/text()').extract()
            if item["zhType"]:
                item["zhType"] = item["zhType"][0]
            else:
                item["zhType"] = "无"

            # 人数
            item["zhNum"] = base.xpath('./td[3]/text()').extract()[0]
            # 地点
            item["zhAddress"]= base.xpath('./td[4]/text()').extract()[0]
            # 时间
            item["zhTime"] = base.xpath('./td[5]/text()').extract()[0]

            yield item

