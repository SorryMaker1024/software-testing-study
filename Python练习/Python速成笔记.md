# Python 速成笔记

> 目的：够写 Selenium + pytest 自动化脚本就行，不追求精通
> 你计算机专业出身，重点放在和 Java/C 不一样的地方

---

## 一、变量和数据类型

### 不需要声明类型

```python
# Python 是动态类型，不用写 int x = 10;
name = "zhangsan"
age = 25
height = 1.75
is_student = True
```

### 6 种常用类型

| 类型 | 写法 | 例子 | 面试常问 |
|------|------|------|----------|
| int | 整数 | `10`, `-5` | |
| float | 小数 | `3.14`, `0.0` | |
| str | 单引号或双引号 | `'hello'`, `"hello"` | |
| bool | 首字母大写 | `True`, `False` | ⚠️ 不是 true/false |
| None | 空值 | `None` | ⚠️ 不是 null |
| list | 中括号 | `[1, 2, 3]` | |
| dict | 花括号键值对 | `{"name": "zhangsan"}` | |
| tuple | 小括号不可变 | `(1, 2)` | 和 list 区别必考 |

### f-string 字符串格式化（最常用）

```python
name = "张三"
age = 25
print(f"我叫{name}，今年{age}岁")  # 我叫张三，今年25岁
```

### 类型转换

```python
int("10")     # 10
str(100)      # "100"
float("3.14") # 3.14
bool("")      # False — 空字符串转bool是False
bool("hello") # True — 非空字符串是True
```

---

## 二、条件判断

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

**和 Java/C 的区别**：没有 `{}`，靠缩进（4个空格），冒号不能忘。

### 多条件组合

```python
if age >= 18 and age <= 60:    # 不是 &&
    print("成年人")

if status == "A" or status == "B":  # 不是 ||
    print("有效状态")

if not is_deleted:              # 不是 !
    print("未删除")
```

---

## 三、循环

### for 循环（常用）

```python
# 遍历列表
names = ["张三", "李四", "王五"]
for name in names:
    print(name)

# range 生成数列
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):    # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8（步长2）
    print(i)
```

### while 循环

```python
count = 0
while count < 5:
    print(count)
    count += 1  # Python 没有 count++
```

### break 和 continue（和 C 一样）

```python
for i in range(10):
    if i == 3:
        continue   # 跳过本次
    if i == 7:
        break      # 跳出循环
    print(i)
```

---

## 四、列表操作（最常用）

```python
# 创建
fruits = ["苹果", "香蕉", "橘子"]

# 增
fruits.append("西瓜")          # 加到末尾
fruits.insert(1, "草莓")       # 插到位置1

# 删
fruits.remove("香蕉")          # 按值删除
fruits.pop(0)                  # 按位置删除，删第一个
fruits.clear()                 # 全部清空

# 查
fruits[0]                      # 取第一个
fruits[-1]                     # 取最后一个（负数从右数）
fruits[0:2]                    # 切片：取前两个，不含位置2

# 改
fruits[0] = "榴莲"

# 长度
len(fruits)

# 判断存在
if "苹果" in fruits:
    print("有苹果")

# 列表推导式（Python 特色写法）
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

### 列表 vs 元组（面试必问）

| | list | tuple |
|------|------|------|
| 写法 | `[1, 2, 3]` | `(1, 2, 3)` |
| 能改吗 | 能增删改 | ❌ 创建后不能改 |
| 场景 | 数据会变 | 固定配置、坐标、函数返回多值 |

---

## 五、字典操作（最常用 No.2）

```python
# 创建
user = {"name": "张三", "age": 25, "city": "宁波"}

# 取值
user["name"]       # "张三"
user.get("age")    # 25
user.get("phone", "没填")  # 没这key就返回默认值，不报错

# 增/改
user["phone"] = "13800138000"   # 新增
user["age"] = 26                # 修改

# 删
user.pop("city")   # 删除city

# 遍历
for key, value in user.items():
    print(f"{key}: {value}")

