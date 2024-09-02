"""Video categories resource implementation."""

from typing import Optional, Union

from ..error import PyYouTubeIncorrectParamsError
from ..models import VideoCategoryListResponse
from ..resources.resource import Resource
from ..utils.params_checker import enf_comma_separated, enf_parts


class VideoCategoriesResource(Resource):
    """A videoCategory resource identifies a category that has been or could be associated with uploaded videos.

    References: https://developers.google.com/youtube/v3/docs/videoCategories
    """

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        category_id: Optional[Union[str, list[str]]] = None,
        region_code: Optional[str] = None,
        hl: Optional[str] = None,
    ) -> VideoCategoryListResponse:
        """Returns a list of categories that can be associated with YouTube videos.

        Args:
            parts:
                Comma-separated list of one or more video category resource properties.
                Accepted values: snippet
            category_id:
                Specifies a comma-separated list of video category IDs for the resources that you are retrieving.
            region_code:
                Instructs the API to return the list of video categories available in the specified country.
                The parameter value is an ISO 3166-1 alpha-2 country code.
            hl:
                Specifies the language that should be used for text values in the API response.
                The default value is en_US.

        Returns:
            Video category data.
        """
        params = {
            "part": enf_parts(resource="videoCategories", value=parts),
            "hl": hl,
        }

        if category_id is not None:
            params["id"] = enf_comma_separated(field="category_id", value=category_id)
        elif region_code is not None:
            params["regionCode"] = region_code
        else:
            raise PyYouTubeIncorrectParamsError("Specify at least one of category_id or region_code")

        return await self._client.list(VideoCategoryListResponse, "videoCategories", params)
