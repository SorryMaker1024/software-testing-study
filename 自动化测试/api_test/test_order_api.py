"""
订单相关接口测试
"""

import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


class TestOrderAPI:

    def test_get_all_posts(self):
        """获取所有文章（模拟订单列表）"""
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_filter_posts(self):
        """按条件筛选（模拟订单筛选）"""
        response = requests.get(f"{BASE_URL}/posts", params={"userId": 1})
        assert response.status_code == 200
        data = response.json()
        for post in data:
            assert post["userId"] == 1

    def test_create_post(self):
        """创建文章（模拟下单）"""
        payload = {
            "title": "test order",
            "body": "order detail",
            "userId": 1
        }
        response = requests.post(
            f"{BASE_URL}/posts",
            json=payload
        )
        assert response.status_code == 201

    def test_update_post(self):
        """更新文章（模拟修改订单）"""
        payload = {"title": "updated order"}
        response = requests.patch(
            f"{BASE_URL}/posts/1",
            json=payload
        )
        assert response.status_code == 200

    def test_delete_post(self):
        """删除文章（模拟取消订单）"""
        response = requests.delete(f"{BASE_URL}/posts/1")
        assert response.status_code == 200
