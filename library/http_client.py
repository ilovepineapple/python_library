import requests
from library.error_handler import handle_error

class HttpClient:
    def __init__(self, base_url, timeout=5):
        self.base_url = base_url
        self.timeout = timeout

    @handle_error
    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}/{endpoint}", params=params, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    @handle_error
    def post(self, endpoint, data=None, json=None):
        response = requests.post(f"{self.base_url}/{endpoint}", data=data, json=json, timeout=self.timeout)
        response.raise_for_status()
        return response.json()
