import pytest
from Basic.driver import chrome_driver
from Page.page_login import Login


@pytest.fixture(scope="class", name="driver")
def init_driver():
    return chrome_driver()


@pytest.fixture(scope="class")
def login(driver):
    driver.implicitly_wait(1)
    Login(driver).login()
