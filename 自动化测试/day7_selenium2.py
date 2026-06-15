# ==========================================
# Day 7 Selenium — 元素定位 + 操作实战
# 练习网站：https://www.saucedemo.com（测试专用，不会反爬）
# ==========================================

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com")

print(f"当前页面：{driver.title}\n")

# ==========================================
# 练习1：用 6 种不同方式定位登录按钮（同一个按钮）
# ==========================================
# ID 定位
btn1 = driver.find_element(By.ID, "login-button")
print(f"1. By.ID         → {btn1.get_attribute('value')}")

# NAME 定位
btn2 = driver.find_element(By.NAME, "login-button")
print(f"2. By.NAME       → {btn2.get_attribute('value')}")

# CLASS 定位
btn3 = driver.find_element(By.CLASS_NAME, "submit-button")
print(f"3. By.CLASS_NAME → {btn3.get_attribute('value')}")

# TAG 定位（不推荐，input 太多）
# 跳过，实际场景很少单用 TAG_NAME

# CSS_SELECTOR 定位 — 重点！
btn4 = driver.find_element(By.CSS_SELECTOR, "#login-button")
print(f"4. CSS #id       → {btn4.get_attribute('value')}")

btn5 = driver.find_element(By.CSS_SELECTOR, "input.submit-button")
print(f"5. CSS .class    → {btn5.get_attribute('value')}")

# XPATH 定位 — 重点！
btn6 = driver.find_element(By.XPATH, "//input[@id='login-button']")
print(f"6. XPATH         → {btn6.get_attribute('value')}")

# ==========================================
# 练习2：元素操作 — 输入、清空、点击、读取
# ==========================================
print("\n--- 元素操作 ---")

# send_keys — 输入文字
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

# clear — 清空再输入（演示）
username.clear()
print(f"清空后用户名输入框内容：'{username.get_attribute('value')}'")

# 重新输入
username.send_keys("standard_user")

# get_attribute — 读取任意属性
placeholder = username.get_attribute("placeholder")
print(f"placeholder 属性值：{placeholder}")

# text — 读取元素上显示的文字
login_text = btn1.get_attribute("value")
print(f"登录按钮文字：{login_text}")

# click — 点击
btn1.click()
print(f"登录后页面标题：{driver.title}")

# ==========================================
# 练习3：Xpath 多种写法
# ==========================================
print("\n--- XPATH 写法 ---")

# 通过文字精准匹配
cart_link = driver.find_element(By.XPATH, "//span[@class='title']")
print(f"页面标题栏文字：{cart_link.text}")

# contains — 属性包含
item_names = driver.find_elements(By.XPATH, "//div[contains(@class, 'inventory_item_name')]")
print(f"\n商品列表（前5个）：")
for i, item in enumerate(item_names[:5]):
    print(f"  {i+1}. {item.text}")

# 多条件 and
add_btns = driver.find_elements(By.XPATH, "//button[contains(@id, 'add-to-cart')]")
print(f"\n找到 {len(add_btns)} 个「加入购物车」按钮")

# 点击第一个商品的加入购物车
add_btns[0].click()
print(f"已点击第1个商品的加入购物车")

# ==========================================
# 练习4：CSS_SELECTOR 多种写法
# ==========================================
print("\n--- CSS_SELECTOR 写法 ---")

# 属性选择器
cart_badge = driver.find_element(By.CSS_SELECTOR, "[class='shopping_cart_badge']")
print(f"购物车数量：{cart_badge.text}")

# 后代选择器（div 里的 span.title）
page_title = driver.find_element(By.CSS_SELECTOR, "div span.title")
print(f"标题：{page_title.text}")

# 直接子元素（>）
item_price = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price")
print(f"第一个商品价格：{item_price.text}")

# ==========================================
# 练习5：获取所有商品名称和价格
# ==========================================
print("\n--- 商品价格列表 ---")

names = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
prices = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")

for i in range(min(5, len(names))):
    print(f"  {i+1}. {names[i].text}  —  {prices[i].text}")

# ==========================================
# 截图
# ==========================================
driver.save_screenshot("saucedemo_products.png")
print("\n截图已保存为 saucedemo_products.png")

time.sleep(2)
driver.quit()
print("浏览器已关闭。")
