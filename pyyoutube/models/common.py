# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable


@dataclass
class Thumbnail(Serializable):
    """A class representing the thumbnail resource info.

    Refer: https://developers.google.com/youtube/v3/docs/channels#snippet.thumbnails.(key).url
    """

    url: Optional[str] = field(default=None)
    width: Optional[int] = field(default=None, repr=False)
    height: Optional[int] = field(default=None, repr=False)


@dataclass
class Thumbnails(Serializable):
    """A class representing the multi thumbnail resource info.

    Refer: https://developers.google.com/youtube/v3/docs/channels#snippet.thumbnails
    """

    default: Optional[Thumbnail] = field(default=None)
    medium: Optional[Thumbnail] = field(default=None, repr=False)
    high: Optional[Thumbnail] = field(default=None, repr=False)
    standard: Optional[Thumbnail] = field(default=None, repr=False)
    maxres: Optional[Thumbnail] = field(default=None, repr=False)


@dataclass
class Topic(Serializable):
    """A class representing the channel topic info. this model also suitable for video.

    Refer:
        https://developers.google.com/youtube/v3/docs/channels#topicDetails.topicIds[]
        https://developers.google.com/youtube/v3/docs/videos#topicDetails.topicIds[]

    This model is customized for parsing topic id. YouTube Data Api not return this.
    """

    id: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)


@dataclass
class BaseTopicDetails(Serializable):
    """This is the base model for channel or video topic details."""

    topicIds: list[str] = field(repr=False)

    def get_full_topics(self):  # noqa: ANN201, D102
        from pyyoutube.utils.constants import TOPICS

        r: list[Topic] = []
        if self.topicIds:
            for topic_id in self.topicIds:
                topic = Topic.deserialize({"id": topic_id, "description": TOPICS.get(topic_id)})
                r.append(topic)
        return r


@dataclass
class Localized(Serializable):
    """A class representing the channel or video snippet localized info.

    Refer:
        https://developers.google.com/youtube/v3/docs/channels#snippet.localized
        https://developers.google.com/youtube/v3/docs/videos#snippet.localized
    """

    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None, repr=False)


@dataclass
class PageInfo(Serializable):
    """This is data model for save paging data.

    Note:
        totalResults is only an approximation/estimate.
        Refer:
            https://stackoverflow.com/questions/43507281/totalresults-count-doesnt-match-with-the-actual-results-returned-in-youtube-v3
    """

    totalResults: Optional[int] = field(default=None)
    """The total number of results in the result set."""
    resultsPerPage: Optional[int] = field(default=None)
    """The number of results included in the API response."""


@dataclass
class PaginationResponse(Serializable):
    """A base model for pagination response types."""

    nextPageToken: str = field(repr=False)
    """The token that can be used as the value of the pageToken parameter to retrieve the next page in the result set."""
    prevPageToken: str = field(repr=False)
    """The token that can be used as the value of the pageToken parameter to retrieve the previous page in the result set."""  # noqa: E501
    pageInfo: PageInfo = field(repr=False)
    """The pageInfo object encapsulates paging information for the result set."""


@dataclass
class BaseList(Serializable):
    """A base model for list response types.

    Refer:
        https://developers.google.com/youtube/v3/docs/channels/list#response_1
        https://developers.google.com/youtube/v3/docs/playlistItems/list#response_1
    """

    kind: str = field()
    """Identifies the API resource's type."""
    etag: str = field(repr=False)
    """The Etag of this resource."""


@dataclass
class BaseResource(Serializable):
    """This is a base model for different resource type.

    Refer: https://developers.google.com/youtube/v3/docs#resource-types
    """

    kind: str = field()
    """Identifies the API resource's type."""
    etag: str = field(repr=False)
    """The Etag of this resource."""
    id: str = field()
    """The ID that YouTube uses to uniquely identify the resource."""


@dataclass
class ResourceId(Serializable):
    """A class representing the subscription snippet resource info.

    Refer:
         1. https://developers.google.com/youtube/v3/docs/playlistItems#snippet.resourceId
         2. https://developers.google.com/youtube/v3/docs/subscriptions#snippet.resourceId
         3. https://developers.google.com/youtube/v3/docs/activities#contentDetails.social.resourceId
    """

    kind: Optional[str] = field(default=None)
    videoId: Optional[str] = field(default=None)
    channelId: Optional[str] = field(default=None)
    playlistId: Optional[str] = field(default=None)


@dataclass
class Player(Serializable):
    """A class representing the video,playlist player info.

    Refer:
        https://developers.google.com/youtube/v3/docs/videos#player
    """

    embedHtml: Optional[str] = field(default=None)
    # Important:
    # follows attributions maybe not exists.
    embedHeight: Optional[int] = field(default=None, repr=False)
    embedWidth: Optional[int] = field(default=None, repr=False)
