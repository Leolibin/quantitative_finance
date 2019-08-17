#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/13 19:45
# @Author : libin(leoli)
# @File   : duplicate.py

def dup():
    with open("111.txt", encoding='utf-8') as f:
        read = f.readlines()
        for i in read:
            if i not in a:
                a.append(i)


def read():
    with open("222.txt", 'w', encoding='utf-8') as f:
        f.write(str(a))


if __name__ == '__main__':
    a = []
    dup()
    read()
