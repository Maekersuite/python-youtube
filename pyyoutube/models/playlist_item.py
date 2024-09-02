# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable
from .common import BaseList, BaseResource, ResourceId, Thumbnails
from .mixins import DatetimeTimeMixin


@dataclass
class PlaylistItemContentDetails(Serializable, DatetimeTimeMixin):
    """A class representing the playlist item's content details info.

    Refer: https://developers.google.com/youtube/v3/docs/playlistItems#contentDetails
    """

    videoId: Optional[str] = field(default=None)
    note: Optional[str] = field(default=None, repr=False)
    videoPublishedAt: Optional[str] = field(default=None)
    startAt: Optional[str] = field(default=None, repr=False)
    endAt: Optional[str] = field(default=None, repr=False)


@dataclass
class PlaylistItemSnippet(Serializable, DatetimeTimeMixin):
    """A class representing the playlist item's snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/playlistItems#snippet
    """

    publishedAt: Optional[str] = field(default=None, repr=False)
    channelId: Optional[str] = field(default=None, repr=False)
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    thumbnails: Optional[Thumbnails] = field(default=None, repr=False)
    channelTitle: Optional[str] = field(default=None, repr=False)
    videoOwnerChannelTitle: Optional[str] = field(default=None, repr=False)
    videoOwnerChannelId: Optional[str] = field(default=None, repr=False)
    playlistId: Optional[str] = field(default=None, repr=False)
    position: Optional[int] = field(default=None, repr=False)
    resourceId: Optional[ResourceId] = field(default=None, repr=False)


@dataclass
class PlaylistItemStatus(Serializable):
    """A class representing the playlist item's status info.

    Refer: https://developers.google.com/youtube/v3/docs/playlistItems#status
    """

    privacyStatus: Optional[str] = field(default=None)


@dataclass
class PlaylistItem(BaseResource):
    """A class representing the playlist item's info.

    Refer: https://developers.google.com/youtube/v3/docs/playlistItems
    """

    snippet: Optional[PlaylistItemSnippet] = field(default=None, repr=False)
    contentDetails: Optional[PlaylistItemContentDetails] = field(default=None, repr=False)
    status: Optional[PlaylistItemStatus] = field(default=None, repr=False)


@dataclass
class PlaylistItemListResponse(BaseList):
    """A class representing the playlist item's retrieve response info.

    Refer: https://developers.google.com/youtube/v3/docs/playlistItems/list#response_1
    """

    items: list[PlaylistItem] = field(repr=False)
