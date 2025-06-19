import pytest
from django.test import Client

client = Client()

@pytest.mark.django_db
def test_product_list_empty(monkeypatch):
    from chatbot.services.product_service import get_all_products

    # Patch pour éviter la vraie connexion Mongo
    monkeypatch.setattr(get_all_products, "__call__", lambda: [])

    response = client.get("/api/products/")
    assert response.status_code == 200
    assert response.json() == []