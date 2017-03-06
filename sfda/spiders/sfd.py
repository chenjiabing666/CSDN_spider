# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest,Request
import requests,lxml
from bs4 import BeautifulSoup
from scrapy.conf import settings
from sfda.settings import *


class SfdSpider(scrapy.Spider):
    name = "sfd"
    start_urls=["http://write.blog.csdn.net/postlist"]
    cookie = settings['COOKIE']  # 带着Cookie向网页发请求
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }

    # 对请求的返回进行处理的配置
    meta = {
        'dont_redirect': True,  # 禁止网页重定向
        'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    }

    # 爬虫的起点
    def start_requests(self):
        # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
        yield Request(self.start_urls[0], callback=self.parse, cookies=self.cookie,
                      headers=self.headers, meta=self.meta)

    # Request请求的默认回调函数
    def parse(self, response):
        print response.body
        with open("check.html", "wb") as f:
            f.write(response.body)  # 把下载的网页存入文件
    # #allowed_domains = ["sfda.com"]
    # #start_urls = ['http://write.blog.csdn.net/postlist']
    # headers={#'Referer': 'https://passport.csdn.net/account/login',
    #                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36", }
    #
    # def start_requests(self):
    #     return [scrapy.Request("https://passport.csdn.net/account/login",meta = {'cookiejar' : 1},callback=self.post_login)]
    #
    #
    # def post_login(self,response):
    #     soup = BeautifulSoup(response.body, 'lxml')
    #     all_input = soup.find_all('input')
    #     lt_value = all_input[3].get('value')
    #     execution_value = all_input[4].get('value')
    #     _eventId_value = all_input[5].get('value')
    #     data = {
    #         "username": "18796327106@163.com",
    #         "password": "as676767as",
    #         "lt": lt_value,
    #         "execution": execution_value,
    #         "_eventId": _eventId_value
    #     }
    #     return [FormRequest.from_response(response,
    #                                       meta = {'cookiejar' : response.meta['cookiejar']},
    #                                       headers=self.headers,
    #                                       formdata=data,
    #                                       callback=self.after_login,
    #                                       dont_filter=True
    #                                       )]
    # def after_login(self,response):
    #     url='http://write.blog.csdn.net/postlist'
    #     yield scrapy.Request(url,headers=self.headers)
    # def parse(self, response):
    #     print "url=%s"%response.url
    #     print response.body






    # def start_requests(self):
    #     url="https://passport.csdn.net/account/login"
    #     soup=BeautifulSoup(requests.get(url).text,'lxml')
    #     all_input = soup.find_all('input')
    #     lt_value = all_input[3].get('value')
    #     execution_value = all_input[4].get('value')
    #     _eventId_value = all_input[5].get('value')
    #     data = {
    #         "username": "18796327106@163.com",
    #         "password": "as676767a",
    #         "lt": lt_value,
    #         "execution": execution_value,
    #         "_eventId": _eventId_value
    #     }
    #     yield FormRequest(url=url,formdata=data,headers=self.headers,callback=self.paser_content)
    #
    # def paser_content(self,response):
    #     #print "url=%s"%response.url
    #     url="http://write.blog.csdn.net/postlist"
    #     yield scrapy.Request(url,callback=self.paser_item)
    # def paser_item(self,response):
    #     print response.url





    # def parse(self, response):
    #     print 'url=%s'%response.url

