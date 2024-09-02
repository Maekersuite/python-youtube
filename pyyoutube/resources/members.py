from typing import Optional, Union

from ..models import MemberListResponse
from ..protocols import APIClientProto
from ..resources.resource import Resource
from ..utils.params_checker import enf_comma_separated, enf_parts
from .membership_levels import MembershipLevelsResource


class MembersResource(Resource):
    """A member resource represents a channel member for a YouTube channel.

    References: https://developers.google.com/youtube/v3/docs/members
    """

    levels: MembershipLevelsResource

    def __init__(self, client: APIClientProto) -> None:
        super().__init__(client)
        self.levels = MembershipLevelsResource(client)

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        mode: Optional[str] = None,
        max_results: Optional[int] = None,
        page_token: Optional[str] = None,
        has_access_to_level: Optional[str] = None,
        filter_by_member_channel_id: Optional[Union[str, list[str]]] = None,
    ) -> MemberListResponse:
        """Lists members (formerly known as "sponsors") for a channel.

        Args:
            parts:
                Comma-separated list of one or more channel resource properties.
                Accepted values: snippet
            mode:
                Indicates which members will be included in the API response.
                Accepted values:
                    - all_current: List current members, from newest to oldest.
                    - updates: List only members that joined or upgraded since the previous API call.
            max_results:
                The parameter specifies the maximum number of items that should be returned
                the result set.
                Acceptable values are 0 to 1000, inclusive. The default value is 5.
            page_token:
                The parameter identifies a specific page in the result set that should be returned.
            has_access_to_level:
                A level ID that specifies the minimum level that members in the result set should have.
            filter_by_member_channel_id:
                specifies a comma-separated list of channel IDs that can be used to check the membership
                status of specific users.
                Maximum of 100 channels can be specified per call.

        Returns:
            Members data.
        """
        params = {
            "part": enf_parts(resource="members", value=parts),
            "mode": mode,
            "maxResults": max_results,
            "pageToken": page_token,
            "hasAccessToLevel": has_access_to_level,
            "filterByMemberChannelId": enf_comma_separated(
                field="filter_by_member_channel_id", value=filter_by_member_channel_id
            ),
        }

        return await self._client.list(MemberListResponse, path="members", params=params)
