import pytest
from stellar_harvest_ie_producers.stellar.swpc.client import (
    fetch_latest_planetary_kp_index,
)


def test_fetch_latest_raw():
    data = fetch_latest_planetary_kp_index()

    assert isinstance(data, dict)
