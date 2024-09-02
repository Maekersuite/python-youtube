# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable


@dataclass
class WatermarkTiming(Serializable):  # noqa: D101
    type: Optional[str] = field(default=None)
    offsetMs: Optional[int] = field(default=None, repr=False)
    durationMs: Optional[int] = field(default=None, repr=False)


@dataclass
class WatermarkPosition(Serializable):  # noqa: D101
    type: Optional[str] = field(default=None)
    cornerPosition: Optional[str] = field(default=None, repr=False)


@dataclass
class Watermark(Serializable):
    """A class representing the watermark info.

    References: https://developers.google.com/youtube/v3/docs/watermarks#resource-representation
    """

    timing: Optional[WatermarkTiming] = field(default=None, repr=False)
    position: Optional[WatermarkPosition] = field(default=None, repr=False)
    imageUrl: Optional[str] = field(default=None)
    imageBytes: Optional[bytes] = field(default=None, repr=False)
    targetChannelId: Optional[str] = field(default=None, repr=False)
