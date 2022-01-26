#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Basic.base import Base


class SwitchStore(Base):
    def click_switch(self):
        account = super().wait_element_explicit(By.CSS_SELECTOR, ".account-arrow", "悬停我的账户")
        self.action_chains.move_to_element(account).perform()
        switch = super().wait_element_explicit(By.CSS_SELECTOR, "#common-nav-shift-shop", "点击切换店铺")
        self.action_chains.click(switch).perform()

    def search_store(self):
        super().send_to_keys(By.CSS_SELECTOR, "[placeholder='请输入店铺编码或店铺名称']", "搜索店铺", *["北杏仁餐饮测试门店", Keys.ENTER])
        super().wait_element_explicit(By.XPATH, "//span[text()='北杏仁餐饮测试门店']", "点击北杏仁餐饮测试门店").click()

    def view_mall_order(self):
        super().wait_element_explicit(By.XPATH, "//a[text()='掌柜工具']", "点击掌柜工具").click()
        super().wait_element_explicit(By.XPATH, "//li[text()='微商城订单']", "点击微商城订单").click()
        # super().wait_element_explicit(By.XPATH, "//span[text()='批量发货']/parent::button[1]", "点击批量发货").click()
        # super().wait_element_explicit(By.XPATH, "//span[text()='选择文件']/parent::button[1]", "点击选择文件").click()

    def filter(self):
        """筛选手机号为17771432624，订单状态选待发货，下单日期设定2022-01-01至2022-01-14"""
        super().send_to_keys(By.CSS_SELECTOR, ".ant-input", "筛选手机号", *["17771432624"])
        super().find_elements(By.CSS_SELECTOR, ".ant-select-selection__rendered", "点击下拉订单状态")[0].click()
        super().find_element(By.XPATH, "//li[text()='待发货']", "选择待发货").click()
        super().find_elements(By.CSS_SELECTOR, ".ant-calendar-range-picker-input", "点击日期控件")[0].click()
        super().find_elements(By.CSS_SELECTOR, ".ant-calendar-input ", "填写结束日期")[1].send_keys(
            "2022-01-14 23:59:59")
        super().find_elements(By.CSS_SELECTOR, ".ant-calendar-input ", "填写开始日期")[0].send_keys(
            "2022-01-01 00:00:00")
        super().find_element(By.CSS_SELECTOR, ".ant-calendar-ok-btn", "确定日期").click()
        # remove_start = "document.getElementsByClassName('ant-calendar-range-picker-input')[0].removeAttribute('readonly');"
        # self.driver.execute_script(remove_start)
        # remove_end = "document.getElementsByClassName('ant-calendar-range-picker-input')[1].removeAttribute('readonly');"
        # self.driver.execute_script(remove_end)
        # end_date = "document.getElementsByClassName('ant-calendar-input ')[1].value='2022-01-15 23:59:59';"
        # self.driver.execute_script(end_date)
        # start_date = "document.getElementsByClassName('ant-calendar-input ')[0].value='2022-01-15 00:00:00';"
        # self.driver.execute_script(start_date)
        super().find_element(By.CSS_SELECTOR, "button[class$='ant-btn-primary']", "点击筛选").click()

    def send(self):
        """选择亚马逊物流快递"""
        # time.sleep(1)
        super().wait_element_explicit(By.XPATH, "//a[text()='发货']", "点击发货").click()
        super().wait_element_explicit(By.XPATH,
                                      "//div[@class='ant-select-search ant-select-search--inline']/parent::div[1]",
                                      "点击下拉物流公司").click()
        # time.sleep(1)
        super().wait_element_explicit(By.XPATH, "//li[text()='亚马逊物流']", "选择亚马逊物流快递").click()
        super().send_to_keys(By.XPATH, "//span[text()='物流单号:']/following-sibling::input[1]", "输入物流单号", *["12345678"])
        super().wait_element_explicit(By.XPATH, "//span[text()='确 定']/parent::button[1]", "点击确定").click()
        time.sleep(5)
