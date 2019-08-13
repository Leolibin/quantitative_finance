#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/8 16:59
# @Author : libin(leoli)
# @File   : use_requests.py
import requests


def get_book(sn):
    url = 'http://search.dangdang.com/'
    rest = requests.get(url, params={
        'key': sn,
        'act': 'input'
    })
    print(rest.text)
    print(rest.status_code)
    print(rest.encoding)


if __name__ == '__main__':
    get_book()
