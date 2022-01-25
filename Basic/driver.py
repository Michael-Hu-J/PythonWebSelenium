#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
封装driver
"""

from selenium import webdriver


def chrome_driver():
    driver = webdriver.Chrome()
    driver.get("https://biz.2dfire.com/")
    driver.maximize_window()
    return driver
