import os
import requests
from typing import List, Dict

SWCP_KP_INDEX_URL = os.getenv(
    "SWCP_KP_INDEX_URL",
    "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"
)

def fetch_planetary_kp_index() -> List[Dict]:
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
