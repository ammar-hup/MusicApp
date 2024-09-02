from users.serializers import *
import pytest
from users.models import User
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


class TestEndpoints:
    def test_register_success(self):
        client = APIClient()
        response = client.post("/auth/register/", {
            "username": "remarema",
            "email": "asdfadfsd@gmail.com",
            "password1": "ldifuhtrl23!",
            "password2": "ldifuhtrl23!"
        })
        assert response.status_code == 201

    def test_register_username_missing(self, auth_client):
        client = APIClient()
        payload = dict(
            email="remarema@email.com",
            password1="remaremaF!",
            password2="remaremaF!"
        )
        response = client.post("/auth/register/", payload)
        data = response.data
        assert response.status_code == 400
        assert "username" in data

    def test_register_password_missing(self, auth_client):
        client = APIClient()
        payload = dict(
            username="remarema",
            email="remarema@email.com",
            password1="remaremaF!"
        )
        response = client.post("/auth/register/", payload)
        data = response.data
        assert response.status_code == 400
        assert "password2" in data

    def test_register_password1_missing(self, auth_client):
        client = APIClient()
        payload = dict(
            username="remarema",
            email="remarema@email.com",
            password="remaremaF!",
        )
        response = client.post("/auth/register/", payload)
        data = response.data
        assert response.status_code == 400
        assert "password1" in data

    def test_register_passwords_not_match(self, auth_client):
        client = APIClient()
        payload = dict(
            username="qwerqwer",
            email="qwerqwer@gmail.com",
            password1="reamream1!",
            password2="reamream1!!"
        )
        response = client.post("/auth/register/", payload)
        assert response.status_code == 400

    def test_register_common_password(self, auth_client):
        client = APIClient()
        payload = dict(
            username="asdfasdff",
            email="asdfasdfdf@gmail.com",
            password1="123456789",
            password2="123456789"
        )
        response = client.post("/auth/register/", payload)
        assert response.status_code == 400

    def test_register_invalid_mail(self, auth_client):
        client = APIClient()
        payload = dict(
            username="asdfasdfsdf",
            email="asdfjjsdfiosdif",
            password1="asdfasdfF!",
            password2="asdfasdfF!"
        )
        response = client.post("/auth/register/", payload)
        assert response.status_code == 400

    def test_register_uniqe_username(self, auth_client):
        client = APIClient()
        payload = dict(
            username="asdfasdf",  # same as the user used in auth client
            email="asdfmdlk@gmail.com",
            password1="asdfasdf!1",
            password2="asdfasdf1!"
        )
        response = client.post("/auth/register/", payload)
        assert response.status_code == 400

    def test_register_unique_email(self, auth_client):
        client = APIClient()
        payload = dict(
            username="asdfsdfasdfsd",  # same as the user used in auth client
            email="asdfasdf@gmail.com",
            password1="asdfasdf!1",
            password2="asdfasdf1!"
        )
        response = client.post("/auth/register/", payload)
        assert response.status_code == 400

    def test_login_success(self, user, auth_client):
        client = APIClient()
        response = client.post("/auth/login/", {
            "username": "asdfasdf",
            "password": "asdfasdF1!"
        })
        assert response.status_code == 200
        data = response.data
        assert "token" in data
        assert "user" in data
        assert data['user']['username'] == user.username

    def test_login_fail(self, auth_client):
        client = APIClient()
        payload = {
            "username": "remarema",
            "password": "ldifuhtrl23"
        }
        response = client.post("/auth/login/", payload)
        assert response.status_code == 400

    def test_logout_user(self, auth_client):
        client , id = auth_client()
        response = client.post('/auth/logout/')

        assert response.status_code == 204

    def test_logout_user_unauthenticated(self, client):
        response = client.post('/auth/logout/')

        assert response.status_code == 401