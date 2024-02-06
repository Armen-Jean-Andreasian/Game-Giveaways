import time
import requests

BASE_URL = 'http://127.0.0.1:8000/'

def get_url(url):
    return requests.get(url)


if __name__ == '__main__':
    ip = BASE_URL

    assert get_url(BASE_URL).status_code == 200
    assert get_url(BASE_URL).status_code == 429
    time.sleep(5)
    assert get_url(BASE_URL).status_code == 200
