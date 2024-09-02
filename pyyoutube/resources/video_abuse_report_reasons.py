from typing import Optional, Union

from ..models import VideoAbuseReportReasonListResponse
from ..resources.resource import Resource
from ..utils.params_checker import enf_parts


class VideoAbuseReportReasonsResource(Resource):
    """A videoAbuseReportReason resource contains information about a reason that a video would be flagged for containing abusive content.

    References: https://developers.google.com/youtube/v3/docs/videoAbuseReportReasons
    """  # noqa: E501

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        hl: Optional[str] = None,
    ) -> VideoAbuseReportReasonListResponse:
        """Retrieve a list of reasons that can be used to report abusive videos.

        Args:
            parts:
                Comma-separated list of one or more channel resource properties.
                Accepted values: id,snippet
            hl:
                Specifies the language that should be used for text values in the API response.
                The default value is en_US.

        Returns:
            reasons data.
        """
        params = {
            "part": enf_parts(resource="videoAbuseReportReasons", value=parts),
            "hl": hl,
        }

        return await self._client.list(VideoAbuseReportReasonListResponse, "videoAbuseReportReasons", params)
