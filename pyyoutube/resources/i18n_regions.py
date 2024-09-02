"""i18n regions resource implementation."""

from typing import Optional, Union

from ..models import I18nRegionListResponse
from ..resources.resource import Resource
from ..utils.params_checker import enf_parts


class I18nRegionsResource(Resource):
    """An i18nRegion resource identifies a geographic area that a YouTube user can select as the preferred content region.

    References: https://developers.google.com/youtube/v3/docs/i18nRegions
    """

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        hl: Optional[str] = None,
    ) -> I18nRegionListResponse:
        """Returns a list of content regions that the YouTube website supports.

        Args:
            parts:
                Comma-separated list of one or more i18n regions resource properties.
                Accepted values: snippet.
            hl:
                Specifies the language that should be used for text values in the API response.
                The default value is en_US.

        Returns:
            i18n regions data.
        """
        params = {
            "part": enf_parts(resource="i18nRegions", value=parts),
            "hl": hl,
        }

        return await self._client.list(I18nRegionListResponse, "i18nRegions", params)
