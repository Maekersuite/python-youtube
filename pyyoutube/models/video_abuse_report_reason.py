# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field

from ..utils.serializable import Serializable
from .common import BaseList, BaseResource


@dataclass
class SecondaryReason(Serializable):
    """A class representing the video abuse report reason info.

    Refer: https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons#snippet.secondaryReasons
    """

    id: str = field()
    label: str = field(repr=True)


@dataclass
class VideoAbuseReportReasonSnippet(Serializable):
    """A class representing the video abuse report snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons#snippet
    """

    label: str = field()
    secondaryReasons: list[SecondaryReason] = field(repr=True)


@dataclass
class VideoAbuseReportReason(BaseResource):
    """A class representing the video abuse report info.

    Refer: https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons
    """

    snippet: VideoAbuseReportReasonSnippet = field()


@dataclass
class VideoAbuseReportReasonListResponse(BaseList):
    """A class representing the I18n language list response info.

    Refer: https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons/list#response_1
    """

    items: list[VideoAbuseReportReason] = field(repr=False)
