#coding=utf-8
__author__ = 'lixiaojian'


import scrapy
import re

from youku.items import YoukuItem

class YoukuSpider(scrapy.Spider):
    name = "youku"
    allowed_domains = ["youku.com"]
    start_urls = (
        "http://i.youku.com/dapili",
    )

    def __init__(self, args=None):

        if args is not None:
            scrapy_id = args


    def start_requests(self):
        reqs = []
        req = scrapy.Request("http://list.youku.com/albumlist/show/id_49412420.html")
        reqs.append(req)
        return reqs

    def parse(self, response):

        play_list = response.xpath('//div[@id="playList"]//div[@class="p-thumb"]')

        items = []
        for play in play_list:
            url = play.xpath('a/@href').extract_first()
            # url = "//v.youku.com/v_show/id_XMjc2NjE5NjU0OA==.html?f=49412420&amp;o=1"
            id = re.findall(r'(id_)(.*)(\.)', url)[0][1]
            url = "http:" + url
            album_id = "49412420"
            title = play.xpath('a/@title').extract_first().encode('utf-8')
            img_url = play.xpath('img/@src').extract_first()

            item = YoukuItem()
            item['id'] = id
            item['album_id'] = album_id
            item['title'] = title
            item['url'] = url
            item['img_url'] = img_url

            items.append(item)
        return items




    def parse_cover(self, response):
        pass
