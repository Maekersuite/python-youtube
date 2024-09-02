# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable
from .common import BaseList, BaseResource


@dataclass
class ChannelSectionSnippet(Serializable):
    """A class representing the channel section snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/channelSections#snippet
    """

    type: Optional[str] = field(default=None)
    channelId: Optional[str] = field(default=None, repr=False)
    title: Optional[str] = field(default=None, repr=False)
    position: Optional[int] = field(default=None)


@dataclass
class ChannelSectionContentDetails(Serializable):
    """A class representing the channel section content details info.

    Refer: https://developers.google.com/youtube/v3/docs/channelSections#contentDetails
    """

    playlists: Optional[list[str]] = field(default=None, repr=False)
    channels: Optional[list[str]] = field(default=None)


@dataclass
class ChannelSection(BaseResource):
    """A class representing the channel section info.

    Refer: https://developers.google.com/youtube/v3/docs/channelSections#properties
    """

    snippet: Optional[ChannelSectionSnippet] = field(default=None, repr=False)
    contentDetails: Optional[ChannelSectionContentDetails] = field(default=None, repr=False)


@dataclass
class ChannelSectionListResponse(BaseList):
    """A class representing the channel section's retrieve response info.

    Refer: https://developers.google.com/youtube/v3/docs/channelSections/list?#properties_1
    """

    items: list[ChannelSection] = field(repr=False)
