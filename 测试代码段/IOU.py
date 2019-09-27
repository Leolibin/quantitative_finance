#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/9/27 14:32
# @Author : libin(leoli)
# @File   : IOU.py


class Box:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


def box_iou(a, b):
    # 计算相交部分面积
    box_in = box_intersection(a, b)
    # 计算两个box的并集面积
    box_un = box_union(a, b)

    if (box_in < 0) | (box_un < 0):
        return 0
    return box_in / box_un


def box_intersection(a, b):
    # 计算相交的box的宽
    w = overlap(a.x, a.w, b.x, b.w)
    # 计算相交的部分的高
    h = overlap(a.y, a.h, b.y, b.h)
    # 返回相交部分的面积
    return w * h


def overlap(x1, w1, x2, w2):
    l1 = x1 - w1 / 2
    l2 = x2 - w2 / 2
    left = l1 if l1 > l2 else l2
    r1 = x1 + w1 / 2
    r2 = x2 + w2 / 2
    right = r1 if r1 < r2 else r2
    return right - left


def box_union(a, b):
    box_all = a.w * a.h + b.w * b.h
    inter = box_intersection(a, b)
    return box_all - inter


if __name__ == '__main__':
    a1 = Box(5, 6, 2, 2)
    b1 = Box(5, 6, 2, 2)

    print(box_iou(a1, b1))
