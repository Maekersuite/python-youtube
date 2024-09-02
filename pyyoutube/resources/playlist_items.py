"""Playlist items resource implementation."""

from typing import Optional, Union

from ..error import PyYouTubeIncorrectParamsError
from ..models import PlaylistItemListResponse
from ..resources.resource import Resource
from ..utils.params_checker import enf_comma_separated, enf_parts


class PlaylistItemsResource(Resource):
    """A playlistItem resource identifies another resource, such as a video, that is included in a playlist.

    In addition, the playlistItem resource contains details about the included resource
    that pertain specifically to how that resource is used in that playlist.

    References: https://developers.google.com/youtube/v3/docs/playlistItems
    """

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        playlist_item_id: Optional[Union[str, list[str]]] = None,
        playlist_id: Optional[str] = None,
        max_results: Optional[int] = None,
        on_behalf_of_content_owner: Optional[str] = None,
        page_token: Optional[str] = None,
        video_id: Optional[str] = None,
    ) -> PlaylistItemListResponse:
        """Returns a collection of playlist items that match the API request parameters.

        Args:
            parts:
                Comma-separated list of one or more channel resource properties.
                Accepted values: id,contentDetails,snippet,snippet
            playlist_item_id:
                Specifies a comma-separated list of one or more unique playlist item IDs.
            playlist_id:
                Specifies the unique ID of the playlist for which you want to retrieve playlist items.
            max_results:
                The parameter specifies the maximum number of items that should be returned
                the result set.
                Acceptable values are 0 to 50, inclusive. The default value is 5.
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
            video_id:
                Specifies that the request should return only the playlist items that contain the specified video.

        Returns:
            Playlist items data.
        """
        params = {
            "part": enf_parts(resource="playlistItems", value=parts),
            "maxResults": max_results,
            "onBehalfOfContentOwner": on_behalf_of_content_owner,
            "videoId": video_id,
            "pageToken": page_token,
        }
        if playlist_item_id is not None:
            params["id"] = enf_comma_separated(field="playlist_item_id", value=playlist_item_id)
        elif playlist_id is not None:
            params["playlistId"] = playlist_id
        else:
            raise PyYouTubeIncorrectParamsError("Specify at least one of playlist_item_id or playlist_id")

        return await self._client.list(PlaylistItemListResponse, "playlistItems", params)
