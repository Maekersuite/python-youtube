# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable
from .common import BaseList, BaseResource, Thumbnails
from .mixins import DatetimeTimeMixin


@dataclass
class SearchResultSnippet(Serializable, DatetimeTimeMixin):
    """A class representing the search result snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/search#snippet
    """

    publishedAt: Optional[str] = field(default=None, repr=False)
    channelId: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None, repr=False)
    thumbnails: Optional[Thumbnails] = field(default=None, repr=False)
    channelTitle: Optional[str] = field(default=None, repr=False)
    liveBroadcastContent: Optional[str] = field(default=None, repr=False)


@dataclass
class SearchResultId(Serializable):
    """A class representing the search result id info.

    Refer: https://developers.google.com/youtube/v3/docs/search#id
    """

    kind: str = field()
    videoId: Optional[str] = field(default=None, repr=False)
    channelId: Optional[str] = field(default=None, repr=False)
    playlistId: Optional[str] = field(default=None, repr=False)


@dataclass
class SearchResult(BaseResource):
    """A class representing the search result's info.

    Refer: https://developers.google.com/youtube/v3/docs/search
    """

    id: SearchResultId = field(repr=False)
    snippet: SearchResultSnippet = field(repr=False)


@dataclass
class SearchListResponse(BaseList):
    """A class representing the channel's retrieve response info.

    Refer: https://developers.google.com/youtube/v3/docs/channels/list#response_1
    """

    items: list[SearchResult] = field(repr=False)
    regionCode: Optional[str] = field(default=None, repr=False)
