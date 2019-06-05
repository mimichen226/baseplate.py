"""Extensions to the standard library `datetime` module."""

from datetime import datetime
from datetime import timezone


def datetime_to_epoch_seconds(dt: datetime) -> int:
    """Convert datetime object to epoch seconds."""
    return int(datetime_to_epoch_milliseconds(dt) / 1000)


def datetime_to_epoch_milliseconds(dt: datetime) -> int:
    """Convert datetime object to epoch milliseconds."""
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=timezone.utc)
    return int(dt.timestamp() * 1000)


def epoch_seconds_to_datetime(sec: int) -> datetime:
    """Convert epoch seconds to UTC datetime."""
    return datetime.utcfromtimestamp(sec).replace(tzinfo=timezone.utc)
