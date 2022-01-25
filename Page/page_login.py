#!/usr/bin/python3
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from Basic.base import Base


class Login(Base):
    def login(self):
        super().find_element(By.CSS_SELECTOR, ".login-btn", "点击手机账号登录").click()
        super().send_to_keys(By.CSS_SELECTOR, "[placeholder='请输入手机号码']", "输入手机号码", *["17771432624"])
        super().send_to_keys(By.CSS_SELECTOR, "[placeholder='请输入密码']", "输入密码", *["hujian1380725545"])
        super().find_element(By.CSS_SELECTOR, "[class='btn ivu-btn ivu-btn-primary'] > span", "点击登录").click()
