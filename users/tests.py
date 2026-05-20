import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        email="test@test.com",
        password="testpass123",
        first_name="Test",
        last_name="User",
        phone_number="+71234567890",
    )


@pytest.mark.django_db
def test_register(client):
    response = client.post(
        "/users/register/",
        {
            "email": "new@test.com",
            "password": "testpass123",
            "first_name": "New",
            "last_name": "User",
            "phone_number": "+79999999999",
        },
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_login(client, user):
    response = client.post(
        "/token/",
        {
            "email": "test@test.com",
            "password": "testpass123",
        },
    )
    assert response.status_code == 200
    assert "access" in response.data


@pytest.mark.django_db
def test_reset_password(client, user):
    response = client.post("/users/reset_password/", {"email": "test@test.com"})
    assert response.status_code == 200
