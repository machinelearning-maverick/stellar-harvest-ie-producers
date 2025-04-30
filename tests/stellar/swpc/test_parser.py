import pytest
from stellar_harvest_ie_producers.stellar.swpc.parser import parse_latest
from stellar_harvest_ie_models.stellar.swpc.models import KpIndexRecord


def test_parse_latest_correct():
    raw = [
        {
            "time_tag": "2025-04-21T23:45:00Z",
            "kp_index": 2,
            "mid_latitude_kp_index": 3,
            "dst": -24.5,
            "source": "NOAA",
        },
        {
            "time_tag": "2025-04-21T23:46:00Z",
            "kp_index": 4,
            "mid_latitude_kp_index": 5,
            "dst": -22.1,
            "source": "NOAA",
        },
    ]

    record = parse_latest(raw)
    assert isinstance(record, KpIndexRecord)
    assert record.kp_index == 4
    assert record.dst == -22.1


@pytest.mark.parametrize("payload", [[], [{}]])
def test_parse_latest_failure(payload):
    with pytest.raises(Exception):
        parse_latest(payload)
