# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable
from .common import BaseList
from .mixins import DatetimeTimeMixin


@dataclass
class MemberSnippetMemberDetails(Serializable):
    """A class representing the member snippet member detail.

    Refer: https://developers.google.com/youtube/v3/docs/members#snippet.memberDetails
    """

    channelId: Optional[str] = field(default=None)
    channelUrl: Optional[str] = field(default=None, repr=False)
    displayName: Optional[str] = field(default=None, repr=False)
    profileImageUrl: Optional[str] = field(default=None, repr=False)


@dataclass
class MemberSnippetMembershipsDuration(Serializable, DatetimeTimeMixin):
    """A class representing the member snippet memberships duration."""

    memberSince: Optional[str] = field(default=None)
    memberTotalDurationMonths: Optional[int] = field(default=None, repr=False)


@dataclass
class MemberSnippetMembershipsDurationAtLevel(Serializable):
    """A class representing the member snippet memberships duration at level."""

    level: Optional[str] = field(default=None)
    memberSince: Optional[str] = field(default=None, repr=False)
    memberTotalDurationMonths: Optional[int] = field(default=None, repr=False)


@dataclass
class MemberSnippetMembershipsDetails(Serializable):
    """A class representing the member snippet membership detail.

    Refer: https://developers.google.com/youtube/v3/docs/members#snippet.membershipsDetails
    """

    membershipsDurationAtLevel: list[MemberSnippetMembershipsDurationAtLevel] = field(repr=False)
    accessibleLevels: Optional[list[str]] = field(default=None, repr=False)
    membershipsDuration: Optional[MemberSnippetMembershipsDuration] = field(default=None, repr=False)
    highestAccessibleLevel: Optional[str] = field(default=None)
    highestAccessibleLevelDisplayName: Optional[str] = field(default=None)


@dataclass
class MemberSnippet(Serializable):
    """A class representing the member snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/members#snippet
    """

    creatorChannelId: Optional[str] = field(default=None)
    memberDetails: Optional[MemberSnippetMemberDetails] = field(default=None, repr=False)
    membershipsDetails: Optional[MemberSnippetMembershipsDetails] = field(default=None, repr=False)


@dataclass
class Member(Serializable):
    """A class representing the member info.

    Refer: https://developers.google.com/youtube/v3/docs/members
    """

    kind: Optional[str] = field(default=None)
    etag: Optional[str] = field(default=None, repr=False)
    snippet: Optional[MemberSnippet] = field(default=None, repr=False)


@dataclass
class MemberListResponse(BaseList):
    """A class representing the member's retrieve response info.

    Refer: https://developers.google.com/youtube/v3/docs/members/list#response
    """

    items: list[Member] = field(repr=False)
