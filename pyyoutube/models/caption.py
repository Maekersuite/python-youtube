# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable
from .common import BaseList, BaseResource
from .mixins import DatetimeTimeMixin


@dataclass
class CaptionSnippet(Serializable, DatetimeTimeMixin):
    """A class representing the caption snippet resource info.

    Refer: https://developers.google.com/youtube/v3/docs/captions#snippet
    """

    videoId: Optional[str] = field(default=None)
    lastUpdated: Optional[str] = field(default=None)
    trackKind: Optional[str] = field(default=None, repr=False)
    language: Optional[str] = field(default=None, repr=False)
    name: Optional[str] = field(default=None, repr=False)
    audioTrackType: Optional[str] = field(default=None, repr=False)
    isCC: Optional[bool] = field(default=None, repr=False)
    isLarge: Optional[bool] = field(default=None, repr=False)
    isEasyReader: Optional[bool] = field(default=None, repr=False)
    isDraft: Optional[bool] = field(default=None, repr=False)
    isAutoSynced: Optional[bool] = field(default=None, repr=False)
    status: Optional[str] = field(default=None, repr=False)
    failureReason: Optional[str] = field(default=None, repr=False)


@dataclass
class Caption(BaseResource):
    """A class representing the caption resource info.

    Refer: https://developers.google.com/youtube/v3/docs/captions
    """

    snippet: Optional[CaptionSnippet] = field(default=None)


@dataclass
class CaptionListResponse(BaseList):
    """A class representing the activity response info.

    Refer: https://developers.google.com/youtube/v3/docs/captions/list?#response_1
    """

    items: list[Caption] = field(repr=False)
