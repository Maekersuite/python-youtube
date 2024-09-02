from typing import Optional, Union

from ..error import PyYouTubeIncorrectParamsError
from ..models import ChannelSectionListResponse
from ..resources.resource import Resource
from ..utils.params_checker import enf_comma_separated, enf_parts


class ChannelSectionsResource(Resource):
    """A channelSection resource contains information about a set of videos that a channel has chosen to feature.

    References: https://developers.google.com/youtube/v3/docs/channelSections
    """

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        channel_id: Optional[str] = None,
        section_id: Optional[Union[str, list[str]]] = None,
        mine: Optional[bool] = None,
        hl: Optional[str] = None,
        on_behalf_of_content_owner: Optional[str] = None,
    ) -> ChannelSectionListResponse:
        """Returns a list of channelSection resources that match the API request criteria.

        Args:
            parts:
                Comma-separated list of one or more channel resource properties.
            channel_id:
                ID for the channel which you want to retrieve sections.
            section_id:
                Specifies a comma-separated list of IDs that uniquely identify the channelSection
                resources that are being retrieved.
            mine:
                Set this parameter's value to true to retrieve a feed of the channel sections
                associated with the authenticated user's YouTube channel.
            hl:
                The hl parameter provided support for retrieving localized metadata for a channel section.
            on_behalf_of_content_owner:
                The onBehalfOfContentOwner parameter indicates that the request's authorization
                credentials identify a YouTube CMS user who is acting on behalf of the content
                owner specified in the parameter value. This parameter is intended for YouTube
                content partners that own and manage many different YouTube channels. It allows
                content owners to authenticate once and get access to all their video and channel
                data, without having to provide authentication credentials for each individual channel.
                The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

        Returns:
            Channel section data.
        """
        params = {
            "part": enf_parts(resource="channelSections", value=parts),
            "hl": hl,
            "onBehalfOfContentOwner": on_behalf_of_content_owner,
        }
        if channel_id is not None:
            params["channelId"] = channel_id
        elif section_id is not None:
            params["id"] = enf_comma_separated(field="section_id", value=section_id)
        elif mine is not None:
            params["mine"] = mine
        else:
            raise PyYouTubeIncorrectParamsError("Specify at least one of channel_id, section_id or mine")

        return await self._client.list(ChannelSectionListResponse, path="channelSections", params=params)
