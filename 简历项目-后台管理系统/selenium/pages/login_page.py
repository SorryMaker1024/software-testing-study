"""
登录页面对象（Page Object）
对应页面：/login
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """登录页"""

    # ========== 元素定位器 ==========
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    CAPTCHA_INPUT = (By.CSS_SELECTOR, "input[placeholder='验证码']")
    CAPTCHA_IMAGE = (By.CSS_SELECTOR, ".captcha-image img")
    LOGIN_BTN = (By.CSS_SELECTOR, ".el-button--primary")
    TITLE_TEXT = (By.CSS_SELECTOR, ".text-xl.font-medium")
    ERROR_MSG = (By.CSS_SELECTOR, ".el-message--error .el-message__content")
    DROPDOWN_TOGGLE = (By.CSS_SELECTOR, ".login-form .el-dropdown .cursor-pointer")
    DROPDOWN_ITEM_ROOT = (By.XPATH, "//li[contains(text(),'root')]")
    DROPDOWN_ITEM_ADMIN = (By.XPATH, "//li[contains(text(),'系统管理员')]")
    DROPDOWN_ITEM_TEST = (By.XPATH, "//li[contains(text(),'测试小游客')]")
    FORM_ERROR = (By.CSS_SELECTOR, ".el-form-item__error")

    # ========== 页面操作 ==========
    def open_login(self):
        """打开登录页"""
        self.open("/login")
        # 等待验证码图片加载
        self.wait_visible(*self.CAPTCHA_IMAGE, timeout=10)
        return self

    def enter_username(self, username):
        """输入用户名"""
        self.fill(*self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password):
        """输入密码"""
        self.fill(*self.PASSWORD_INPUT, password)
        return self

    def enter_captcha(self, captcha):
        """输入验证码"""
        self.fill(*self.CAPTCHA_INPUT, captcha)
        return self

    def click_login(self):
        """点击登录按钮"""
        self.click(*self.LOGIN_BTN)
        return self

    def login_as(self, username, password, captcha):
        """完整登录流程"""
        self.enter_username(username)
        self.enter_password(password)
        self.enter_captcha(captcha)
        self.click_login()
        return self

    def select_preset_account(self, account="admin"):
        """选择预设账号"""
        import time
        # Element Plus dropdown 渲染到 body，先点击触发按钮
        toggle = self.driver.find_element(By.CSS_SELECTOR, ".login-form .el-dropdown")
        toggle.click()
        time.sleep(0.8)
        # 下拉菜单渲染在 body 下的 .el-popper 中
        items = self.driver.find_elements(By.CSS_SELECTOR, ".el-popper .el-dropdown-menu__item")
        target = "系统管理员" if account == "admin" else ("root" if account == "root" else "测试小游客")
        for item in items:
            if target in item.text:
                item.click()
                return self
        raise Exception(f"未找到预设账号选项: {account}")

    def get_form_error(self):
        """获取表单校验错误信息"""
        return self.get_text(*self.FORM_ERROR)

    def wait_dashboard(self):
        """等待跳转到首页"""
        self.wait_visible(By.CSS_SELECTOR, ".dashboard-container", timeout=10)
        return self

    def is_logged_in(self):
        """判断是否已登录（是否在首页）"""
        return "login" not in self.driver.current_url and "/#" in self.driver.current_url
