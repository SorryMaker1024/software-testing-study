"""
用户相关接口测试
"""

import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"  # 示例公开 API


class TestUserAPI:

    def test_get_all_users(self):
        """获取所有用户"""
        response = requests.get(f"{BASE_URL}/users")
        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_get_single_user(self):
        """获取单个用户"""
        response = requests.get(f"{BASE_URL}/users/1")
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "email" in data

    def test_create_user(self):
        """创建用户"""
        payload = {
            "name": "test user",
            "email": "test@example.com"
        }
        response = requests.post(
            f"{BASE_URL}/users",
            json=payload
        )
        assert response.status_code == 201

    def test_user_not_found(self):
        """查询不存在的用户"""
        response = requests.get(f"{BASE_URL}/users/99999")
        assert response.status_code == 404
