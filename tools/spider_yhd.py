#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/9 9:44
# @Author : libin(leoli)
# @File   : spider_yhd.py
import requests
from lxml import html


def spider(sn, booklist=[]):
    url = 'https://search.yhd.com/c0-0/k{sn}/'.format(sn=sn)
    # 获取到html源码
    html_doc = requests.get(url).text
    # xpath对象
    selector = html.fromstring(html_doc)
    # 书籍列表
    ul_list = selector.xpath('//div[@id="itemSearchList"]/div')
    # print(len(ul_list))
    # 解析数据
    for li in ul_list:
        # 标题
        title = li.xpath('div//p[@class="proName clearfix"]/a/@title')
        # print(title)
        # 价格
        price = li.xpath('div//em[@class="num"]/@yhdprice')
        # print(price)
        # 购买链接
        link = li.xpath('div//p[@class="proName clearfix"]/a/@href')
        # print(link)
        # 出版社或购买店铺
        store = li.xpath('div//p[@class="searh_shop_storeName storeName limit_width"]/a/@title')
        # print(store)
        # 优惠活动
        active = li.xpath('div//div[@class="item_bg_icon_q"]')
        # for sp in active:
        #     discount = sp.xpath('span/text()')
        #     print(discount)
        booklist.append({
            'title': title[0],
            'price': price[0],
            'link': link[0],
            'store': store[0]
            # 'discount': discount
        })
        # print("------------------------------------------------------------------------")


if __name__ == '__main__':
    sn = '9787115428028'
    spider(sn)
