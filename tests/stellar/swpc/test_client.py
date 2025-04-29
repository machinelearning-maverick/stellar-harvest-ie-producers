import pytest
import requests
from stellar_harvest_ie_producers.stellar.swpc.client import fetch_planetary_kp_index

class DummyResponse:
    def __init__(self, json_data, status=200):
        self._json = json_data
        self.status_code = status
    
    def rise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"Status {self.status_code}")
    
    def json(self):
        return self._json
