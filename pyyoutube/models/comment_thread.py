# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable
from .comment import Comment
from .common import BaseList, BaseResource


@dataclass
class CommentThreadSnippet(Serializable):
    """A class representing comment tread snippet info.

    References: https://developers.google.com/youtube/v3/docs/commentThreads#snippet
    """

    channelId: Optional[str] = field(default=None)
    videoId: Optional[str] = field(default=None)
    topLevelComment: Optional[Comment] = field(default=None, repr=False)
    canReply: Optional[bool] = field(default=None, repr=False)
    totalReplyCount: Optional[int] = field(default=None, repr=False)
    isPublic: Optional[bool] = field(default=None, repr=False)


@dataclass
class CommentThreadReplies(Serializable):
    """A class representing comment tread replies info.

    Refer: https://developers.google.com/youtube/v3/docs/commentThreads#replies
    """

    comments: list[Comment] = field(repr=False)


@dataclass
class CommentThread(BaseResource):
    """A class representing comment thread info.

    Refer: https://developers.google.com/youtube/v3/docs/commentThreads
    """

    snippet: Optional[CommentThreadSnippet] = field(default=None, repr=False)
    replies: Optional[CommentThreadReplies] = field(default=None, repr=False)


@dataclass
class CommentThreadListResponse(BaseList):
    """A class representing the comment thread's retrieve response info.

    Refer: https://developers.google.com/youtube/v3/docs/commentThreads/list#response_1
    """

    items: list[CommentThread] = field(repr=False)
