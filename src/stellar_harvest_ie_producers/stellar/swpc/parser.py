from typing import Dict
from stellar_harvest_ie_models.stellar.swpc.models import KpIndexRecord
from stellar_harvest_ie_config.utils.log_decorators import log_io


@log_io()
def parse_latest_planetary_kp_index(kp_index: Dict) -> KpIndexRecord:
    """
    Given a raw SWPC entity and validate it against our Pydantic model.
    Raises:
        ValueError if kp_index is empty or missing required fields.
    """
    if not kp_index:
        raise ValueError("No KP Index to parse from NOAA SWPC")

    return KpIndexRecord(**kp_index)
