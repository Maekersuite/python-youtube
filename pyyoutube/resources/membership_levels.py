from typing import Optional, Union

from ..models import MembershipsLevelListResponse
from ..resources.resource import Resource
from ..utils.params_checker import enf_parts


class MembershipLevelsResource(Resource):
    """A membershipsLevel resource identifies a pricing level managed by the creator that authorized the API request.

    References: https://developers.google.com/youtube/v3/docs/membershipsLevels
    """

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
    ) -> MembershipsLevelListResponse:
        """Lists membership levels for the channel that authorized the request.

        Args:
            parts:
                Comma-separated list of one or more channel resource properties.
                Accepted values: id,snippet

        Returns:
            Membership levels data.

        """
        params = {
            "part": enf_parts(resource="membershipsLevels", value=parts),
        }

        return await self._client.list(MembershipsLevelListResponse, "membershipsLevels", params)
