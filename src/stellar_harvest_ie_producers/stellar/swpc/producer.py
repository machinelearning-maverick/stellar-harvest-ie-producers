from stellar_harvest_ie_stream.clients import get_producer
from stellar_harvest_ie_stream.settings import settings

from .client import fetch_latest_raw
from .parser import parse_latest


def publish_swpc_record() -> None:
    """Fetches the latest SWPC record, parse and publishes it to Kafka."""
    producer = get_producer()
    record_raw = fetch_latest_raw()
    record_parsed = parse_latest(record_raw)
    producer.send(settings.swpc_topic, record_parsed)
    producer.flush()
