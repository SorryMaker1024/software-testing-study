# Selenium WebDriver 速成笔记

> 目标：能写脚本自动打开浏览器、定位元素、点击、输入、获取内容
> 重点：xpath 和 css_selector 两个定位方式，实际工作最常用

---

## 一、Selenium 是什么

Selenium 是一个浏览器自动化工具。你可以用 Python 代码控制浏览器：
- 打开网页
- 找到页面上的按钮/输入框
- 自动点击、输入文字
- 读取页面内容做断言

**就像一个机器人在操作你的浏览器。**

测试场景举例：
```
1. 打开淘宝首页
2. 搜索框输入 "机械键盘"
3. 点击搜索按钮
4. 获取搜索结果数量
5. 截图保存
```

---

## 二、第一个脚本：打开浏览器访问网页

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 创建浏览器对象
driver = webdriver.Chrome()

# 打开一个网页
driver.get("https://www.baidu.com")

# 打印当前页面标题
print(f"页面标题：{driver.title}")

# 等2秒看看效果（后面会学更好的等待方式）
import time
time.sleep(2)

# 关闭浏览器
driver.quit()
```

**Selenium 4.6+ 不需要手动下载 chromedriver**，它会自动管理。

---

## 三、8 种元素定位方式

定位就是告诉 Selenium "我要操作的是页面上的哪个元素"。就像在页面上用手指指出"这个按钮"。

| 定位方式 | 怎么用 | 频率 |
|----------|--------|------|
| `By.ID` | `driver.find_element(By.ID, "kw")` | ⭐⭐⭐ |
| `By.NAME` | `driver.find_element(By.NAME, "wd")` | ⭐⭐⭐ |
| `By.CLASS_NAME` | `driver.find_element(By.CLASS_NAME, "s_ipt")` | ⭐⭐ |
| `By.TAG_NAME` | `driver.find_element(By.TAG_NAME, "input")` | ⭐ |
| `By.LINK_TEXT` | `driver.find_element(By.LINK_TEXT, "新闻")` | ⭐⭐ |
| `By.PARTIAL_LINK_TEXT` | `driver.find_element(By.PARTIAL_LINK_TEXT, "新")` | ⭐ |
| `By.XPATH` | `driver.find_element(By.XPATH, "//input[@id='kw']")` | ⭐⭐⭐⭐ |
| `By.CSS_SELECTOR` | `driver.find_element(By.CSS_SELECTOR, "#kw")` | ⭐⭐⭐⭐ |

**xpath 和 css_selector 是必须重点掌握的**，因为很多元素没有 id 也没有 name，只能靠它们定位。

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 8种方式定位百度搜索框（都能找到同一个输入框）：
# 1. 通过 id
driver.find_element(By.ID, "kw")

# 2. 通过 name
driver.find_element(By.NAME, "wd")

# 3. 通过 class
driver.find_element(By.CLASS_NAME, "s_ipt")

# 4. 通过标签名（不推荐，input太多了）
driver.find_element(By.TAG_NAME, "input")

# 5. 通过链接文字——找页面上的链接
driver.find_element(By.LINK_TEXT, "新闻")

# 6. 通过部分链接文字
driver.find_element(By.PARTIAL_LINK_TEXT, "新")

# 7. 通过 xpath（★★★★★ 最重要）
driver.find_element(By.XPATH, "//input[@id='kw']")

# 8. 通过 css_selector（★★★★★ 最重要）
driver.find_element(By.CSS_SELECTOR, "#kw")
driver.find_element(By.CSS_SELECTOR, "input.s_ipt")

driver.quit()
```

---

## 四、xpath 详解（面试+工作必备）

xpath 就是给元素写一条"路径"，像文件路径一样定位到它。

### 4.1 绝对路径 vs 相对路径

```python
# 绝对路径（从根开始，一长串）—— 不推荐，页面一改就失效
# /html/body/div[1]/div[2]/div/input

# 相对路径（推荐）
# //input[@id='kw']
```

### 4.2 常用 xpath 写法

| 写法 | 含义 | 例子 |
|------|------|------|
| `//标签名[@属性='值']` | 属性匹配 | `//input[@id='kw']` |
| `//*[@id='kw']` | 任意标签，只要 id 匹配 | `//*[@name='wd']` |
| `//标签名[contains(@属性, '值')]` | 属性包含某值 | `//input[contains(@class, 's_ipt')]` |
| `//标签名[text()='文字']` | 精确文字匹配 | `//a[text()='新闻']` |
| `//标签名[contains(text(), '文字')]` | 文字包含 | `//a[contains(text(), '新')]` |
| `//input[@id='kw' and @name='wd']` | 多条件（and） | 同时满足两个属性 |
| `//input[@id='kw' or @name='xxx']` | 多条件（or） | 满足任一即可 |

### 4.3 xpath 轴（上级/下级/兄弟）

```python
# 找父元素
# //span[@class='txt']/..

# 找子元素
# //div[@id='box']/span

# 找兄弟元素（同级的下一个）
# //span[@class='txt']/following-sibling::input

# 找前面的兄弟
# //input[@id='kw']/preceding-sibling::span
```

