import pytest
from stellar_harvest_ie_producers.stellar.swpc.parser import (
    parse_latest_planetary_kp_index,
)
from stellar_harvest_ie_models.stellar.swpc.models import KpIndexRecord


def test_parse_latest_planetary_kp_index_correct():
    raw_record = {
        "time_tag": "2025-04-21T23:45:00Z",
        "kp_index": 2,
        "mid_latitude_kp_index": 3,
        "dst": -24.5,
        "source": "NOAA",
    }

    record = parse_latest_planetary_kp_index(raw_record)
    assert isinstance(record, KpIndexRecord)
    assert record.kp_index == 2
    assert record.dst == -24.5


@pytest.mark.parametrize("payload", [[], [{}]])
def test_parse_latest_planetary_kp_index_failure(payload):
    with pytest.raises(Exception):
        parse_latest_planetary_kp_index(payload)
