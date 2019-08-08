#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/8 17:58
# @Author : libin(leoli)
# @File   : spider_dangdang.py
import requests
from lxml import html


def spider(sn):
    """爬取当当网"""
    url = 'http://search.dangdang.com/?key={sn}&act=input'.format(sn=sn)
    # 获取html
    html_data = requests.get(url=url).text

    # xpath对象
    selector = html.fromstring(html_data)

    # 找到书本列表
    ul_list = selector.xpath('//div[@id="search_nature_rg"]/ul/li')
    print(len(ul_list))
    for li in ul_list:
        # 标题
        title = li.xpath('a/@title')
        print(title[0])
        # 购买链接
        link = li.xpath('a/@href')
        print(link[0])
        # 价格
        price = li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
        print(price[0].replace('¥', ''))

        # 商家
        store = li.xpath('p[@class="search_shangjia"]/a/text()')
        store = '当当自营' if len(store) <= 0 else store[0]
        print(store)
        print("------------------------------------------------------------------------")


if __name__ == '__main__':
    sn = 9787115428028
    spider(sn)
