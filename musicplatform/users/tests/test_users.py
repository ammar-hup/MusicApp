import pytest
from django.urls import reverse
from users.models import User

@pytest.mark.django_db
class TestUser:
    def test_get_user(self, auth_client):
        client, user_id = auth_client()
        user = User.objects.get(id=user_id)
        url = reverse('user-detail', kwargs={'pk': user_id})
        response = client.get(url)
        assert response.status_code == 200
        data = response.data
        assert data['username'] == user.username
        assert data['email'] == user.email
        assert data['bio'] == user.bio

    def test_put_method(self, auth_client):
        client, user_id = auth_client()
        url = reverse('user-detail', kwargs={'pk': user_id})
        response = client.put(url, {
            "username": "Update",
            "email": "a@gmail.com",
            "bio": "Success"
        })
        assert response.status_code == 200
        user = User.objects.get(id=user_id)  # Refresh user from db
        assert user.bio == "Success"
        assert user.username == "Update"
        assert user.email == "a@gmail.com"

    def test_patch_method(self, auth_client):
        client, user_id = auth_client()
        url = reverse('user-detail', kwargs={'pk': user_id})
        response = client.patch(url, {
            "username": "updatedUserName",
        })
        assert response.status_code == 200
        user = User.objects.get(id=user_id)  # Refresh user from db
        assert user.username == "updatedUserName"