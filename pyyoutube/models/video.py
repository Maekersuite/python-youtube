# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils import get_video_duration
from ..utils.serializable import Serializable
from .common import (
    BaseList,
    BaseResource,
    BaseTopicDetails,
    Localized,
    Player,
    Thumbnails,
)
from .mixins import DatetimeTimeMixin


@dataclass
class RegionRestriction(Serializable):
    """A class representing the video content details region restriction info.

    Refer: https://developers.google.com/youtube/v3/docs/videos#contentDetails.regionRestriction
    """

    allowed: Optional[list[str]] = field(default=None)
    blocked: Optional[list[str]] = field(default=None, repr=False)


class ContentRating(Serializable):
    """A class representing the video content rating info.

    Refer: https://developers.google.com/youtube/v3/docs/videos#contentDetails.contentRating
    """

    acbRating: Optional[str] = field(default=None, repr=False)
    agcomRating: Optional[str] = field(default=None, repr=False)
    anatelRating: Optional[str] = field(default=None, repr=False)
    bbfcRating: Optional[str] = field(default=None, repr=False)
    bfvcRating: Optional[str] = field(default=None, repr=False)
    bmukkRating: Optional[str] = field(default=None, repr=False)
    catvRating: Optional[str] = field(default=None, repr=False)
    catvfrRating: Optional[str] = field(default=None, repr=False)
    cbfcRating: Optional[str] = field(default=None, repr=False)
    cccRating: Optional[str] = field(default=None, repr=False)
    cceRating: Optional[str] = field(default=None, repr=False)
    chfilmRating: Optional[str] = field(default=None, repr=False)
    chvrsRating: Optional[str] = field(default=None, repr=False)
    cicfRating: Optional[str] = field(default=None, repr=False)
    cnaRating: Optional[str] = field(default=None, repr=False)
    cncRating: Optional[str] = field(default=None, repr=False)
    csaRating: Optional[str] = field(default=None, repr=False)
    cscfRating: Optional[str] = field(default=None, repr=False)
    czfilmRating: Optional[str] = field(default=None, repr=False)
    djctqRating: Optional[str] = field(default=None, repr=False)
    djctqRatingReasons: Optional[list[str]] = field(default=None, repr=False)
    ecbmctRating: Optional[str] = field(default=None, repr=False)
    eefilmRating: Optional[str] = field(default=None, repr=False)
    egfilmRating: Optional[str] = field(default=None, repr=False)
    eirinRating: Optional[str] = field(default=None, repr=False)
    fcbmRating: Optional[str] = field(default=None, repr=False)
    fcoRating: Optional[str] = field(default=None, repr=False)
    fpbRating: Optional[str] = field(default=None, repr=False)
    fpbRatingReasons: Optional[list[str]] = field(default=None, repr=False)
    fskRating: Optional[str] = field(default=None, repr=False)
    grfilmRating: Optional[str] = field(default=None, repr=False)
    icaaRating: Optional[str] = field(default=None, repr=False)
    ifcoRating: Optional[str] = field(default=None, repr=False)
    ilfilmRating: Optional[str] = field(default=None, repr=False)
    incaaRating: Optional[str] = field(default=None, repr=False)
    kfcbRating: Optional[str] = field(default=None, repr=False)
    kijkwijzerRating: Optional[str] = field(default=None, repr=False)
    kmrbRating: Optional[str] = field(default=None, repr=False)
    lsfRating: Optional[str] = field(default=None, repr=False)
    mccaaRating: Optional[str] = field(default=None, repr=False)
    mccypRating: Optional[str] = field(default=None, repr=False)
    mcstRating: Optional[str] = field(default=None, repr=False)
    mdaRating: Optional[str] = field(default=None, repr=False)
    medietilsynetRating: Optional[str] = field(default=None, repr=False)
    mekuRating: Optional[str] = field(default=None, repr=False)
    mibacRating: Optional[str] = field(default=None, repr=False)
    mocRating: Optional[str] = field(default=None, repr=False)
    moctwRating: Optional[str] = field(default=None, repr=False)
    mpaaRating: Optional[str] = field(default=None, repr=False)
    mpaatRating: Optional[str] = field(default=None, repr=False)
    mtrcbRating: Optional[str] = field(default=None, repr=False)
    nbcRating: Optional[str] = field(default=None, repr=False)
    nfrcRating: Optional[str] = field(default=None, repr=False)
    nfvcbRating: Optional[str] = field(default=None, repr=False)
    nkclvRating: Optional[str] = field(default=None, repr=False)
    oflcRating: Optional[str] = field(default=None, repr=False)
    pefilmRating: Optional[str] = field(default=None, repr=False)
    resorteviolenciaRating: Optional[str] = field(default=None, repr=False)
    rtcRating: Optional[str] = field(default=None, repr=False)
    rteRating: Optional[str] = field(default=None, repr=False)
    russiaRating: Optional[str] = field(default=None, repr=False)
    skfilmRating: Optional[str] = field(default=None, repr=False)
    smaisRating: Optional[str] = field(default=None, repr=False)
    smsaRating: Optional[str] = field(default=None, repr=False)
    tvpgRating: Optional[str] = field(default=None, repr=False)
    ytRating: Optional[str] = field(default=None)


