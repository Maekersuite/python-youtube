# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable
from .common import BaseList, BaseResource


@dataclass
class MembershipLevelSnippetLevelDetails(Serializable):  # noqa: D101
    displayName: Optional[str] = field(default=None)


@dataclass
class MembershipsLevelSnippet(Serializable):
    """A class representing the membership level snippet.

    Refer: https://developers.google.com/youtube/v3/docs/membershipsLevels#snippet
    """

    creatorChannelId: Optional[str] = field(default=None)
    levelDetails: Optional[MembershipLevelSnippetLevelDetails] = field(default=None, repr=False)


@dataclass
class MembershipsLevel(BaseResource):
    """A class representing the membership level.

    Refer: https://developers.google.com/youtube/v3/docs/membershipsLevels
    """

    snippet: Optional[MembershipsLevelSnippet] = field(default=None, repr=False)


@dataclass
class MembershipsLevelListResponse(BaseList):
    """A class representing the memberships level's retrieve response info.

    Refer: https://developers.google.com/youtube/v3/docs/membershipsLevels/list#response
    """

    items: list[MembershipsLevel] = field(repr=False)
