"""
pytest 配置文件
- 管理 WebDriver 生命周期
- 失败自动截图
- 命令行参数化
"""

import pytest
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# ========== 命令行参数 ==========
def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default="http://localhost:3002",
                     help="测试目标地址，默认 http://localhost:3002")
    parser.addoption("--browser", action="store", default="chrome",
                     help="浏览器类型：chrome / edge")
    parser.addoption("--headless", action="store_true", default=False,
                     help="无头模式运行")


# ========== 截图目录 ==========
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")


# ========== WebDriver Fixture ==========
@pytest.fixture(scope="function")
def driver(request):
    """创建 WebDriver 实例，测试结束后自动关闭"""
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "edge":
        from selenium.webdriver.edge.service import Service as EdgeService
        from selenium.webdriver.edge.options import Options as EdgeOptions
        from webdriver_manager.microsoft import EdgeChromiumDriverManager

        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        service = EdgeService(EdgeChromiumDriverManager().install())
        _driver = webdriver.Edge(service=service, options=options)
    else:
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        _driver = webdriver.Chrome(service=service, options=options)

    _driver.implicitly_wait(5)

    yield _driver

    _driver.quit()


# ========== 失败截图 Hook ==========
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """测试失败时自动截图"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)
            test_name = item.name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{test_name}_{timestamp}.png"
            filepath = os.path.join(SCREENSHOT_DIR, filename)
            driver.save_screenshot(filepath)
            print(f"\n[SCREENSHOT] {filepath}")


# ========== 测试报告 ==========
@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")
