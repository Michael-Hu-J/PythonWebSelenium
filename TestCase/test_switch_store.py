#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pytest
from Page.page_switch_store import SwitchStore


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("login")
class TestSwitchStore:
    def test_switch_store(self, driver):
        SwitchStore(driver).click_switch()
        SwitchStore(driver).search_store()
        SwitchStore(driver).view_mall_order()
        SwitchStore(driver).filter()
        # SwitchStore(driver).send()
