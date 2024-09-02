from .captions import CaptionsResource
from .channel_sections import ChannelSectionsResource
from .channels import ChannelsResource
from .comment_threads import CommentThreadsResource
from .comments import CommentsResource
from .i18n_languages import I18nLanguagesResource
from .i18n_regions import I18nRegionsResource
from .members import MembersResource
from .membership_levels import MembershipLevelsResource
from .playlist_items import PlaylistItemsResource
from .playlists import PlaylistsResource
from .resource import APIClientProto, Resource
from .search import SearchResource
from .subscriptions import SubscriptionsResource
from .video_abuse_report_reasons import VideoAbuseReportReasonsResource
from .video_categories import VideoCategoriesResource
from .videos import VideosResource

resources: list[type[Resource]] = [
    CaptionsResource,
    ChannelsResource,
    ChannelSectionsResource,
    CommentsResource,
    CommentThreadsResource,
    I18nLanguagesResource,
    I18nRegionsResource,
    MembersResource,
    MembershipLevelsResource,
    PlaylistItemsResource,
    PlaylistsResource,
    SearchResource,
    SubscriptionsResource,
    VideoAbuseReportReasonsResource,
    VideoCategoriesResource,
    VideosResource,
]

__all__ = [
    "CaptionsResource",
    "ChannelsResource",
    "ChannelSectionsResource",
    "CommentsResource",
    "CommentThreadsResource",
    "I18nLanguagesResource",
    "I18nRegionsResource",
    "MembersResource",
    "MembershipLevelsResource",
    "PlaylistItemsResource",
    "PlaylistsResource",
    "SearchResource",
    "SubscriptionsResource",
    "VideoAbuseReportReasonsResource",
    "VideoCategoriesResource",
    "VideosResource",
    "Resource",
    "APIClientProto",
]
