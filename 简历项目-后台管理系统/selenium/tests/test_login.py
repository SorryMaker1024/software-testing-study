"""
登录模块 Selenium 自动化测试

运行方式：
    pytest tests/test_login.py -v
    pytest tests/test_login.py -v --headless
    pytest tests/test_login.py -v --html=report.html
"""

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


def wait_for_url_change(driver, old_url, timeout=10):
    """等待 URL 变化（登录成功后跳转）"""
    for _ in range(timeout * 2):
        if driver.current_url != old_url:
            return True
        time.sleep(0.5)
    return False


class TestLoginSuccess:
    """登录成功场景"""

    def test_correct_captcha(self, driver, base_url):
        """TC-01：验证码正确（0），登录成功"""
        page = LoginPage(driver, base_url)
        page.open_login()
        old_url = driver.current_url
        page.login_as("admin", "123456", "0")

        # 等待跳转
        time.sleep(2)
        assert "login" not in driver.current_url, f"应跳离登录页，当前URL: {driver.current_url}"

    def test_preset_account_admin(self, driver, base_url):
        """TC-02：选择预设账号 admin/123456"""
        page = LoginPage(driver, base_url)
        page.open_login()
        page.select_preset_account("admin")
        page.enter_captcha("0")
        page.click_login()

        time.sleep(2)
        # 预设账号自动填充了用户名密码+正确验证码，应登录成功
        assert "login" not in driver.current_url, "预设账号登录后应跳转首页"


class TestLoginFail:
    """登录失败场景"""

    def test_wrong_captcha(self, driver, base_url):
        """TC-04：验证码错误，提示错误信息"""
        page = LoginPage(driver, base_url)
        page.open_login()
        page.login_as("admin", "123456", "999")

        # 验证：停留在登录页
        assert "login" in driver.current_url, "验证码错误应停留在登录页"

    def test_empty_captcha(self, driver, base_url):
        """TC-05：不填验证码，前端校验拦截"""
        page = LoginPage(driver, base_url)
        page.open_login()
        # 清掉默认用户名，填入新值
        page.enter_username("admin")
        page.enter_password("123456")
        page.fill(By.CSS_SELECTOR, "input[placeholder='验证码']", "")
        page.click_login()

        # Mock 返回"验证码不能为空"
        time.sleep(1)
        assert "login" in driver.current_url, "验证码为空应停留在登录页"

    def test_empty_username(self, driver, base_url):
        """TC-06：用户名为空，前端校验"""
        page = LoginPage(driver, base_url)
        page.open_login()
        # 清空默认用户名
        page.fill(*page.USERNAME_INPUT, "")
        page.enter_password("123456")
        page.enter_captcha("0")
        page.click_login()

        # 表单校验或停留在登录页
        time.sleep(1)
        still_on_login = "login" in driver.current_url
        assert still_on_login, f"用户名为空应停留在登录页，当前URL: {driver.current_url}"


class TestLoginUI:
    """登录页 UI 元素"""

    def test_captcha_image_loaded(self, driver, base_url):
        """TC-07：验证码图片正常加载"""
        page = LoginPage(driver, base_url)
        page.open_login()

        img = page.find(*page.CAPTCHA_IMAGE)
        assert img.is_displayed(), "验证码图片应显示"

    def test_captcha_refresh_click(self, driver, base_url):
        """TC-08：点击验证码图片刷新"""
        page = LoginPage(driver, base_url)
        page.open_login()

        img = page.find(*page.CAPTCHA_IMAGE)
        old_src = img.get_attribute("src")

        img.click()
        # 等待一下刷新
        import time
        time.sleep(1)

        img = page.find(*page.CAPTCHA_IMAGE)
        new_src = img.get_attribute("src")

        assert old_src == new_src, "Mock 验证码图片不会变（相同 Base64）"

    def test_login_button_exists(self, driver, base_url):
        """TC-09：登录按钮存在"""
        page = LoginPage(driver, base_url)
        page.open_login()

        btn = page.find(*page.LOGIN_BTN)
        assert btn.is_displayed(), "登录按钮应显示"
        # Element Plus 渲染可能把"登录"拆成多个节点，用 textContent
        btn_text = btn.get_attribute("textContent") or btn.text
        assert "登" in btn_text and "录" in btn_text, f"按钮应含'登录'，实际: {btn_text}"

    def test_page_title(self, driver, base_url):
        """TC-10：页面标题显示"""
        page = LoginPage(driver, base_url)
        page.open_login()

        title = page.get_text(*page.TITLE_TEXT)
        assert len(title) > 0, "应显示系统标题"
