"""Videos resource implementation."""

from typing import Optional, Union

from ..error import PyYouTubeIncorrectParamsError
from ..models import (
    VideoListResponse,
)
from ..protocols import APIClientProto
from ..resources.resource import Resource
from ..utils.params_checker import enf_comma_separated, enf_parts
from .video_abuse_report_reasons import VideoAbuseReportReasonsResource
from .video_categories import VideoCategoriesResource


class VideosResource(Resource):
    """A video resource represents a YouTube video.

    References: https://developers.google.com/youtube/v3/docs/videos
    """

    categories: VideoCategoriesResource
    abuse_report_reasons: VideoAbuseReportReasonsResource

    def __init__(self, client: APIClientProto) -> None:
        super().__init__(client)
        self.categories = VideoCategoriesResource(client)
        self.abuse_report_reasons = VideoAbuseReportReasonsResource(client)

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        chart: Optional[str] = None,
        video_id: Optional[Union[str, list[str]]] = None,
        my_rating: Optional[str] = None,
        hl: Optional[str] = None,
        max_height: Optional[int] = None,
        max_results: Optional[int] = None,
        max_width: Optional[int] = None,
        on_behalf_of_content_owner: Optional[str] = None,
        page_token: Optional[str] = None,
        region_code: Optional[str] = None,
        video_category_id: Optional[str] = None,
    ) -> VideoListResponse:
        """Returns a list of videos that match the API request parameters.

        Args:
            parts:
                Comma-separated list of one or more channel resource properties.
                Accepted values: id,contentDetails,fileDetails,liveStreamingDetails,
                localizations,player,processingDetails,recordingDetails,snippet,statistics,
                status,suggestions,topicDetails
            chart:
                Identifies the chart that you want to retrieve.
                Acceptable values are:
                    - mostPopular:  Return the most popular videos for the specified content region and video category.
            video_id:
                Specifies a comma-separated list of the YouTube video ID(s) for the resource(s) that are being retrieved.
            my_rating:
                Set this parameter's value to like or dislike to instruct the API to only return videos liked
                or disliked by the authenticated user.
                Acceptable values are:
                    - dislike: Returns only videos disliked by the authenticated user.
                    - like: Returns only video liked by the authenticated user.
            hl:
                Instructs the API to retrieve localized resource metadata for a specific application language
                that the YouTube website supports.
            max_height:
                Specifies the maximum height of the embedded player returned the player.embedHtml property.
            max_results:
                Specifies the maximum number of items that should be returned the result set.
            max_width:
                Specifies the maximum width of the embedded player returned the player.embedHtml property.
            on_behalf_of_content_owner:
                The onBehalfOfContentOwner parameter indicates that the request's authorization
                credentials identify a YouTube CMS user who is acting on behalf of the content
                owner specified in the parameter value. This parameter is intended for YouTube
                content partners that own and manage many difference YouTube channels. It allows
                content owners to authenticate once and get access to all their video and channel
                data, without having to provide authentication credentials for each individual channel.
                The CMS account that the user authenticates with must be linked to the specified YouTube content owner.
            page_token:
                The parameter identifies a specific page in the result set that should be returned.
            region_code:
                Instructs the API to select a video chart available in the specified region.
            video_category_id:
                Identifies the video category for which the chart should be retrieved.

        Returns:
            Videos data.
        """
        params = {
            "part": enf_parts(resource="videos", value=parts),
            "hl": hl,
            "maxHeight": max_height,
            "maxResults": max_results,
            "maxWidth": max_width,
            "onBehalfOfContentOwner": on_behalf_of_content_owner,
            "pageToken": page_token,
            "regionCode": region_code,
            "videoCategoryId": video_category_id,
        }
        if chart is not None:
            params["chart"] = chart
        elif video_id is not None:
            params["id"] = enf_comma_separated(field="video_id", value=video_id)
        elif my_rating is not None:
            params["myRating"] = my_rating
        else:
            raise PyYouTubeIncorrectParamsError("Specify at least one of chart,video_id or my_rating")

        return await self._client.list(VideoListResponse, path="videos", params=params)
