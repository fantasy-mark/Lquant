# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
from Data.str2int import str2int

class Lizard:
    def __init__(self):
        # webdriver中的PhantomJS方法可以打开一个我们下载的静默浏览器。
        # 输入executable_path为当前文件夹下的phantomjs.exe以启动浏览器
        self.driver = webdriver.PhantomJS(executable_path="../bin/phantomjs.exe")

    def Get_Industry_Index(self):
        # 使用浏览器请求页面
        self.driver.get("http://finance.sina.com.cn/stock/sl/#industry_1")
        # 加载3秒，等待所有数据加载完毕
        time.sleep(3)
        # 通过id来定位元素，
        # .text获取元素的文本数据
        contents = self.driver.page_source.encode('utf-8', 'ignore')
        soup = BeautifulSoup(contents, 'html.parser', from_encoding="utf-8")

        tr_list = soup.find_all("tr")

        data = []

        for item in tr_list:
            a_list = item.find_all(name="a", href=re.compile(
                r"http://vip.stock.finance.sina.com.cn/mkt/#hangye_"))
            span_list = item.find_all("span")

            industries = []
            info = []

            for item in a_list:
                industries.append(item.string)
                # print(type(item))
            i = 0
            for item in span_list:
                i += 1
                if i % 3 == 0:
                    info.append(str2int(item.string[:-1]))
                    print(str2int(item.string[:-1]))
                    break

            if industries:
                data.append(industries + info)
        return pd.DataFrame(data, columns=['行业', '涨跌幅(%)'])

    def __del__(self):
        # 关闭浏览器
        self.driver.close()
