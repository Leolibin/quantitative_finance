#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/8 17:58
# @Author : libin(leoli)
# @File   : spider_dangdang.py


def spider(sn):
    """爬取当当网"""
    url = 'http://search.dangdang.com/?key={sn}&act=input'.format(sn=sn)

