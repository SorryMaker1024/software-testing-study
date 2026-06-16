# ==========================================
# Day 8 Selenium — 显式等待 + 窗口切换 + iframe + Select
# ==========================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Edge()
driver.get("https://www.saucedemo.com")

# ==========================================
# 练习1：显式等待 — 等登录页加载好再操作
# ==========================================
print("=== 练习1：显式等待 ===")

# 用显式等待等用户名输入框可点击
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "user-name"))
)
username.send_keys("standard_user")

# 等密码框可点击
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "password"))
)
password.send_keys("secret_sauce")

# 等登录按钮可点击
login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)
login_btn.click()
print("登录成功")

# 等商品列表加载（等某个商品名出现在页面）
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
)
print("商品列表已加载")

# ==========================================
# 练习2：Select 下拉框操作
# ==========================================
print("\n=== 练习2：Select 下拉框 ===")

# SauceDemo 商品排序下拉框
sort_select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))

# 看当前选中了哪个
print(f"当前排序：{sort_select.first_selected_option.text}")

# 列出所有选项
print("可用排序方式：")
for option in sort_select.options:
    print(f"  - {option.text}")

# 按价格从低到高排序
sort_select.select_by_visible_text("Price (low to high)")

# 排序后页面变了，必须重新找 Select 元素（否则 stale element 报错）
sort_select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
print(f"切换后排序：{sort_select.first_selected_option.text}")

# 验证排序生效 — 获取第一个商品价格
first_price = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price")
print(f"第一个商品价格：{first_price.text}")  # 应该是最便宜的

# ==========================================
# 练习3：窗口切换 — 打开新标签页再切回来
# ==========================================
print("\n=== 练习3：窗口切换 ===")

# 用 JS 打开一个新窗口（跳转到百度）
original_window = driver.current_window_handle
driver.execute_script("window.open('https://www.baidu.com', '_blank');")
time.sleep(1)

# 现在有两个窗口了
handles = driver.window_handles
print(f"当前窗口数：{len(handles)}")

# 切到新窗口（百度）
driver.switch_to.window(handles[1])
print(f"新窗口标题：{driver.title}")

# 切回原窗口
driver.switch_to.window(original_window)
print(f"切回原窗口：{driver.title}")

# 切到新窗口，关掉它
driver.switch_to.window(handles[1])
driver.close()
# 切回原窗口后等一下
driver.switch_to.window(original_window)
time.sleep(1)
print("窗口切换完成，继续练习4...")

# ==========================================
# 练习4：iframe 切换（用本地 HTML 文件，不依赖外网）
# ==========================================
print("\n=== 练习4：iframe 切换 ===")

import os
demo_path = os.path.join(os.path.dirname(__file__), "iframe_demo.html")
driver.get(f"file:///{demo_path.replace(chr(92), '/')}")
time.sleep(1)

# 页面上有个 iframe，切进去
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# 现在在 iframe 里面了，可以操作里面的元素
h1_text = driver.find_element(By.TAG_NAME, "h1")
print(f"iframe 里的标题：{h1_text.text}")

# 找里面所有的 <a> 链接
links = driver.find_elements(By.TAG_NAME, "a")
print(f"iframe 里有 {len(links)} 个链接")
for i, link in enumerate(links):
    print(f"  {i+1}. {link.text} → {link.get_attribute('href')}")

# 切回主页面
driver.switch_to.default_content()
main_h1 = driver.find_element(By.TAG_NAME, "h1")
print(f"切回主页面标题：{main_h1.text}")

# ==========================================
# 练习5：综合 — 用显式等待回到 SauceDemo 验证商品排序
# ==========================================
print("\n=== 练习5：综合验证 ===")
driver.get("https://www.saucedemo.com")

# 重新登录
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "user-name"))
).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# 等商品列表加载
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
)

# 按价格排序
Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("lohi")

# 获取排序后的所有价格
prices = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
price_values = [float(p.text.replace("$", "")) for p in prices]
print(f"价格列表（已排序）：{price_values}")

# assert 验证：第一个应该是最便宜的
assert price_values[0] == min(price_values), "排序错误！"
print("✅ 排序验证通过！最便宜的是 ${:.2f}".format(price_values[0]))

# 截图
driver.save_screenshot("day8_result.png")
print("\n截图已保存")

time.sleep(2)
driver.quit()
print("浏览器已关闭")