@dataclass
class VideoContentDetails(Serializable):
    """A class representing the video content details info.

    Refer: https://developers.google.com/youtube/v3/docs/videos#contentDetails
    """

    duration: Optional[str] = field(default=None)
    dimension: Optional[str] = field(default=None)
    definition: Optional[str] = field(default=None, repr=False)
    caption: Optional[str] = field(default=None, repr=False)
    licensedContent: Optional[bool] = field(default=None, repr=False)
    regionRestriction: Optional[RegionRestriction] = field(default=None, repr=False)
    contentRating: Optional[ContentRating] = field(default=None, repr=False)
    projection: Optional[str] = field(default=None, repr=False)
    hasCustomThumbnail: Optional[bool] = field(default=None, repr=False)

    def get_video_seconds_duration(self):  # noqa: ANN201, D102
        if not self.duration:
            return None

        return get_video_duration(self.duration)


@dataclass
class VideoTopicDetails(BaseTopicDetails):
    """A class representing video's topic detail info.

    Refer: https://developers.google.com/youtube/v3/docs/videos#topicDetails
    """

    # Important:
    # This property has been deprecated as of November 10, 2016.
    # Any topics associated with a video are now returned by the topicDetails.relevantTopicIds[] property value.
    topicIds: Optional[list[str]] = field(default=None, repr=False)
    relevantTopicIds: Optional[list[str]] = field(default=None, repr=False)
    topicCategories: Optional[list[str]] = field(default=None)

    def __post_init__(self):
        if self.topicIds is None and self.relevantTopicIds is not None:
            self.topicIds = self.relevantTopicIds


@dataclass
class VideoSnippet(Serializable, DatetimeTimeMixin):
    """A class representing the video snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/videos#snippet
    """

    publishedAt: Optional[str] = field(default=None, repr=False)
    channelId: Optional[str] = field(default=None, repr=False)
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    thumbnails: Optional[Thumbnails] = field(default=None, repr=False)
    channelTitle: Optional[str] = field(default=None, repr=False)
    tags: Optional[list[str]] = field(default=None, repr=False)
    categoryId: Optional[str] = field(default=None, repr=False)
    liveBroadcastContent: Optional[str] = field(default=None, repr=False)
    defaultLanguage: Optional[str] = field(default=None, repr=False)
    localized: Optional[Localized] = field(default=None, repr=False)
    defaultAudioLanguage: Optional[str] = field(default=None, repr=False)


@dataclass
class VideoStatistics(Serializable):
    """A class representing the video statistics info.

    Refer: https://developers.google.com/youtube/v3/docs/videos#statistics
    """

    viewCount: int = field()
    likeCount: Optional[int] = field(default=None)
    dislikeCount: Optional[int] = field(default=None, repr=False)
    commentCount: Optional[int] = field(default=None, repr=False)


@dataclass
class VideoStatus(Serializable, DatetimeTimeMixin):
    """A class representing the video status info.

    Refer: https://developers.google.com/youtube/v3/docs/videos#status
    """

    uploadStatus: Optional[str] = field(default=None, repr=False)
    failureReason: Optional[str] = field(default=None, repr=False)
    rejectionReason: Optional[str] = field(default=None, repr=False)
    privacyStatus: Optional[str] = field(default=None, repr=False)
    publishAt: Optional[str] = field(default=None, repr=False)
    license: Optional[str] = field(default=None, repr=False)
    embeddable: Optional[bool] = field(default=None, repr=False)
    publicStatsViewable: Optional[bool] = field(default=None, repr=False)
    madeForKids: Optional[bool] = field(default=None, repr=False)
    selfDeclaredMadeForKids: Optional[bool] = field(default=None, repr=False)


@dataclass
class VideoLiveStreamingDetails(Serializable, DatetimeTimeMixin):
    """A class representing the video live streaming details.

    Refer: https://developers.google.com/youtube/v3/docs/videos#liveStreamingDetails
    """

    actualStartTime: Optional[str] = field(default=None, repr=False)
    actualEndTime: Optional[str] = field(default=None, repr=False)
    scheduledStartTime: Optional[str] = field(default=None, repr=False)
    scheduledEndTime: Optional[str] = field(default=None, repr=False)
    concurrentViewers: Optional[int] = field(default=None, repr=False)
    activeLiveChatId: Optional[str] = field(default=None, repr=False)


@dataclass
class Video(BaseResource):
    """A class representing the video info.

    Refer: https://developers.google.com/youtube/v3/docs/videos
    """

    snippet: VideoSnippet = field(repr=False)
    contentDetails: VideoContentDetails = field(repr=False)
    status: VideoStatus = field(repr=False)
    statistics: VideoStatistics = field(repr=False)
    topicDetails: VideoTopicDetails = field(repr=False)
    player: Player = field(repr=False)
    liveStreamingDetails: Optional[VideoLiveStreamingDetails] = field(default=None, repr=False)


@dataclass
class VideoListResponse(BaseList):
    """A class representing the video's retrieve response info.

    Refer: https://developers.google.com/youtube/v3/docs/videos/list#response_1
    """

    items: list[Video] = field(repr=False)
    """A list of videos that match the request criteria."""
