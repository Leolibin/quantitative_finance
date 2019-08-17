#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/14 11:43
# @Author : libin(leoli)
# @File   : test3.py

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import pylab as mpl  # 导入中文字体，避免显示乱码

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置为黑体字

# 需要用到read_csv方法中的parse_dates参数和date_parser参数
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M')
data = pd.read_csv('min/dev9_min.txt', encoding='utf-8', parse_dates=['timestamp'], date_parser=dateparse)
# print(data.head())

# 数据透视表，需要对受理日期进行聚合，并对‘区局’列计数，计数使用的函数是aggfunc='count'
table = pd.pivot_table(data, index=['timestamp'], values=['dev'], aggfunc='count')
# print(table.head(20))  # 看一下table的前20行数据是否正常

# 检测一下table的index是否为时间序列格式
print(table.index)

# 生成figure对象
fig = plt.figure()

# 生成axis对象
ax = fig.add_subplot(111)  # 本案例的figure中只包含一个图表

# 设置x轴为时间格式，这句非常重要，否则x轴显示的将是类似于‘736268’这样的转码后的数字格式
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y/%m/%d'))

# 设置x轴坐标值和标签旋转45°的显示方式
plt.xticks(pd.date_range(table.index[0], table.index[-1], freq='M'), rotation=45)
# x轴为table.index，也就是‘异常日期’，y轴为数量，颜色设置为红色
ax.plot(table.index, table['dev'], color='r')
plt.show()

