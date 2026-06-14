# ==========================================
# Day 6 Python 速成 — 8 道动手练习
# ==========================================

# --------------------------------------------------
# 练习1：数据类型 + f-string
# 创建3个变量：姓名、年龄、身高，然后用 f-string 打印一句话
# --------------------------------------------------
name = "张三"
age = 25
height = 1.75
print(f"我叫{name},今年{age}岁，身高{height}米")


# --------------------------------------------------
# 练习2：if/elif/else
# 写一个函数 check_score(score)，根据分数打印等级
# --------------------------------------------------
def check_score(score):
    if score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")

check_score(95)
check_score(70)
check_score(55)


# --------------------------------------------------
# 练习3：列表操作
# 在末尾加10 → 删除0 → 第1个改为33 → 排序打印 → 推导式筛>5的数
# --------------------------------------------------
numbers = [3, 7, 1, 9, 2, 8, 4, 6, 5, 0]

numbers.append(10)       # 末尾加10
numbers.remove(0)        # 删除0
numbers[0] = 33          # 第一个元素改为33
numbers.sort()           # 排序
print(f"排序后：{numbers}")

filtered = [x for x in numbers if x > 5]   # 推导式筛大于5
print(f"大于5的数字：{filtered}")
print(f"长度：{len(filtered)}")


# --------------------------------------------------
# 练习4：字典操作
# 创建字典 → 修改score → 新增email → 删除city → 遍历打印
# --------------------------------------------------
student = {"name": "小明", "age": 20, "score": 85, "city": "上海"}
student["score"] = 92                      # 修改
student["email"] = "xiaoming@test.com"     # 新增
student.pop("city")                        # 删除

for key, value in student.items():
    print(f"{key}: {value}")


# --------------------------------------------------
# 练习5：函数
# 写 login_test(username, password, expected_result)，判断用例是否通过
# --------------------------------------------------
def login_test(username, password, expected_result):
    if username == "admin" and password == "123456":
        actual_result = "pass"
    else:
        actual_result = "fail"

    if actual_result == expected_result:
        print("用例通过")
    else:
        print(f"用例失败：期望登录{expected_result}，实际登录{actual_result}")

login_test("admin", "123456", "pass")   # 期望通过
login_test("admin", "wrong", "fail")    # 期望失败
login_test("admin", "123456", "fail")   # 期望失败但实际通过


# --------------------------------------------------
# 练习6：文件读写
# 写 write_and_read(filename, content)，写入文件再读出来返回
# --------------------------------------------------
def write_and_read(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

result = write_and_read("test.txt", "Hello Python!")
print(f"读出来的内容：{result}")


# --------------------------------------------------
# 练习7：json 模块
# 读 test.json → 遍历打印所有 name → 筛出 score>=80 → 写入 pass.json
# --------------------------------------------------
import json

with open("test.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("所有姓名：")
for item in data:
    print(item["name"])

passed = [x for x in data if x["score"] >= 80]

with open("pass.json", "w", encoding="utf-8") as f:
    json.dump(passed, f, ensure_ascii=False, indent=2)

print(f"及格人数：{len(passed)}，已写入 pass.json")


# --------------------------------------------------
# 练习8：try/except
# 写 safe_divide(a, b)，处理除零和非数字的情况
# --------------------------------------------------
def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "请输入数字"
    elif b == 0:
        return "除数不能为零"
    else:
        return a / b

print(safe_divide(10, 2))       # 5.0
print(safe_divide(10, 0))       # 除数不能为零
print(safe_divide("abc", 2))    # 请输入数字