---

## 五、css_selector 详解

比 xpath 更简洁，运行更快。

| 写法 | 含义 | 等价 xpath |
|------|------|------------|
| `#kw` | id=kw | `//*[@id='kw']` |
| `.s_ipt` | class=s_ipt | `//*[@class='s_ipt']` |
| `input#kw` | input标签且id=kw | `//input[@id='kw']` |
| `input.s_ipt` | input标签且class=s_ipt | `//input[@class='s_ipt']` |
| `[name='wd']` | 属性name=wd | `//*[@name='wd']` |
| `input[name='wd']` | input标签且name=wd | `//input[@name='wd']` |
| `div > input` | 直接子元素 | 父子关系 |
| `div input` | 后代元素 | 任意层级 |
| `input[name*='w']` | 属性包含 | `//input[contains(@name, 'w')]` |
| `input[name^='w']` | 属性以w开头 | |
| `input[name$='d']` | 属性以d结尾 | |

---

## 六、元素操作

找到元素后，要能操作它：

```python
element = driver.find_element(By.ID, "kw")

# 输入文字
element.send_keys("机械键盘")

# 清空输入框
element.clear()

# 点击
element.click()

# 获取元素上的文字
print(element.text)

# 获取元素属性（比如 href、class、value 等）
print(element.get_attribute("value"))

# 获取元素属性（比如 href、class、value 等）
print(element.get_attribute("class"))

# 判断元素是否显示在页面上
print(element.is_displayed())

# 判断元素是否可用
print(element.is_enabled())

# 判断元素是否被选中（checkbox/radio）
print(element.is_selected())
```

---

## 七、等待机制（面试必问）

页面加载需要时间，如果元素还没出来就去操作，会报错。

### 7.1 强制等待（最低级）

```python
import time
time.sleep(3)  # 硬等3秒，不管元素出来没
```

❌ 缺点：浪费时间，元素早出来了也在等

### 7.2 隐式等待（全局设置）

```python
driver.implicitly_wait(10)  # 最多等10秒，元素一出现就继续
```

✅ 设置一次，全局有效。元素早出来早继续。

### 7.3 显式等待（★★★ 最推荐）

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 等某个元素出现（可点击），最多等10秒
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "kw"))
)

# element_to_be_clickable — 可点击
# presence_of_element_located — 元素出现在DOM
# visibility_of_element_located — 元素可见
# text_to_be_present_in_element — 文字出现
```

✅ 最灵活，只等需要的元素，到了就继续。

---

## 八、窗口和 iframe 切换

### 8.1 窗口切换

```python
# 点击一个链接打开了新窗口
driver.find_element(By.LINK_TEXT, "打开新窗口").click()

# 获取所有窗口句柄
handles = driver.window_handles
print(f"当前有 {len(handles)} 个窗口")

# 切换到新窗口
driver.switch_to.window(handles[-1])  # handles[0]是第一个窗口

# 切回原来的窗口
driver.switch_to.window(handles[0])
```

### 8.2 iframe 切换

iframe 就是页面里套了另一个页面，必须切进去才能操作里面的元素。

```python
# 方式1：通过 iframe 的 id/name
driver.switch_to.frame("iframe_id")

# 方式2：先找到 iframe 元素再切换
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# 操作完 iframe 里的元素后，切回主页面
driver.switch_to.default_content()
```

---

## 九、截图

```python
# 截整个页面
driver.save_screenshot("screenshot.png")

# 截某个元素
element = driver.find_element(By.ID, "kw")
element.screenshot("element.png")
```

---

## 十、Select 下拉框

```python
from selenium.webdriver.support.ui import Select

select_element = driver.find_element(By.ID, "province")
select = Select(select_element)

# 三种选择方式
select.select_by_value("zhejiang")        # 按 value 属性选
select.select_by_visible_text("浙江省")    # 按可见文字选（最常用）
select.select_by_index(1)                 # 按位置选（从0开始）

# 获取当前选中的选项
print(select.first_selected_option.text)

# 获取所有选项
for option in select.options:
    print(option.text)
```

---

## 学习检查

- [ ] 能写脚本打开 Chrome 访问任意网页
- [ ] 能用 ID / NAME / CLASS 定位元素
- [ ] 能手写 xpath 定位（含 contains、多条件）
- [ ] 能手写 css_selector 定位（#id、.class、[属性]）
- [ ] 能执行 click / send_keys / text / get_attribute
- [ ] 能说清楚三种等待的区别：sleep vs 隐式等待 vs 显式等待
- [ ] 能切换窗口和 iframe
- [ ] 能操作 Select 下拉框
- [ ] 实操：打开百度搜索关键词，获取前10条结果标题

---

## 今日实操任务

1. **打开百度，搜索"软件测试"**
   - 定位搜索框，输入"软件测试"
   - 点击"百度一下"
   - 等待结果加载

2. **获取搜索结果**
   - 用 css_selector 或 xpath 定位结果列表
   - 打印前10条结果的标题
   - 截图保存

3. **放到 `day7_selenium.py` 文件里**
   - 用注释分隔每一步
   - 用 try/except 包住关键操作
