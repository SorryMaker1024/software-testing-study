"""
pytest 公共配置
存放 fixture、公共函数等
"""

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """初始化浏览器驱动"""
    # TODO: 配置 WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
