from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_valid_payment():
    response = client.post(
        "/payments",
        json={
            "card_id": 1,
            "amount": 100
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "transaction_id" in data
    assert data["card_id"] == 1
    assert data["amount"] == 100
    assert data["status"] in ["SUCCESS", "FAILED"]


def test_invalid_amount():
    response = client.post(
        "/payments",
        json={
            "card_id": 1,
            "amount": -100
        }
    )

    assert response.status_code == 422