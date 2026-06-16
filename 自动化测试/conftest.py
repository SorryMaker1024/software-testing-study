# ==========================================
# conftest.py — 公共 fixture，pytest 自动加载
# ==========================================
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """每个用例：打开浏览器 → 执行测试 → 关闭浏览器"""
    d = webdriver.Edge()
    d.implicitly_wait(5)
    d.get("https://www.saucedemo.com")
    yield d
    d.quit()
