# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable
from .common import BaseList, BaseResource


@dataclass
class CategorySnippet(Serializable):
    """This is base category snippet for video and guide."""

    channelId: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)


@dataclass
class VideoCategorySnippet(CategorySnippet):
    """A class representing video category snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/videoCategories#snippet
    """

    assignable: Optional[bool] = field(default=None, repr=False)


@dataclass
class VideoCategory(BaseResource):
    """A class representing video category info.

    Refer: https://developers.google.com/youtube/v3/docs/videoCategories
    """

    snippet: Optional[VideoCategorySnippet] = field(default=None, repr=False)


@dataclass
class VideoCategoryListResponse(BaseList):
    """A class representing the video category's retrieve response info.

    Refer: https://developers.google.com/youtube/v3/docs/videoCategories/list#response_1
    """

    items: list[VideoCategory] = field(repr=False)
