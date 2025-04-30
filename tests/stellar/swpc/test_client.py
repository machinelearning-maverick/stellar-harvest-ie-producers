import pytest
import requests
from stellar_harvest_ie_producers.stellar.swpc.client import (
    fetch_planetary_kp_index,
    SWCP_KP_INDEX_URL,
)


class DummyResponse:
    def __init__(self, json_data, status=200):
        self._json = json_data
        self.status_code = status

    def rise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"Status {self.status_code}")

    def json(self):
        return self._json


@pytest.fixture(autouse=True)
def patch_env(monkeypatch):
    # ensure default URL is used
    monkeypatch.delenv("SWCP_KP_INDEX_URL", raising=False)


def test_fetch_success(monkeypatch):
    sample = [{"time_tag": "2025-04-21T23:45:00Z"}]

    def fake_get(url, timeout):
        assert url == SWCP_KP_INDEX_URL
        return DummyResponse(sample, status=200)

    monkeypatch.setattr(requests, "get", fake_get)

    result = fetch_planetary_kp_index()
    assert isinstance(result, list)
    assert result == sample


def test_fetch_http_error(monkeypatch):
    def fake_get(url, timeout):
        return DummyResponse([], status=500)

    monkeypatch.setattr(requests, "get", fake_get)

    with pytest.raises(requests.HTTPError):
        fetch_planetary_kp_index()
