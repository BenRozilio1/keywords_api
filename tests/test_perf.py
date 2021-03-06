import random
from fastapi.testclient import TestClient

from src.main import app
from tests.tests_consts import TESTED_KEYWORDS, API_VERSION

test_client = TestClient(app)
keywords = TESTED_KEYWORDS


def test_get_stats_time():
    n = 10000

    # Write data
    data = ""
    for _ in range(n):
        for kw in keywords:
            data += kw
            data += " "

        if random.random() > 0.50:
            data += 'white traffic'
            data += " "

    # sending big chunk, k times.
    k = 2
    for _ in range(k):
        response = test_client.post(f'{API_VERSION}/events', data=data, verify=False)
        print(f'''Write {len(data)} chars,   time:{float(response.headers['X-Process-Time']):.04f}s''')

    # Read data
    interval = 300
    response = test_client.get(f'{API_VERSION}/stats?interval={interval}', verify=False)
    response_body = response.json()

    expected = {'avanan': n * k, 'checkpoint': n * k, 'email': n * k, 'security': n * k}

    assert response.status_code == 200
    assert expected == response_body

    print(f'''Read ,  time:{float(response.headers['X-Process-Time']):.04f}s''')

    print(response_body)
