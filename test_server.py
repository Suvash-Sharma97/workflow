import requests


def test_status():
    url = 'http://127.0.0.1:5000/status'
    response = requests.get(url)
    assert response.json() == {'status': 'ok'}

def test_sum_numbers():
    url = 'http://127.0.0.1:5000/sum?a=3&b=5'
    resp = requests.get(url)
    assert resp.json() == {'sum': 8}