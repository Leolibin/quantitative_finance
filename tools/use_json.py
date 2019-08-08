#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/8 9:39
# @Author : libin(leoli)
# @File   : use_json.py
import json


def python_to_json():
    """将python对象转为json"""
    d = {
        'name': 'python数据',
        'price': 23,
        'is_valid': True
    }
    rest = json.dumps(d, indent=4)
    print(rest)


def json_to_python():
    """将json转化为python"""
    data = '''
        {
            "name": "Python书籍",
            "origin_price": 66,
            "pub_date": "2018-4-14 17:00:00",
            "store": ["京东", "淘宝"],
            "author": ["张三", "李四", "Jhone"],
            "is_valid": true,
            "is_sale": false,
            "meta": {
                "isbn": "abc-123",
                "pages": 300
            },
            "desc": null
        }
    '''
    rest1 = json.loads(data)
    print(rest1)
    print(rest1["name"])


def json_to_python_from_file():
    """从文件读取json转为python对象"""
    f = open('./static/book.json', 'r', encoding='UTF-8')
    s = f.read()
    s = json.loads(s)
    print(s['name'])
    f.close()


if __name__ == '__main__':
    python_to_json()
    # json_to_python()
    # json_to_python_from_file()
