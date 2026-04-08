from stellar_harvest_ie_config.utils.log_decorators import log_io

from stellar_harvest_ie_stream.clients import get_producer
from stellar_harvest_ie_stream.settings import settings

from stellar_harvest_ie_producers.stellar.swpc.client import (
    fetch_latest_planetary_kp_index,
)
from stellar_harvest_ie_producers.stellar.swpc.parser import (
    parse_latest_planetary_kp_index,
)


@log_io()
def publish_latest_planetary_kp_index() -> None:
    """
    Fetches the latest Planetary KP-Index from SWPC NOAA,
    parse and publishes it to Kafka.
    """
    producer = get_producer()
    kp_index = fetch_latest_planetary_kp_index()
    parsed_pk_index = parse_latest_planetary_kp_index(kp_index)
    producer.send(settings.swpc_topic, parsed_pk_index)
    producer.flush()
