from typing import Optional, Union

from ..error import PyYouTubeIncorrectParamsError
from ..models import SubscriptionListResponse
from ..resources.resource import Resource
from ..utils.params_checker import enf_comma_separated, enf_parts


class SubscriptionsResource(Resource):
    """A subscription resource contains information about a YouTube user subscription.

    References: https://developers.google.com/youtube/v3/docs/subscriptions
    """

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        channel_id: Optional[str] = None,
        subscription_id: Optional[Union[str, list[str]]] = None,
        mine: Optional[bool] = None,
        my_recent_subscribers: Optional[bool] = None,
        my_subscribers: Optional[bool] = None,
        for_channel_id: Optional[Union[str, list[str]]] = None,
        max_results: Optional[int] = None,
        on_behalf_of_content_owner: Optional[str] = None,
        on_behalf_of_content_owner_channel: Optional[str] = None,
        order: Optional[str] = None,
        page_token: Optional[str] = None,
    ) -> SubscriptionListResponse:
        """Returns subscription resources that match the API request criteria.

        Args:
            parts:
                Comma-separated list of one or more channel resource properties.
                Accepted values: id,contentDetails,snippet,subscriberSnippet
            channel_id:
                Specifies a YouTube channel ID. The API will only return that channel's subscriptions.
            subscription_id:
                Specifies a comma-separated list of the YouTube subscription ID(s) for the resource(s)
                that are being retrieved.
            mine:
                Set this parameter's value to true to retrieve a feed of the authenticated user's subscriptions.
            my_recent_subscribers:
                Set this parameter's value to true to retrieve a feed of the subscribers of the authenticated user
                in reverse chronological order (the newest first).
            my_subscribers:
                Set this parameter's value to true to retrieve a feed of the subscribers of the authenticated user
                in no particular order.
            for_channel_id:
                Specifies a comma-separated list of channel IDs.
                The API response will then only contain subscriptions matching those channels.
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
                The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of
                the channel to which a video is being added. This parameter is required when a request
                specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in
                conjunction with that parameter. In addition, the request must be authorized using a
                CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter
                specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value
                specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.
            order:
                Specifies the method that will be used to sort resources in the API response.
                Acceptable values are:
                    - alphabetical: Sort alphabetically.
                    - relevance: Sort by relevance. Default.
                    - unread: Sort by order of activity.
            page_token:
                The parameter identifies a specific page in the result set that should be returned.

        Returns:
            Subscriptions data.
        """
        params = {
            "part": enf_parts(resource="subscriptions", value=parts),
            "forChannelId": enf_comma_separated(field="for_channel_id", value=for_channel_id),
            "maxResults": max_results,
            "onBehalfOfContentOwner": on_behalf_of_content_owner,
            "onBehalfOfContentOwnerChannel": on_behalf_of_content_owner_channel,
            "order": order,
            "pageToken": page_token,
        }

        if channel_id is not None:
            params["channelId"] = channel_id
        elif subscription_id is not None:
            params["id"] = enf_comma_separated(field="subscription_id", value=subscription_id)
        elif mine is not None:
            params["mine"] = mine
        elif my_recent_subscribers is not None:
            params["myRecentSubscribers"] = my_recent_subscribers
        elif my_subscribers is not None:
            params["mySubscribers"] = my_subscribers
        else:
            raise PyYouTubeIncorrectParamsError(
                "Specify at least one of channel_id,subscription_id,mine,my_recent_subscribers or mySubscribers"
            )

        return await self._client.list(SubscriptionListResponse, "subscriptions", params)
