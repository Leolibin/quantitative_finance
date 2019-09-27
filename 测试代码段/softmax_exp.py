#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/9/27 16:42
# @Author : libin(leoli)
# @File   : softmax_exp.py
import numpy as np

a = np.array([10011, 10010, 10009])
# a_exp = np.exp(a) / np.sum(np.exp(a))
# print(a_exp)

# 为什么softmax要使用指数函数：https://segmentfault.com/a/1190000017320763?utm_source=tag-newest

c = np.max(a)
a_exp_c = np.exp(a - c) / np.sum(np.exp(a - c))
print(a_exp_c)
# softmax输出的数组的和为1
print(np.sum(a_exp_c))
