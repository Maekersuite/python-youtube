"""This provide some common utils methods for YouTube resource."""

import re
from datetime import timedelta
from re import Pattern

ISO_8601_PATTERN: Pattern[str] = re.compile(
    r"P(?P<days>\d{1,2}D)?T(?P<hours>\d{1,2}H)?(?P<minutes>\d{1,2}M)?(?P<seconds>\d{1,2}S)?"
)
"""ISO 8601 duration pattern."""


def get_video_duration(duration: str) -> int:
    """Parse video ISO 8601 duration to seconds. It doesn't validate the duration string.

    Refer: https://developers.google.com/youtube/v3/docs/videos#contentDetails.duration

    Returns:
        `int`: Duration in seconds.
    """
    match = re.match(ISO_8601_PATTERN, duration)

    if not match:
        raise ValueError(f"Invalid ISO8601 duration string: {duration}")

    # Convert the matched groups to int and remove the 'S', 'M', 'H', 'D' suffixes
    duration_dict = {key: int(value[:-1]) for key, value in match.groupdict().items() if value}
    return int(timedelta(**duration_dict).total_seconds())
