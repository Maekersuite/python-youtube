# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable
from .common import BaseList, BaseResource, ResourceId, Thumbnails
from .mixins import DatetimeTimeMixin


@dataclass
class SubscriptionSnippet(Serializable, DatetimeTimeMixin):
    """A class representing the subscription snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/subscriptions#snippet
    """

    publishedAt: Optional[str] = field(default=None, repr=False)
    channelTitle: Optional[str] = field(default=None, repr=False)
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    resourceId: Optional[ResourceId] = field(default=None, repr=False)
    channelId: Optional[str] = field(default=None, repr=False)
    thumbnails: Optional[Thumbnails] = field(default=None, repr=False)


@dataclass
class SubscriptionContentDetails(Serializable):
    """A class representing the subscription contentDetails info.

    Refer: https://developers.google.com/youtube/v3/docs/subscriptions#contentDetails
    """

    totalItemCount: Optional[int] = field(default=None)
    newItemCount: Optional[int] = field(default=None)
    activityType: Optional[str] = field(default=None, repr=False)


@dataclass
class SubscriptionSubscriberSnippet(Serializable):
    """A class representing the subscription subscriberSnippet info.

    Refer: https://developers.google.com/youtube/v3/docs/subscriptions#subscriberSnippet
    """

    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    channelId: Optional[str] = field(default=None, repr=False)
    thumbnails: Optional[Thumbnails] = field(default=None, repr=False)


@dataclass
class Subscription(BaseResource):
    """A class representing the subscription info.

    Refer: https://developers.google.com/youtube/v3/docs/subscriptions
    """

    snippet: Optional[SubscriptionSnippet] = field(default=None)
    contentDetails: Optional[SubscriptionContentDetails] = field(default=None, repr=False)
    subscriberSnippet: Optional[SubscriptionSubscriberSnippet] = field(default=None, repr=False)


@dataclass
class SubscriptionListResponse(BaseList):
    """A class representing the subscription's retrieve response info.

    Refer: https://developers.google.com/youtube/v3/docs/subscriptions/list#response_1
    """

    items: list[Subscription] = field(repr=False)
