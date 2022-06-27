from fastapi.testclient import TestClient

from src.main import app

test_client = TestClient(app)


def test_post_event():
    data = {"text": "Avanan is a leading Enterprise Solution for Cloud Email and Collaboration Security"}

    response = test_client.post('/events', json=data, verify=False)
    response_body = response.json()

    expected = {"avanan": 1, "email": 1, "security": 1}

    assert response.status_code == 201
    assert expected == response_body


def test_get_stats():
    interval = 90
    response = test_client.get(f'/stats/{interval}', verify=False)
    response_body = response.json()

    expected = {}

    assert response.status_code == 200
    assert expected == response_body
