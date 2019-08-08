#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/8 10:07
# @Author : libin(leoli)
# @File   : use_xpath_demo.py
from lxml import html


def parse():
    """将html文件中的内容使用xpath进行提取"""
    # 读取文件中的内容
    f = open('./static/index.html', 'r', encoding='UTF-8')
    s = f.read()
    selector = html.fromstring(s)
    # xpath解析h3标题
    h3 = selector.xpath('/html/body/h3/text()')
    print(h3[0])

    # 解析ul下面的内容
    ul = selector.xpath('/html/body/ul/li')
    print(len(ul))
    for li in ul:
        print(li.xpath('text()')[0])
    print("------------------------------------------------------------------------")
    # 另一种语法
    ul = selector.xpath('//ul/li')
    print(len(ul))
    for li in ul:
        print(li.xpath('text()')[0])
    print("------------------------------------------------------------------------")

    # 指定ul下指定元素值
    ul2 = selector.xpath('/html/body/ul/li[@class="important"]/text()')
    print(ul2)

    print("------------------------------------------------------------------------")
    # 解析a标签的内容
    a = selector.xpath('//div[@id="container"]/a')
    print(a[0].xpath('text()')[0])
    # 打印href标签
    print(a[0].xpath('@href'))

    print("------------------------------------------------------------------------")
    # 解析最后一个p标签
    p = selector.xpath('/html/body/p[last()]/text()')
    print(p[0])

    f.close()


if __name__ == '__main__':
    parse()
