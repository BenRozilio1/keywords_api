from fastapi.testclient import TestClient

from src.main import app
from tests.tests_consts import API_VERSION

test_client = TestClient(app)


def test_post_event():
    data = "Avanan is a leading Enterprise Solution for Cloud Email and Collaboration Security"

    response = test_client.post(f'{API_VERSION}/events', data=data, verify=False)
    response_body = response.json()

    expected = "event received"
    assert response.status_code == 201
    assert expected == response_body


def test_get_stats():
    interval = 90
    response = test_client.get(f'{API_VERSION}/stats?interval={interval}', verify=False)
    response_body = response.json()

    expected = {}

    assert response.status_code == 200
    assert expected == response_body


def test_post_get():
    data = "Avanan is a leading Enterprise Solution for Cloud Email and Collaboration Security"
    response = test_client.post(f'{API_VERSION}/events', data=data, verify=False)
    response_body = response.json()

    expected = "event received"

    assert response.status_code == 201
    assert expected == response_body

    interval = 10
    response = test_client.get(f'{API_VERSION}/stats?interval={interval}', verify=False)
    response_body = response.json()

    expected = {'avanan': 1, 'email': 1, 'security': 1}

    assert response.status_code == 200
    assert expected == response_body

    more_data = "Checkpoint and Avanan is Rock in cyber security Products"
    response = test_client.post(f'{API_VERSION}/events', data=more_data, verify=False)
    response_body = response.json()

    expected = "event received"
    assert response.status_code == 201
    assert expected == response_body

    response = test_client.get(f'{API_VERSION}/stats?interval={interval}', verify=False)
    response_body = response.json()

    expected = {'avanan': 2, 'checkpoint': 1, 'email': 1, 'security': 2}

    assert response.status_code == 200
    assert expected == response_body
