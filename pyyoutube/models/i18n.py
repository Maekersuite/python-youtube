# ruff: noqa: N815 (YouTube specific attributes)

from dataclasses import dataclass, field
from typing import Optional

from ..utils.serializable import Serializable
from .common import BaseList, BaseResource


@dataclass
class I18nRegionSnippet(Serializable):
    """A class representing the I18n region snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/i18nRegions#snippet
    """

    gl: Optional[str] = field(default=None)
    name: Optional[str] = field(default=None)


@dataclass
class I18nRegion(BaseResource):
    """A class representing the I18n region info.

    Refer: https://developers.google.com/youtube/v3/docs/i18nRegions#resource-representation
    """

    snippet: Optional[I18nRegionSnippet] = field(default=None)


@dataclass
class I18nRegionListResponse(BaseList):
    """A class representing the I18n region list response info.

    Refer: https://developers.google.com/youtube/v3/docs/i18nLanguages/list#response_1
    """

    items: list[I18nRegion] = field(repr=False)


@dataclass
class I18nLanguageSnippet(Serializable):
    """A class representing the I18n language snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/i18nLanguages#snippet
    """

    hl: Optional[str] = field(default=None)
    name: Optional[str] = field(default=None)


@dataclass
class I18nLanguage(BaseResource):
    """A class representing the I18n language info.

    Refer: https://developers.google.com/youtube/v3/docs/i18nLanguages#resource-representation
    """

    snippet: Optional[I18nLanguageSnippet] = field(default=None)


@dataclass
class I18nLanguageListResponse(BaseList):
    """A class representing the I18n language list response info.

    Refer: https://developers.google.com/youtube/v3/docs/i18nLanguages/list#response_1
    """

    items: list[I18nLanguage] = field(repr=False)
