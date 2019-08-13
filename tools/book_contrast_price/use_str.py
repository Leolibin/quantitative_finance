#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/8 17:23
# @Author : libin(leoli)
# @File   : use_str.py


def format_str():
    """格式化字符串"""
    name = "张三"
    print('欢迎你%s' % name)

    # 格式化整形,float

    num = 30.37777
    print('您输入的数字是：%.1f' % num)

    num2 = 54
    print('您的编号是:%04d' % num2)

    tuple1 = (1, 2, 3, 4, 5)
    print('您输入的元组为：%s' % str(tuple1))

    print('您的名字为:%(name)s' % {'name': name})


def format_str_2():
    """使用format进行格式化"""
    # 使用位置
    print('欢迎您，{0}，{1} ------{0}说{1}'.format('张三', '好久不见'))
    # 使用名称
    name = "张三"
    code = 222
    print('欢迎你，{name}，您的编号是{code}'.format(name=name, code=code))

    # 使用字段
    d = {
        'name': '李彬',
        'code': '916'
    }
    print('欢迎你{name}，您的编号是{code}'.format(**d))

    # 格式化元组
    point = (1, 9)
    print('您的坐标是：{0[0]}:{0[1]}'.format(point))

    # 格式化类
    user = User('李彬', 23)
    print(user.show())
    print(user)


class User(object):
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def show(self):
        return '用户名：{self.username}，年龄:{self.age}'.format(self=self)

    def __str__(self):
        return self.show()


if __name__ == '__main__':
    # format_str()
    format_str_2()
