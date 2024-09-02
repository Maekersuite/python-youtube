# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable
from .common import BaseList, BaseResource
from .mixins import DatetimeTimeMixin


@dataclass
class CommentSnippetAuthorChannelId(Serializable):
    """A class representing comment's snippet authorChannelId info.

    Refer: https://developers.google.com/youtube/v3/docs/comments#snippet.authorChannelId
    """

    value: Optional[str] = field(default=None)


@dataclass
class CommentSnippet(Serializable, DatetimeTimeMixin):
    """A class representing comment's snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/comments#snippet
    """

    authorDisplayName: Optional[str] = field(default=None)
    authorProfileImageUrl: Optional[str] = field(default=None, repr=False)
    authorChannelUrl: Optional[str] = field(default=None, repr=False)
    authorChannelId: Optional[CommentSnippetAuthorChannelId] = field(default=None, repr=False)
    channelId: Optional[str] = field(default=None, repr=False)
    videoId: Optional[str] = field(default=None, repr=False)
    textDisplay: Optional[str] = field(default=None, repr=False)
    textOriginal: Optional[str] = field(default=None, repr=False)
    parentId: Optional[str] = field(default=None, repr=False)
    canRate: Optional[bool] = field(default=None, repr=False)
    viewerRating: Optional[str] = field(default=None, repr=False)
    likeCount: Optional[int] = field(default=None)
    moderationStatus: Optional[str] = field(default=None, repr=False)
    publishedAt: Optional[str] = field(default=None, repr=False)
    updatedAt: Optional[str] = field(default=None, repr=False)


@dataclass
class Comment(BaseResource):
    """A class representing comment info.

    Refer: https://developers.google.com/youtube/v3/docs/comments
    """

    snippet: Optional[CommentSnippet] = field(default=None)


@dataclass
class CommentListResponse(BaseList):
    """A class representing the comment's retrieve response info.

    Refer: https://developers.google.com/youtube/v3/docs/comments/list#response_1
    """

    items: list[Comment] = field(repr=False)
