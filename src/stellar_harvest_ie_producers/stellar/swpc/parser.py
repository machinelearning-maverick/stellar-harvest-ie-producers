from typing import List
from stellar_harvest_ie_models.stellar.swpc.models import KpIndexRecord
from stellar_harvest_ie_config.utils.log_decorators import log_io


@log_io()
def parse_latest(raw_entries: List[dict]) -> KpIndexRecord:
    """
    Given a list of raw SWPC entries (as dicts), pick the one with the newest time_tag
    and validate it against our Pydantic model.
    Raises:
        ValueError if raw_entries is empty or missing required fields.
    """
    if not raw_entries:
        raise ValueError("No entries to parse in NOAA SWPC feed")

    # find the entry with the max time_tag string
    latest = max(raw_entries, key=lambda e: e["time_tag"])
    return KpIndexRecord(**latest)
