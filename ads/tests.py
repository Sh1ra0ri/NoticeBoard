import pytest
from django.contrib.auth import get_user_model

from ads.models import Ad

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


@pytest.fixture
def admin(db):
    return User.objects.create_user(
        email="admin@test.com",
        password="testpass123",
        first_name="Admin",
        last_name="User",
        phone_number="+71111111111",
        role="admin",
    )


@pytest.fixture
def ad(db, user):
    return Ad.objects.create(
        title="Test Ad",
        price=100,
        description="Test",
        author=user,
    )


@pytest.fixture
def auth_client(client, user):
    response = client.post(
        "/token/", {"email": "test@test.com", "password": "testpass123"}
    )
    client.defaults["HTTP_AUTHORIZATION"] = f'Bearer {response.data["access"]}'
    return client


@pytest.mark.django_db
def test_list_ads_anonymous(client):
    response = client.get("/ads/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_ad(auth_client):
    response = auth_client.post(
        "/ads/",
        {
            "title": "New Ad",
            "price": 200,
            "description": "Desc",
        },
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_delete_own_ad(auth_client, ad):
    response = auth_client.delete(f"/ads/{ad.id}/")
    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_other_ad_forbidden(client, ad, admin):
    other = User.objects.create_user(
        email="other@test.com",
        password="testpass123",
        first_name="Other",
        last_name="User",
        phone_number="+72222222222",
    )
    response = client.post(
        "/token/", {"email": "other@test.com", "password": "testpass123"}
    )
    client.defaults["HTTP_AUTHORIZATION"] = f'Bearer {response.data["access"]}'
    response = client.delete(f"/ads/{ad.id}/")
    assert response.status_code == 403


@pytest.mark.django_db
def test_search_by_title(auth_client, ad):
    response = auth_client.get("/ads/?title=Test")
    assert response.status_code == 200
    assert len(response.data["results"]) == 1