# 拿所有 key / value
user.keys()      # dict_keys(['name', 'age', 'phone'])
user.values()    # dict_values(['张三', 26, '13800138000'])
```

---

## 六、函数

```python
def 函数名(参数):
    """这是函数的说明"""
    # 函数体
    return 结果

# 例子
def login(username, password, retry=3):
    """登录函数，retry 有默认值"""
    for i in range(retry):
        if username == "admin" and password == "123456":
            return True
    return False

# 调用
login("admin", "123456")           # 位置传参
login(password="123", username="a") # 关键字传参，顺序无所谓
```

### 和 Java 的区别

```python
# Python 函数是一等公民，可以赋值给变量
def add(a, b):
    return a + b

func = add       # 把函数赋给变量
func(1, 2)       # 3

# 没有函数重载 — 同名函数后定义的会覆盖前一个
```

---

## 七、文件读写

```python
# 读文件
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()           # 读整个文件
    # lines = f.readlines()      # 读成列表，每行一个元素

# 写文件
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python\n")
    f.write("第二行")

# 追加模式
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("追加一行\n")
```

读写模式：
- `r` — 只读
- `w` — 覆盖写入（文件不存在就创建）
- `a` — 追加写入
- `r+` — 读写

**用 `with` 的好处**：自动关闭文件，不用写 `f.close()`

---

## 八、try/except 异常处理

```python
try:
    num = int(input("请输入数字："))
    result = 100 / num
    print(f"结果是{result}")

except ValueError:
    print("你输的不是数字！")

except ZeroDivisionError:
    print("不能除以0！")

except Exception as e:
    print(f"其他错误：{e}")

finally:
    print("不管有没有异常，这里都会执行")
```

**自动化测试里最常用**：避免一条用例挂了导致整个脚本崩掉。

```python
def test_case_001():
    try:
        driver.find_element(...).click()
        return True
    except Exception as e:
        print(f"用例失败：{e}")
        return False
```

---

## 九、json 模块（接口测试必用）

```python
import json

# 字符串 → 字典/列表
json_str = '{"name": "张三", "age": 25}'
data = json.loads(json_str)       # loads = load string
print(data["name"])               # 张三

# 字典/列表 → 字符串
user = {"name": "李四", "age": 30}
json_str = json.dumps(user, ensure_ascii=False)  # dumps = dump string
print(json_str)  # {"name": "李四", "age": 30}

# 读 JSON 文件
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)           # load = 从文件读

# 写 JSON 文件
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)  # dump = 写到文件
```

---

## 十、Python 和 Java/C 的速查对照

| Java/C | Python |
|--------|--------|
| `int x = 10;` | `x = 10` |
| `String s = "hello";` | `s = "hello"` |
| `&&` `\|\|` `!` | `and` `or` `not` |
| `true` `false` | `True` `False` |
| `null` | `None` |
| `x++` `x--` | `x += 1` `x -= 1` |
| `{}` 代码块 | 缩进（4空格） |
| `//` 单行注释 | `#` 单行注释 |
| `/* */` 多行注释 | `""" """` 多行注释 |
| `for (int i=0; i<10; i++)` | `for i in range(10)` |
| `array.length` | `len(array)` |
| `switch/case` | `match/case`（Python 3.10+） |
| `public void foo()` | `def foo():` |
| 分号结尾 | ❌ 不需要分号 |

---

## 学习检查

- [✓] 能写出变量声明和 6 种数据类型
- [✓] 会写 if/elif/else 和 for/while
- [✓] 熟练操作 list：增删改查、切片、列表推导式
- [✓] 能说清楚 list 和 tuple 的区别
- [✓] 熟练操作 dict：增删改查、遍历 items()
- [✓] 能定义函数，知道位置参数和默认参数
- [✓] 会用 with open 读写文件和 json 模块
- [✓] 会用 try/except 包住可能报错的代码

---

## 今天动手练习

打开 VS Code 或者直接在命令行 `python` 交互模式，逐块敲一遍上面这些代码。

验证自己会了的标志：
1. 不看笔记，能写出一个函数 `read_json_file(path)`，读 JSON 文件返回 dict
2. 能用列表推导式生成 1-100 的平方数列表
3. 能写 for 循环遍历字典
