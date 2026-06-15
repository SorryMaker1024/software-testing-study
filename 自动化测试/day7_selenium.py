# ==========================================
# Day 7 Selenium 自动化 — 第一个脚本
# ==========================================

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --------------------------------------------------
# 步骤1：打开 Edge 浏览器，访问搜索页面
# --------------------------------------------------
driver = webdriver.Edge()
# 直接跳到搜索页，跳过首页的输入问题
driver.get("https://www.baidu.com/s?wd=软件测试")
time.sleep(3)

print(f"当前页面标题：{driver.title}")

# --------------------------------------------------
# 步骤2：获取前10条搜索结果标题
# --------------------------------------------------
try:
    titles = driver.find_elements(By.CSS_SELECTOR, "h3 a")
    # 过滤掉空标题
    titles = [t for t in titles if t.text.strip()]

    if titles:
        print(f"\n获取到前 {min(10, len(titles))} 条结果：\n")
        for i, title in enumerate(titles[:10]):
            print(f"{i+1}. {title.text}")
    else:
        print("h3 a 没找到，换 xpath 试试...")
        # 百度新版可能用不同的结构
        titles = driver.find_elements(By.XPATH, "//h3/a | //h3//a")
        titles = [t for t in titles if t.text.strip()]
        print(f"\n获取到前 {min(10, len(titles))} 条结果：\n")
        for i, title in enumerate(titles[:10]):
            print(f"{i+1}. {title.text}")

except Exception as e:
    print(f"获取结果失败：{e}")

# --------------------------------------------------
# 步骤3：截图保存
# --------------------------------------------------
driver.save_screenshot("baidu_search_result.png")
print("\n截图已保存为 baidu_search_result.png")

# --------------------------------------------------
# 步骤4：关闭浏览器
# --------------------------------------------------
time.sleep(2)
driver.quit()
print("浏览器已关闭。")
