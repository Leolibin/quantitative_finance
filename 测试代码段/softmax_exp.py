#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/9/27 16:42
# @Author : libin(leoli)
# @File   : softmax_exp.py
import numpy as np

a = np.array([10011, 10010, 10009])
# a_exp = np.exp(a) / np.sum(np.exp(a))
# print(a_exp)

c = np.max(a)
a_exp_c = np.exp(a - c) / np.sum(np.exp(a - c))
print(a_exp_c)
