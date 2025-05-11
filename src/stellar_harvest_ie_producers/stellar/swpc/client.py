import os
import logging
import requests
from typing import List, Dict
from stellar_harvest_ie_config.utils.log_decorators import log_io

SWCP_KP_INDEX_URL = os.getenv(
    "SWCP_KP_INDEX_URL", "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"
)

logger = logging.getLogger(__name__)


@log_io()
def fetch_planetary_kp_indexes() -> List[Dict]:
    """
    Fetch the full list of Planetary K-Index entries from NOAA SWPC.
    Raises:
        requests.HTTPError on bad status codes.
    Returns:
        A list of raw dicts, each containing keys like 'time_tag', 'kp_index', etc.
    """
    response = requests.get(SWCP_KP_INDEX_URL, timeout=10)
    response.raise_for_status()
    return response.json()


@log_io()
def fetch_latest_planetary_kp_index() -> Dict:
    """
    Fetch and return the single most recent Planetary K-Index entry as a raw dict.
    Raises:
        ValueError if no data is returned.
    """
    data = fetch_planetary_kp_indexes()

    if not data:
        raise ValueError("No data for Planetary K-Index from NOAA SWPC.")
    # ISO8601 strings compare lexically in chronological order:
    return max(data, key=lambda e: e["time_tag"])
