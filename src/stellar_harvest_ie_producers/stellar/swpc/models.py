from pydantic import BaseModel
from datetime import datetime

class KpIndexRecord(BaseModel):
    """
    Represents a single reading of the Planetary K-Index from NOAA SWCP.
    """
    time_tag: datetime
    kp_index: int
    mid_latitude_kp_index: int
    dst: float
    source: str
