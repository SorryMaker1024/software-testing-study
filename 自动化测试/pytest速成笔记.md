# pytest 速成笔记

> pytest 是 Python 最流行的测试框架，比 unittest 简洁得多。
> 核心思路：**把 Selenium 脚本拆成一条条独立的测试用例，用 assert 自动判断对错。**

---

## 1. 用例命名规则

```
规则很简单：
  文件名   → test_ 开头，如 test_login.py
  函数名   → test_ 开头，如 test_valid_login()
  类名     → Test 开头，如 TestLogin
```

pytest 运行时会自动发现这些函数，不需要手动注册。

---

## 2. assert 断言（核心）

pytest 不需要 `self.assertEqual()` 之类的啰嗦写法，直接 `assert`：

```python
# ✅ 通过
assert driver.title == "Swag Labs"

# ❌ 失败 — pytest 会自动显示 期望值 vs 实际值
assert 1 + 1 == 3
```

pytest 的 assert 失败时会自动展开变量值，告诉你哪里不对。

---

## 3. fixture — 前置/后置（替代 setup/teardown）

测试用例之间需要共享的东西（如打开浏览器），用 `fixture`：

```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """每个测试用例执行前打开浏览器，执行后关闭"""
    d = webdriver.Edge()
    d.get("https://www.saucedemo.com")
    yield d        # yield 前 = setup，yield 后 = teardown
    d.quit()
```

`yield` 是 Python 的生成器语法，pytest 用它的位置来区分：
- `yield` **之前** → setup（测试开始前执行）
- `yield` **之后** → teardown（测试结束后执行）

---

## 4. 参数化 @pytest.mark.parametrize

同一段测试逻辑，换不同数据跑多次：

```python
@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", True),    # 正确账号
    ("locked_out_user", "secret_sauce", False),  # 被锁账号
    ("", "", False),                             # 空账号
])
def test_login(driver, username, password, expected):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    
    if expected:
        assert "inventory" in driver.current_url
    else:
        assert "error" in driver.page_source or "locked" in driver.page_source
```

一条代码跑 3 组数据，pytest 会显示 3 条结果（3 passed / 2 passed 1 failed 等）。

---

## 5. 运行方式

```bash
# 运行所有测试
python -m pytest

# 运行指定文件
python -m pytest 自动化测试/test_demo.py

# -v 显示详细信息（每个用例名都打印）
python -m pytest -v

# -s 不捕获 print（调试时用）
python -m pytest -s

# -k 按关键词筛选用例
python -m pytest -k "login"      # 只运行名字含 login 的用例

# --html 生成 HTML 报告
python -m pytest --html=report.html --self-contained-html

# 只运行某条用例
python -m pytest 自动化测试/test_demo.py::test_login_success
```

---

## 6. conftest.py — 共享 fixture

如果多个测试文件都要用同一个 fixture，放到 `conftest.py`：

```
自动化测试/
├── conftest.py          ← 公共 fixture 放这里（自动生效，不需要 import）
├── test_login.py
└── test_products.py
```

```python
# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")  # function = 每个用例都新建浏览器（默认）
def driver():
    d = webdriver.Edge()
    yield d
    d.quit()

@pytest.fixture(scope="session")   # session = 整个测试只开一次浏览器
def shared_driver():
    d = webdriver.Edge()
    yield d
    d.quit()
```

`scope` 决定了 fixture 的生命周期：
- `function`（默认）：每个用例都执行一次 setup + teardown
- `class`：每个测试类执行一次
- `module`：每个 .py 文件执行一次
- `session`：整个测试过程只执行一次

---

## 7. 项目文件结构

```
自动化测试/
├── conftest.py           # 公共 fixture（driver 放这里）
├── pages/                # Page Object 模式（进阶）
│   ├── login_page.py
│   └── inventory_page.py
├── test_login.py         # 登录相关用例
├── test_products.py      # 商品相关用例
├── test_sort.py          # 排序相关用例
└── report.html           # 生成的测试报告
```

---

## 8. pytest vs unittest 对比

| | unittest | pytest |
|---|---|---|
| 用例发现 | 继承 TestCase | 文件名/函数名 test_ 开头自动发现 |
| 断言 | self.assertEqual(a, b) | assert a == b（原生 Python） |
| 前后置 | setUp/tearDown | fixture + yield |
| 参数化 | 需要 ddt 库 | 内置 @parametrize |
| 报告 | 需要第三方 | pytest-html 一条命令 |
| 社区 | Java JUnit 风格 | Python 社区首选 |

---

> 一句话总结：pytest = 把你写的 Selenium 脚本改成都以 `test_` 开头的函数，参数全用 `assert` 而不是 `print`。
