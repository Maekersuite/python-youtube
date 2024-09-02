from typing import Optional, Union

from ..error import PyYouTubeIncorrectParamsError
from ..models import CommentThreadListResponse
from ..resources.resource import Resource
from ..utils.params_checker import enf_parts


class CommentThreadsResource(Resource):
    """A commentThread resource contains information about a YouTube comment thread, which comprises a top-level comment and replies, if any exist, to that comment.

    References: https://developers.google.com/youtube/v3/docs/commentThreads
    """  # noqa: E501

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        all_threads_related_to_channel_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        thread_id: Optional[Union[str, list[str]]] = None,
        video_id: Optional[str] = None,
        max_results: Optional[int] = None,
        moderation_status: Optional[str] = None,
        order: Optional[str] = None,
        page_token: Optional[str] = None,
        search_terms: Optional[str] = None,
        text_format: Optional[str] = None,
    ) -> CommentThreadListResponse:
        """Returns a list of comment threads that match the API request parameters.

        Args:
            parts:
                Comma-separated list of one or more comment thread resource properties.
            all_threads_related_to_channel_id:
                Instructs the API to return all comment threads associated with the specified channel.
            channel_id:
                Instructs the API to return comment threads containing comments about the specified channel
            thread_id:
                Specifies a comma-separated list of comment thread IDs for the resources that should be retrieved.
            video_id:
                Instructs the API to return comment threads associated with the specified video ID.
            max_results:
                The parameter specifies the maximum number of items that should be returned
                the result set.
                Acceptable values are 1 to 100, inclusive. The default value is 20.
            moderation_status:
                Set this parameter to limit the returned comment threads to a particular moderation state.
                The default value is published.
                Note: This parameter is not supported for use in conjunction with the id parameter.
            order:
                Specifies the order in which the API response should list comment threads.
                Valid values are:
                    - time: Comment threads are ordered by time. This is the default behavior.
                    - relevance: Comment threads are ordered by relevance.
                Notes: This parameter is not supported for use in conjunction with the `id` parameter.
            page_token:
                 Identifies a specific page in the result set that should be returned.
                 Notes: This parameter is not supported for use in conjunction with the `id` parameter.
            search_terms:
                 Instructs the API to limit the API response to only contain comments that contain
                 the specified search terms.
                 Notes: This parameter is not supported for use in conjunction with the `id` parameter.
            text_format:
                Set this parameter's value to html or plainText to instruct the API to return the comments
                left by users in html formatted or in plain text. The default value is html.
                Acceptable values are:
                    - html: Returns the comments in HTML format. This is the default value.
                    - plainText: Returns the comments in plain text format.
                Notes: This parameter is not supported for use in conjunction with the `id` parameter.

        Returns:
            Comment threads data.

        """
        params = {
            "part": enf_parts(resource="commentThreads", value=parts),
            "maxResults": max_results,
            "moderationStatus": moderation_status,
            "order": order,
            "pageToken": page_token,
            "searchTerms": search_terms,
            "textFormat": text_format,
        }
        if all_threads_related_to_channel_id is not None:
            params["allThreadsRelatedToChannelId"] = all_threads_related_to_channel_id
        elif channel_id:
            params["channelId"] = channel_id
        elif thread_id:
            params["id"] = thread_id
        elif video_id:
            params["videoId"] = video_id
        else:
            raise PyYouTubeIncorrectParamsError(
                "Specify at least one of all_threads_related_to_channel_id,channel_id,thread_id or video_id"
            )

        return await self._client.list(CommentThreadListResponse, path="commentThreads", params=params)
