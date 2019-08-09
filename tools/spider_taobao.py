#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/8/9 10:37
# @Author : libin(leoli)
# @File   : spider_taobao.py
from selenium import webdriver
import csv
from time import sleep
import os
import random


class TaobaoSpider:
    def __init__(self):
        self.d = os.path.dirname(__file__)
        self.abspath = os.path.abspath(self.d)
        options = webdriver.ChromeOptions()
        options.binary_location = r"E:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        chrome_driver_path = r"E:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        browser = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome()

    def login(self):
        # 打开淘宝登录页，并进行扫码登录
        self.driver.get("https://login.taobao.com/")
        sleep(3)  # 等待3秒让浏览器打开网址，
        print('请在15秒内扫码')
        sleep(15)
        print('跳转')

    def Seach(self):
        # 搜索商品
        # 如果不想走这一步，可以手动把搜索的url复制下来直接用login打开登录后会自动跳转
        self.driver.find_element_by_class_name('search-combobox-input').send_keys('手')
        sleep(1)  # 睡眠1秒加上输入的时间
        self.driver.find_element_by_class_name('search-combobox-input').send_keys('机')
        sleep(2)
        self.driver.find_element_by_class_name("btn-search").click()
        sleep(2)

    def Spiders(self):
        times = [12, 10, 8, 5, 4]
        sleep(random.choice(times))
        mokuai = self.driver.find_elements_by_xpath('//div[contains(@class,"ctx-box")]')
        lists = []
        for i in mokuai:
            arr = []
            arr.append(str(i.find_element_by_xpath('./div/a').get_attribute("href")))
            strs = i.text.split('\n')
            arr.append(strs[0][1:])
            arr.append(strs[1][0:-3])
            arr.append(strs[2])
            arr.append(strs[3])
            arr.append(strs[4])
            lists.append(arr)
            print(lists)
        # self.save(lists)
        return 1

    def next_pages(self):
        if self.driver.find_element_by_xpath('//ul[@class="items"]/li[3]/a').get_attribute('title') == '下一页':
            self.gungungun()
            sleep(2)
            self.driver.find_element_by_xpath('//ul[@class="items"]/li[3]/a').click()
            print('翻页')
            return 1
        else:
            return 2

    def gungungun(self):
        # 拉动滚动条防止被屏蔽
        times = [1000, 9000, 900, 5000, 40000, 300, 2570, 10000]
        js = "var q=document.documentElement.scrollTop={}".format(random.choice(times))
        js2 = "var q=document.documentElement.scrollTop=0".format(random.choice(times))
        self.driver.execute_script(js)
        sleep(3)
        self.driver.execute_script(js2)

    def save(self, lists):
        # 文件不存在会新建，追加写
        path = './taobao.csv'
        with open(path, 'a+', newline='') as t:
            writer = csv.writer(t)
            writer.writerows(lists)
        return


if __name__ == "__main__":
    res = TaobaoSpider()  # 实例化
    res.login()  # 登录
    res.Seach()  # 搜索商品
    max = 2  # 想爬取的页数，如果想爬完就默认为0
    nums = 1  # 默认页数
    while True:
        print('开始爬取第' + str(nums) + '页')
        spi = res.Spiders()  # 抓取保存数据
        if spi == 1:
            page = res.next_pages()  # 翻页
            if page == 2:
                print('爬取完成')
                exit()
        if nums == max:
            print('爬取完成2')
            exit()
        nums += 1
