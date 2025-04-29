import pytest
from unittest.mock import Mock

from stellar_harvest_ie_producers.stellar.swpc.producer import publish_swpc_record
from stellar_harvest_ie_stream.settings import settings


def test_publish_swpc_record(mocker):
    fake_producer = Mock()
    fake_record = Mock(dict=lambda: {"kp_index": 5})

    # patch the two dependencies


    # call the API
    publish_swpc_record()
