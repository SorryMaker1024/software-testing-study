# ==========================================
# Day 9 接口测试 — Python Requests + pytest
# 练习 API：jsonplaceholder（免费假数据 REST API）
# ==========================================
import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# ==========================================
# 用例1：GET 获取列表
# ==========================================
def test_get_posts():
    """获取所有帖子，验证返回200且数据不为空"""
    res = requests.get(f"{BASE_URL}/posts")

    # 断言1：状态码 200
    assert res.status_code == 200, f"状态码应为200，实际{res.status_code}"

    # 断言2：返回的是列表
    posts = res.json()
    assert isinstance(posts, list), "应返回列表"
    assert len(posts) > 0, "列表不应为空"

    print(f"获取到 {len(posts)} 条帖子")


# ==========================================
# 用例2：GET 获取单条
# ==========================================
def test_get_single_post():
    """获取帖子 #1，验证字段完整"""
    res = requests.get(f"{BASE_URL}/posts/1")

    assert res.status_code == 200

    post = res.json()
    # 验证必需字段都存在
    assert "userId" in post, "缺少 userId"
    assert "id" in post, "缺少 id"
    assert "title" in post, "缺少 title"
    assert "body" in post, "缺少 body"
    assert post["id"] == 1

    print(f"帖子标题：{post['title']}")


# ==========================================
# 用例3：GET 带参数 — 按 userId 过滤
# ==========================================
def test_get_posts_by_user():
    """获取 userId=1 的帖子"""
    res = requests.get(f"{BASE_URL}/posts", params={"userId": 1})

    assert res.status_code == 200

    posts = res.json()
    # 验证每条帖子的 userId 都是 1
    for post in posts:
        assert post["userId"] == 1, f"userId 应为1，实际{post['userId']}"

    print(f"userId=1 有 {len(posts)} 条帖子")


# ==========================================
# 用例4：POST 创建数据
# ==========================================
def test_create_post():
    """POST 新增一条帖子"""
    new_post = {
        "title": "pytest 接口测试",
        "body": "用 requests 发 POST 请求",
        "userId": 1
    }
    res = requests.post(f"{BASE_URL}/posts", json=new_post)

    # POST 成功应返回 201
    assert res.status_code == 201, f"状态码应为201，实际{res.status_code}"

    data = res.json()
    assert data["title"] == new_post["title"]
    assert data["body"] == new_post["body"]
    assert "id" in data  # 服务器应自动生成 id

    print(f"创建成功，新帖子的 id：{data['id']}")


# ==========================================
# 用例5：PUT 修改数据
# ==========================================
def test_update_post():
    """PUT 全量修改帖子 #1"""
    updated = {
        "id": 1,
        "title": "修改后的标题",
        "body": "修改后的内容",
        "userId": 2
    }
    res = requests.put(f"{BASE_URL}/posts/1", json=updated)

    assert res.status_code == 200

    data = res.json()
    assert data["title"] == "修改后的标题"

    print(f"修改成功：{data['title']}")


# ==========================================
# 用例6：DELETE 删除数据
# ==========================================
def test_delete_post():
    """DELETE 删除帖子 #1"""
    res = requests.delete(f"{BASE_URL}/posts/1")

    assert res.status_code == 200

    print("删除成功")


# ==========================================
# 用例7：404 — 资源不存在
# ==========================================
def test_not_found():
    """请求不存在的资源，验证返回404"""
    res = requests.get(f"{BASE_URL}/posts/99999")

    assert res.status_code == 404

    print("正确返回404")


# ==========================================
# 用例8：验证响应头
# ==========================================
def test_content_type():
    """GET 请求返回的应是 JSON 格式"""
    res = requests.get(f"{BASE_URL}/posts/1")

    assert res.status_code == 200
    content_type = res.headers.get("Content-Type", "")
    assert "application/json" in content_type, f"Content-Type 应为 json，实际{content_type}"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
