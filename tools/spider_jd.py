#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/8 19:32
# @Author : libin(leoli)
# @File   : spider_jd.py
import requests
from lxml import html


def spider(sn):
    """爬取京东的书籍"""
    url = 'https://search.jd.com/Search?keyword={sn}'.format(sn=sn)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

    # 获取html
    response = requests.get(url=url, headers=headers)
    response.encoding = 'UTF-8'
    html_doc = response.text
    # 获取xpath对象
    selector = html.fromstring(html_doc)
    # 先抓大（找到列表集合）
    ul_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')
    print(len(ul_list))
    # 再抓小（解析对应的内容，标题，价格，链接）
    for li in ul_list:
        # 标题
        title = li.xpath('div/div[@class="p-name"]/a/@title')
        print(title)
        # 购买链接
        link = li.xpath('div/div[@class="p-name"]/a/@href')
        print(link[0])
        # 价格
        price = li.xpath('div/div[@class="p-price"]/strong/i/text()')
        print(price)
        # 店铺
        store = li.xpath('div//a[@class="curr-shop"]/@title')
        print(store)
        print("------------------------------------------------------------------------")



if __name__ == '__main__':
    sn = '9787115428028'
    spider(sn)
