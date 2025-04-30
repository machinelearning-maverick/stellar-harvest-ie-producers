import pytest
from unittest.mock import Mock

from stellar_harvest_ie_producers.stellar.swpc.producer import publish_swpc_record
from stellar_harvest_ie_stream.settings import settings
from stellar_harvest_ie_models.stellar.swpc.models import KpIndexRecord


def test_publish_swpc_record(mocker):
    fake_producer = Mock()

    first_entry = {
        "time_tag": "2025-09-13T00:00:00Z",
        "kp_index": 3,
        "mid_latitude_kp_index": 2,
        "dst": -5.6,
        "source": "SWPC",
    }
    second_entry = {
        "time_tag": "2025-09-14T00:00:00Z",
        "kp_index": 5,
        "mid_latitude_kp_index": 4,
        "dst": -3.2,
        "source": "SWPC",
    }

    record_entries = [first_entry, second_entry]
    kp_index_record = KpIndexRecord(**first_entry)

    # patch dependencies
    mocker.patch(
        "stellar_harvest_ie_producers.stellar.swpc.producer.get_producer",
        return_value=fake_producer,
    )
    mocker.patch(
        "stellar_harvest_ie_producers.stellar.swpc.producer.fetch_latest_raw",
        return_value=record_entries,
    )
    mocker.patch(
        "stellar_harvest_ie_producers.stellar.swpc.producer.parse_latest",
        return_value=kp_index_record,
    )

    # call the API
    publish_swpc_record()

    # assertions
    fake_producer.send.assert_called_once_with(settings.swpc_topic, kp_index_record)
    fake_producer.flush.assert_called_once()
