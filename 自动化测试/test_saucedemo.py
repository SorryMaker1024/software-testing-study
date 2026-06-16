# ==========================================
# pytest 实战 — SauceDemo 自动化测试用例
# 运行：python -m pytest -v 自动化测试/test_saucedemo.py
# ==========================================
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# ==========================================
# 用例1：登录成功
# ==========================================
def test_login_success(driver):
    """正确账号密码能成功登录"""
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 断言：URL 里包含 inventory，说明跳到了商品页
    assert "inventory" in driver.current_url, "登录后应跳转到商品页"


# ==========================================
# 用例2：登录失败 — 密码错误
# ==========================================
def test_login_wrong_password(driver):
    """错误密码应有错误提示"""
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    # 断言：页面上出现错误提示
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert error.is_displayed(), "错误密码应该显示错误提示"


# ==========================================
# 用例3：商品列表加载
# ==========================================
def test_inventory_loaded(driver):
    """登录后商品列表正常加载"""
    # 登录
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 用显式等待确认商品列表出现
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) >= 1, "至少应该有一个商品"


# ==========================================
# 用例4：商品排序 — 价格从低到高
# ==========================================
def test_sort_price_low_to_high(driver):
    """排序功能：按价格从低到高"""
    # 登录
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    # 切换排序
    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("lohi")

    # 获取所有价格
    prices = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
    prices = [float(p.text.replace("$", "")) for p in prices]

    # 断言：排好序了
    assert prices == sorted(prices), f"价格应该升序排列，实际：{prices}"


# ==========================================
# 用例5：加入购物车
# ==========================================
def test_add_to_cart(driver):
    """点击加入购物车，购物车数量+1"""
    # 登录
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    # 点第一个商品加入购物车
    driver.find_element(By.XPATH, "//button[contains(@id, 'add-to-cart')]").click()

    # 断言：购物车图标显示 1
    badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
    assert badge.text == "1", f"购物车数量应为1，实际为 {badge.text}"


# ==========================================
# 用例6：参数化 — 3 组登录数据
# ==========================================
@pytest.mark.parametrize("username,password,should_pass", [
    ("standard_user", "secret_sauce", True),      # 正确账号
    ("locked_out_user", "secret_sauce", False),    # 被锁账号
    ("", "", False),                               # 空账号
])
def test_login_multi(driver, username, password, should_pass):
    """参数化：不同账号登录不同结果"""
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    if should_pass:
        assert "inventory" in driver.current_url, f"{username} 应该能登录"
    else:
        # 不管什么错，反正不应该跳到商品页
        assert "inventory" not in driver.current_url, f"{username} 不应该能登录"
