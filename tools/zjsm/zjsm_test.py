#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/14 9:32
# @Author : libin(leoli)
# @File   : zjsm_test.py


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 定义读取文件函数

def read_data(file_path):
    # columa_names所有列表的名称
    column_names = ['timestamp', 'dev']
    data = pd.read_csv(file_path, header=None, names=column_names)
    return data


# 画出带有标签的彩图 

def scatter_with_color(x, y, labels, figure_no):
    plt.scatter(x, y, c=labels)
    plt.figure(figure_no)
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('Scatter with color')


# 画图线性图

def simple_line_plot(x, y, figure_no):
    plt.figure(figure_no)
    plt.plot(x, y)
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.title('simple_line_plot')


# 调用函数读取数据
if __name__ == '__main__':
    dataset = read_data('time_dev.txt')
    figure_no = 1
    x = dataset['timestamp']
    y = dataset['dev']
    # label = dataset['dev']
    # scatter_with_color(x, y, label, figure_no)
    # scatter_with_color(x, y, figure_no)
    # figure_no += 1
    # simple_line_plot(x, y, figure_no)
    plt.plot(x, y)
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.show()

