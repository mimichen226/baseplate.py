from datetime import datetime
from datetime import timezone
import pytz
import unittest

from baseplate.datetime import datetime_to_epoch_milliseconds
from baseplate.datetime import datetime_to_epoch_seconds
from baseplate.datetime import epoch_seconds_to_datetime


EXAMPLE_DATETIME = datetime.utcnow().replace(tzinfo=timezone.utc, microsecond=0)


class DatetimeTests(unittest.TestCase):
    def test_datetime_conversions(self):
        epoch_sec = datetime_to_epoch_seconds(EXAMPLE_DATETIME)
        epoch_ms = datetime_to_epoch_milliseconds(EXAMPLE_DATETIME)
        self.assertEqual(EXAMPLE_DATETIME, epoch_seconds_to_datetime(epoch_sec))
        self.assertEqual(epoch_sec, int(epoch_ms / 1000))

    def test_timezone_equivalence(self):
        pytz_datetime = EXAMPLE_DATETIME.replace(tzinfo=pytz.UTC)
        self.assertEqual(
            datetime_to_epoch_milliseconds(pytz_datetime),
            datetime_to_epoch_milliseconds(EXAMPLE_DATETIME),
        )
        self.assertEqual(
            datetime_to_epoch_seconds(pytz_datetime), datetime_to_epoch_seconds(EXAMPLE_DATETIME)
        )