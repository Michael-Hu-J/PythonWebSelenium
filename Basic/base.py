#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time
import os.path
from Basic.path import base_dir
from Basic.log import MyLog
from selenium.common.exceptions import *
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver

    @property
    def action_chains(self):
        """初始化ActionChains"""
        return ActionChains(self.driver)

    @property
    def alert(self):
        """"初始化Alert"""
        return Alert(self.driver)

    @property
    def width(self):
        """当前屏幕宽度"""
        return self.driver.get_window_size()["width"]

    @property
    def height(self):
        """当前屏幕高度"""
        return self.driver.get_window_size()["height"]

    # @property
    # def mouse(self):
    #     return PyMouse()
    #
    # @property
    # def keyboard(self):
    #     return PyKeyboard()

    # 定义显式wait
    def wait_element_explicit(self, By, element_locate, page_description=None, wait_time=5):
        """
        :param By: By.ID,By.XPATH,By.LINK_TEXT,By.PARTIAL_LINK_TEXT,By.NAME,By.TAG_NAME,By.CLASS_NAME,By.CSS_SELECTOR
        :param element_locate: 基于定位方式
        :param page_description: 操作描述
        :param wait_time: 等待时间，默认5秒
        :return: WebElement
        """
        MyLog.info("{}正在{}：({})".format(By, page_description, element_locate))
        try:
            wait_element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By, element_locate)))
            return wait_element
        except Exception as err:
            MyLog.exception("{}失败：{}".format(page_description, err))
            self.get_screenshot(page_description)
            raise

    # 定义多个元素显示wait
    def wait_elements_explicit(self, By, element_locate, page_description=None, wait_time=5):
        """
        :param By: By.ID,By.XPATH,By.LINK_TEXT,By.PARTIAL_LINK_TEXT,By.NAME,By.TAG_NAME,By.CLASS_NAME,By.CSS_SELECTOR
        :param element_locate: 基于定位方式
        :param page_description: 操作描述
        :param wait_time: 等待时间，默认5秒
        :return: WebElement list
        """
        MyLog.info("{}正在{}：({})".format(By, page_description, element_locate))
        try:
            wait_elements = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_any_elements_located((By, element_locate)))
            return wait_elements
        except Exception as err:
            MyLog.exception("{}失败：{}".format(page_description, err))
            self.get_screenshot(page_description)
            raise

    # 查找元素
    def find_element(self, By, element_locate, page_description=None):
        """
        :param By: By.ID,By.XPATH,By.LINK_TEXT,By.PARTIAL_LINK_TEXT,By.NAME,By.TAG_NAME,By.CLASS_NAME,By.CSS_SELECTOR
        :param element_locate: 基于定位方式
        :param page_description: 操作描述
        :return:
        """
        MyLog.info("{}正在{}：({})".format(By, page_description, element_locate))
        try:
            ele = self.driver.find_element(by=By, value=element_locate)
            return ele
        except NoSuchElementException as err:
            MyLog.exception("{}失败：{}".format(page_description, err))
            self.get_screenshot(page_description)
            raise

    # 查找多个元素
    def find_elements(self, By, element_locate, page_description=None):
        """
        :param By: By.ID,By.XPATH,By.LINK_TEXT,By.PARTIAL_LINK_TEXT,By.NAME,By.TAG_NAME,By.CLASS_NAME,By.CSS_SELECTOR
        :param element_locate: 基于定位方式
        :param page_description: 操作描述
        :return: 元素的list列表
        """
        MyLog.info("{}正在{}：({})".format(By, page_description, element_locate))
        try:
            eles = self.driver.find_elements(by=By, value=element_locate)
            return eles
        except NoSuchElementException as err:
            MyLog.exception("{}失败：{}".format(page_description, err))
            self.get_screenshot(page_description)
            raise

    # 输入文本
    def send_to_keys(self, By, element_locate, page_description=None, *keys_to_send):
        """
        :param By: By.ID,By.XPATH,By.LINK_TEXT,By.PARTIAL_LINK_TEXT,By.NAME,By.TAG_NAME,By.CLASS_NAME,By.CSS_SELECTOR
        :param element_locate: 基于定位方式
        :param page_description: 操作描述
        :param keys_to_send: 要输入的文本和Keys特殊键，以列表或者元组传参
        :return:
        """
        ele = self.find_element(By=By, element_locate=element_locate, page_description="查找元素")
        MyLog.info("正在{}：{}".format(page_description, keys_to_send[0]))
        try:
            ele.click()
            ele.clear()
            ele.send_keys(keys_to_send)
        except Exception as err:
            MyLog.exception("{}失败：{}".format(page_description, err))
            self.get_screenshot(page_description=page_description)
            raise

    # 获取元素属性
    def get_attribute(self, By, element_locate, attribute_name):
        """
        :param By: By.ID,By.XPATH,By.LINK_TEXT,By.PARTIAL_LINK_TEXT,By.NAME,By.TAG_NAME,By.CLASS_NAME,By.CSS_SELECTOR
        :param element_locate: 基于定位方式
        :param attribute_name: 元素属性名称
        :return:
        """
        ele = self.find_element(By=By, element_locate=element_locate, page_description="查找元素")
        try:
            att = ele.get_attribute(attribute_name)
            MyLog.info('已成功获取"{}"元素属性'.format(attribute_name))
            return att
        except Exception as err:
            MyLog.exception('获取"{}"元素失败：{}'.format(attribute_name, err))

    # 屏幕截图
    def get_screenshot(self, page_description=None):
        screenshot_path = os.path.join(base_dir, "screenshots/{}_{}.png".format(page_description,
                                                                                time.strftime("%Y-%m-%d",
                                                                                              time.localtime())))
        self.driver.get_screenshot_as_file(screenshot_path)
        MyLog.info("错误截图保存在：{}".format(screenshot_path))

