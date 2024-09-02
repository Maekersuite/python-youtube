from typing import Optional, Union

from ..models import CaptionListResponse
from ..resources.resource import Resource
from ..utils.params_checker import enf_comma_separated, enf_parts


class CaptionsResource(Resource):
    """A caption resource represents a YouTube caption track.

    References: https://developers.google.com/youtube/v3/docs/captions
    """

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        video_id: Optional[str] = None,
        caption_id: Optional[Union[str, list[str]]] = None,
        on_behalf_of_content_owner: Optional[str] = None,
    ) -> CaptionListResponse:
        """Returns a list of caption tracks that are associated with a specified video.

        Args:
            parts:
                Comma-separated list of one or more caption resource properties.
            video_id:
                The parameter specifies the YouTube video ID of the video for which the API
                should return caption tracks.
            caption_id:
                The id parameter specifies a comma-separated list of IDs that identify the
                caption resources that should be retrieved.
            on_behalf_of_content_owner:
                This parameter can only be used in a properly authorized request.
                Note: This parameter is intended exclusively for YouTube content partners.

        Returns:
            Caption data
        """
        params = {
            "part": enf_parts(resource="captions", value=parts),
            "videoId": video_id,
            "id": enf_comma_separated(field="caption_id", value=caption_id),
            "onBehalfOfContentOwner": on_behalf_of_content_owner,
        }

        return await self._client.list(CaptionListResponse, path="captions", params=params)
