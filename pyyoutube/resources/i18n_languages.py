"""i18n language resource implementation."""

from typing import Optional, Union

from ..models import I18nLanguageListResponse
from ..resources.resource import Resource
from ..utils.params_checker import enf_parts


class I18nLanguagesResource(Resource):
    """An i18nLanguage resource identifies an application language that the YouTube website supports.

    The application language can also be referred to as a UI language

    References: https://developers.google.com/youtube/v3/docs/i18nLanguages
    """

    async def list(
        self,
        parts: Optional[Union[str, list[str]]] = None,
        hl: Optional[str] = None,
    ) -> I18nLanguageListResponse:
        """Returns a list of application languages that the YouTube website supports.

        Args:
            parts:
                Comma-separated list of one or more i18n languages resource properties.
                Accepted values: snippet.
            hl:
                Specifies the language that should be used for text values in the API response.
                The default value is en_US.

        Returns:
            i18n language data
        """
        params = {
            "part": enf_parts(resource="i18nLanguages", value=parts),
            "hl": hl,
        }

        return await self._client.list(I18nLanguageListResponse, "i18nLanguages", params)
