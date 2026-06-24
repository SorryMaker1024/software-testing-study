"""
用户管理 Selenium 自动化测试

前提：需先登录，使用已登录的 session
注意：这些测试依赖 Mock 数据，Mock 返回模拟数据而非真实数据库操作

运行方式：
    pytest tests/test_user_management.py -v
"""

import time
import pytest
from pages.login_page import LoginPage
from pages.user_page import UserPage


@pytest.fixture(autouse=True)
def login_first(driver, base_url):
    """每个测试前确保已登录"""
    # 打开登录页
    driver.get(f"{base_url}/#/login")
    time.sleep(2)

    # 如果已登录（被重定向到 dashboard），跳过登录
    if "login" not in driver.current_url:
        return

    # 未登录则执行登录
    login_page = LoginPage(driver, base_url)
    login_page.login_as("admin", "123456", "0")
    # 等待跳转
    time.sleep(3)


class TestUserList:
    """用户列表页"""

    def test_user_page_accessible(self, driver, base_url):
        """TC-USER-01：用户管理页可访问"""
        page = UserPage(driver, base_url)
        page.open_user_page()

        assert page.is_displayed(*page.TABLE), "应显示用户列表"

    def test_table_has_data(self, driver, base_url):
        """TC-USER-02：列表有数据"""
        page = UserPage(driver, base_url)
        page.open_user_page()

        count = page.get_row_count()
        assert count > 0, "Mock 应返回至少 1 条用户数据"

    def test_pagination_visible(self, driver, base_url):
        """TC-USER-03：分页组件存在"""
        page = UserPage(driver, base_url)
        page.open_user_page()

        assert page.is_displayed(*page.PAGINATION), "应显示分页"


class TestUserSearch:
    """用户搜索"""

    def test_search_by_username(self, driver, base_url):
        """TC-USER-04：按用户名搜索"""
        page = UserPage(driver, base_url)
        page.open_user_page()
        page.search_user("admin")

        # 搜索完成后页面应正常
        assert page.is_displayed(*page.TABLE), "搜索后应显示结果"

    def test_reset_search(self, driver, base_url):
        """TC-USER-05：重置搜索"""
        page = UserPage(driver, base_url)
        page.open_user_page()
        page.search_user("admin")
        page.reset_search()

        assert page.is_displayed(*page.TABLE), "重置后应恢复列表"
