"""Comment resource implementation."""

from typing import Optional, Union

from ..error import PyYouTubeIncorrectParamsError
from ..models import CommentListResponse
from ..protocols import APIClientProto
from ..resources.resource import Resource
from ..utils.params_checker import enf_comma_separated, enf_parts
from .comment_threads import CommentThreadsResource


class CommentsResource(Resource):
    """A comment resource contains information about a single YouTube comment.

    References: https://developers.google.com/youtube/v3/docs/comments
    """

    threads: CommentThreadsResource

    def __init__(self, client: APIClientProto) -> None:
        super().__init__(client)
        self.threads = CommentThreadsResource(client)

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        comment_id: Optional[Union[str, list[str]]] = None,
        parent_id: Optional[str] = None,
        max_results: Optional[int] = None,
        text_format: Optional[str] = None,
        page_token: Optional[str] = None,
    ) -> CommentListResponse:
        """Returns a list of comments that match the API request parameters.

        Args:
            parts:
                Comma-separated list of one or more comment resource properties.
            comment_id:
                Specifies a comma-separated list of comment IDs for the resources that are being retrieved.
            parent_id:
                Specifies the ID of the comment for which replies should be retrieved.
            max_results:
                The parameter specifies the maximum number of items that should be returned
                the result set.
                This parameter is not supported for use in conjunction with the comment_id parameter.
                Acceptable values are 1 to 100, inclusive. The default value is 20.
            text_format:
                Whether the API should return comments formatted as HTML or as plain text.
                The default value is html.
                Acceptable values are:
                    - html: Returns the comments in HTML format.
                    - plainText: Returns the comments in plain text format.
            page_token:
                The parameter identifies a specific page in the result set that should be returned.

        Returns:
            Comments data
        """
        params = {
            "part": enf_parts(resource="comments", value=parts),
            "maxResults": max_results,
            "textFormat": text_format,
            "pageToken": page_token,
        }
        if comment_id is not None:
            params["id"] = enf_comma_separated(field="comment_id", value=comment_id)
        elif parent_id is not None:
            params["parentId"] = parent_id
        else:
            raise PyYouTubeIncorrectParamsError("Specify at least one of comment_id, or parent_id")

        return await self._client.list(CommentListResponse, "comments", params)
