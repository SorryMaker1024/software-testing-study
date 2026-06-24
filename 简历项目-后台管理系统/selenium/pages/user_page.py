"""
用户管理页面对象
对应页面：/system/user
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserPage(BasePage):
    """用户管理页"""

    # ========== 元素定位器 ==========
    PAGE_HEADER = (By.CSS_SELECTOR, ".app-main")
    ADD_BTN = (By.XPATH, "//button[contains(.,'新增') or contains(.,'添加')]")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder*='用户名']")
    SEARCH_BTN = (By.XPATH, "//button[contains(.,'搜索') or contains(.,'查询')]")
    RESET_BTN = (By.XPATH, "//button[contains(.,'重置')]")
    TABLE = (By.CSS_SELECTOR, ".el-table")
    TABLE_ROWS = (By.CSS_SELECTOR, ".el-table__body-wrapper tbody tr")
    PAGINATION = (By.CSS_SELECTOR, ".el-pagination")
    DELETE_BTN = (By.XPATH, "//button[contains(.,'删除')]")
    BATCH_DELETE_BTN = (By.XPATH, "//button[contains(.,'批量')]")

    # 新增/编辑弹窗
    DIALOG = (By.CSS_SELECTOR, ".el-dialog")
    DIALOG_TITLE = (By.CSS_SELECTOR, ".el-dialog__title")
    USERNAME_DIALOG_INPUT = (By.XPATH, "//input[@placeholder='用户名']")
    NICKNAME_INPUT = (By.XPATH, "//input[@placeholder='昵称']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='手机号码']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='邮箱']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    SUBMIT_BTN = (By.CSS_SELECTOR, ".el-dialog__footer .el-button--primary")
    CANCEL_BTN = (By.CSS_SELECTOR, ".el-dialog__footer .el-button:first-child")

    # ========== 页面操作 ==========
    def open_user_page(self):
        """打开用户管理页"""
        self.open("/system/user")
        self.wait_visible(*self.TABLE, timeout=10)
        return self

    # ========== 搜索 ==========
    def search_user(self, keyword):
        """搜索用户"""
        self.fill(*self.SEARCH_INPUT, keyword)
        self.click(*self.SEARCH_BTN)
        self.wait_loading()
        return self

    def reset_search(self):
        """重置搜索"""
        self.click(*self.RESET_BTN)
        self.wait_loading()
        return self

    # ========== 新增 ==========
    def click_add(self):
        """点击新增按钮"""
        self.click(*self.ADD_BTN)
        self.wait_visible(*self.DIALOG)
        return self

    def fill_user_form(self, username="", nickname="", phone="", email="", password=""):
        """填写用户表单"""
        if username:
            self.fill(*self.USERNAME_DIALOG_INPUT, username)
        if nickname:
            self.fill(*self.NICKNAME_INPUT, nickname)
        if phone:
            self.fill(*self.PHONE_INPUT, phone)
        if email:
            self.fill(*self.EMAIL_INPUT, email)
        if password:
            self.fill(*self.PASSWORD_INPUT, password)
        return self

    def submit_form(self):
        """提交表单"""
        self.click(*self.SUBMIT_BTN)
        self.wait_loading()
        return self

    def cancel_form(self):
        """取消表单"""
        self.click(*self.CANCEL_BTN)
        return self

    # ========== 删除 ==========
    def delete_user(self, username):
        """删除指定用户"""
        delete_btn = self.driver.find_element(
            By.XPATH,
            f"//tr[contains(.,'{username}')]//button[contains(.,'删除')]"
        )
        delete_btn.click()
        self.confirm_dialog()
        self.wait_loading()
        return self

    # ========== 验证 ==========
    def get_row_count(self):
        """获取表格行数"""
        rows = self.finds(*self.TABLE_ROWS)
        return len(rows)

    def user_exists(self, username):
        """判断用户是否存在"""
        rows = self.finds(*self.TABLE_ROWS)
        for row in rows:
            if username in row.text:
                return True
        return False

    def get_dialog_title(self):
        """获取弹窗标题"""
        return self.get_text(*self.DIALOG_TITLE)
