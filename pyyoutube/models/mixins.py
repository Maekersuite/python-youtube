from datetime import datetime
from typing import Optional


class DatetimeTimeMixin:  # noqa: D101
    @staticmethod
    def string_to_datetime(dt_str: Optional[str]) -> Optional[datetime]:
        """Convert datetime string to datetime instance.

        The original string format is YYYY-MM-DDThh:mm:ss.sZ.
        """
        if not dt_str:
            return None

        return datetime.fromisoformat(dt_str)
