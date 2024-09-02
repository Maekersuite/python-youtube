from typing import Optional, Union

from ..error import PyYouTubeIncorrectParamsError
from ..models import PlaylistListResponse
from ..protocols import APIClientProto
from ..resources.resource import Resource
from ..utils.params_checker import enf_comma_separated, enf_parts
from .playlist_items import PlaylistItemsResource


class PlaylistsResource(Resource):
    """A playlist resource represents a YouTube playlist.

    References: https://developers.google.com/youtube/v3/docs/playlists
    """

    items: PlaylistItemsResource

    def __init__(self, client: APIClientProto) -> None:
        super().__init__(client)
        self.items = PlaylistItemsResource(client)

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        channel_id: Optional[str] = None,
        playlist_id: Optional[Union[str, list[str]]] = None,
        mine: Optional[bool] = None,
        hl: Optional[str] = None,
        max_results: Optional[int] = None,
        on_behalf_of_content_owner: Optional[str] = None,
        on_behalf_of_content_owner_channel: Optional[str] = None,
        page_token: Optional[str] = None,
    ) -> PlaylistListResponse:
        """Returns a collection of playlists that match the API request parameters.

        Args:
            parts:
                Comma-separated list of one or more channel resource properties.
                Accepted values: id,contentDetails,localizations,player,snippet,status
            channel_id:
                Indicates that the API should only return the specified channel's playlists.
            playlist_id:
                Specifies a comma-separated list of the YouTube playlist ID(s) for the resource(s)
                that are being retrieved.
            mine:
                Set this parameter's value to true to instruct the API to only return playlists
                owned by the authenticated user.
            hl:
                The hl parameter instructs the API to retrieve localized resource metadata for
                a specific application language that the YouTube website supports.
                The parameter value must be a language code included in the list returned by the
                i18nLanguages.list method.
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
            on_behalf_of_content_owner_channel:
                The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel
                to which a video is being added. This parameter is required when a request specifies a value
                for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that
                parameter. In addition, the request must be authorized using a CMS account that is linked to
                the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel
                that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content
                owner that the onBehalfOfContentOwner parameter specifies.
            page_token:
                The parameter identifies a specific page in the result set that should be returned.

        Returns:
            Playlist data.
        """
        params = {
            "part": enf_parts(resource="playlists", value=parts),
            "hl": hl,
            "maxResults": max_results,
            "onBehalfOfContentOwner": on_behalf_of_content_owner,
            "onBehalfOfContentOwnerChannel": on_behalf_of_content_owner_channel,
            "pageToken": page_token,
        }
        if channel_id is not None:
            params["channelId"] = channel_id
        elif playlist_id is not None:
            params["id"] = enf_comma_separated(field="playlist_id", value=playlist_id)
        elif mine is not None:
            params["mine"] = mine
        else:
            raise PyYouTubeIncorrectParamsError("Specify at least one of channel_id, playlist_id or mine")

        return await self._client.list(PlaylistListResponse, "playlists", params)
