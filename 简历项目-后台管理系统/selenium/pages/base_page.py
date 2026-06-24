"""
BasePage - 所有页面对象的基类
封装通用操作：等待、点击、输入、截图
"""

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """页面对象基类"""

    def __init__(self, driver, base_url="http://localhost:3002"):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    # ========== 导航 ==========
    def open(self, path=""):
        """打开指定路径"""
        url = f"{self.base_url}/#/{path.lstrip('/')}"
        self.driver.get(url)
        return self

    # ========== 元素定位 ==========
    def find(self, by, value):
        """查找单个元素"""
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        """查找多个元素"""
        return self.driver.find_elements(by, value)

    def wait_visible(self, by, value, timeout=10):
        """等待元素可见"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def wait_clickable(self, by, value, timeout=10):
        """等待元素可点击"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def wait_text_in_element(self, by, value, text, timeout=10):
        """等待元素包含指定文本"""
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((by, value), text)
        )

    # ========== 操作 ==========
    def click(self, by, value):
        """点击元素（带等待可点击）"""
        el = self.wait_clickable(by, value)
        el.click()
        return self

    def fill(self, by, value, text):
        """输入文本（先清空再输入，触发 Vue v-model 更新）"""
        from selenium.webdriver.common.keys import Keys
        el = self.wait_visible(by, value)
        el.click()
        el.send_keys(Keys.CONTROL + "a")  # 全选
        if text:
            el.send_keys(text)  # 输入新文本
        else:
            el.send_keys(Keys.DELETE)  # 清空
        return self
        return self

    def get_text(self, by, value):
        """获取元素文本"""
        return self.wait_visible(by, value).text

    def is_displayed(self, by, value):
        """判断元素是否显示"""
        try:
            return self.find(by, value).is_displayed()
        except NoSuchElementException:
            return False

    def wait_disappear(self, by, value, timeout=10):
        """等待元素消失"""
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((by, value))
        )

    def wait_loading(self, timeout=15):
        """等待页面 Loading 消失"""
        time.sleep(0.5)  # 给 loading 一点时间出现
        try:
            self.wait_disappear(By.CSS_SELECTOR, ".el-loading-mask", timeout=timeout)
        except TimeoutException:
            pass  # 可能没有 loading

    # ========== Element Plus 通用操作 ==========
    def select_option(self, select_el, option_text):
        """在 el-select 中选择一个选项"""
        select_el.click()
        time.sleep(0.5)
        options = self.driver.find_elements(By.CSS_SELECTOR, ".el-select-dropdown__item")
        for opt in options:
            if option_text in opt.text:
                opt.click()
                return self
        raise Exception(f"未找到选项: {option_text}")

    def confirm_dialog(self):
        """点击确认弹窗的确定按钮"""
        time.sleep(0.3)
        confirm_btn = self.driver.find_element(
            By.CSS_SELECTOR, ".el-message-box__btns .el-button--primary"
        )
        confirm_btn.click()
        return self

    def cancel_dialog(self):
        """点击确认弹窗的取消按钮"""
        time.sleep(0.3)
        cancel_btn = self.driver.find_element(
            By.CSS_SELECTOR, ".el-message-box__btns button:first-child"
        )
        cancel_btn.click()
        return self

    def get_toast_msg(self):
        """获取 ElMessage 弹窗消息"""
        el = self.wait_visible(By.CSS_SELECTOR, ".el-message__content", timeout=5)
        text = el.text
        self.wait_disappear(By.CSS_SELECTOR, ".el-message", timeout=5)
        return text

    def screenshot(self, name="screenshot"):
        """保存截图"""
        path = f"screenshots/{name}_{int(time.time())}.png"
        self.driver.save_screenshot(path)
        return path
