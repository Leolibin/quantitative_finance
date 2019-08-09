#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/9 13:46
# @Author : libin(leoli)
# @File   : spider_book.py
from spider_dangdang import spider as spider_dd
from spider_jd import spider as spider_jd
from spider_yhd import spider as spider_yhd


def main(sn):
    """图书比价工具"""
    booklist = []
    # 当当网书的数据
    spider_dd(sn, booklist)
    print("当当网数据爬取完成")
    # 京东书的数据
    spider_jd(sn, booklist)
    print("京东数据爬取完成")
    # 一号店书的数据
    spider_yhd(sn, booklist)
    print("一号店数据爬取完成")

    # 打印所有数据列表
    # for book in booklist:
    #     print(book)
    print("----------------------------------------开始排序-------------------------------------------------------")

    # 排序书的数据
    boot_list = sorted(booklist, key=lambda item: float(item["price"]), reverse=True)
    for book in boot_list:
        print(book)


if __name__ == '__main__':
    sn = input("请输入ISBN:")
    main(sn)
