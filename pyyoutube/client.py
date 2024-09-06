import asyncio
from contextlib import suppress
from dataclasses import dataclass
from typing import Any, ClassVar, Never, Optional, TypeVar

import orjson
from aiohttp import (
    ClientResponse,
    ClientSession,
    ClientTimeout,
    TCPConnector,
    TraceConfig,
)

from .error import PyYouTubeForbiddenError, PyYouTubeQuotaReachedError, PyYouTubeServiceError, PyYouTubeSessionError
from .protocols import APIClientProto
from .resources import (
    CaptionsResource,
    ChannelsResource,
    CommentsResource,
    I18nLanguagesResource,
    I18nRegionsResource,
    MembersResource,
    PlaylistsResource,
    SearchResource,
    SubscriptionsResource,
    VideosResource,
)
from .utils.serializable import Serializable

T = TypeVar("T", bound=Serializable)


# Base class for authentication methods
class AuthenticationMethod:
    """Base class for authentication methods."""


@dataclass
class AccessTokenAuthentication(AuthenticationMethod):
    """Authentication based on existing user's access token."""

    access_token: str
    refresh_token: Optional[str] = None


@dataclass
class APIKeyAuthentication(AuthenticationMethod):
    """Authentication based on Developer Console App API key."""

    api_key: str


@dataclass
class YouTubeDataAPIError:
    """A class representing the error object from the YouTube Data API."""

    message: str
    domain: str
    reason: str


class Client(APIClientProto):
    """YouTube Data API v3 client. Allows getting structured resources from the API."""

    # The ETag caching is not implemented intentionally due to the following reasons:
    # - We need to collect the most recent data (statistics part) for some resources (e.g. videos).
    # - aiohttp ClientSession doesn't keep connections alive if headers change (ETag is provided via headers).

    base_url: ClassVar[str] = "https://www.googleapis.com/youtube/v3/"

    captions: CaptionsResource
    channels: ChannelsResource
    comments: CommentsResource
    i18n_languages: I18nLanguagesResource
    i18n_regions: I18nRegionsResource
    members: MembersResource
    playlists: PlaylistsResource
    search: SearchResource
    subscriptions: SubscriptionsResource
    videos: VideosResource

    session: ClientSession | None = None
    """Current session for the API requests. Can be created manually or using context manager."""

    concurrent_connections: int = 100
    """The maximum number of concurrent connections to make."""

    def _ua(self, gzip: bool = True) -> str:
        """Generate a User-Agent string."""
        agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"  # noqa: E501
        if gzip:
            agent += " (gzip)"
        return agent

    def __init__(
        self,
        auth: AuthenticationMethod,
        timeout: Optional[ClientTimeout] = None,
        proxy: Optional[str] = None,
        headers: Optional[dict[str, str]] = None,
    ):
        """Initialize the YouTube API client with authentication and connection settings."""
        self.auth = auth
        self.timeout = timeout or ClientTimeout(total=30, connect=3)
        self.proxy = proxy
        self.headers: dict[str, str] = {"Accept-Encoding": "gzip", "User-Agent": self._ua(gzip=True)}
        self.semaphore = asyncio.Semaphore(self.concurrent_connections)

        if headers:
            self.headers.update(headers)

        self.captions = CaptionsResource(self)
        self.channels = ChannelsResource(self)
        self.comments = CommentsResource(self)
        self.i18n_languages = I18nLanguagesResource(self)
        self.i18n_regions = I18nRegionsResource(self)
        self.members = MembersResource(self)
        self.playlists = PlaylistsResource(self)
        self.search = SearchResource(self)
        self.subscriptions = SubscriptionsResource(self)
        self.videos = VideosResource(self)

        if isinstance(self.auth, AccessTokenAuthentication):
            self.headers.update({"Authorization": f"Bearer {self.auth.access_token}"})

    async def __aenter__(self) -> "Client":
        """Async context manager entry point."""
        self.tracer = TraceConfig()
        self.connector = TCPConnector(limit=self.concurrent_connections, keepalive_timeout=30, ttl_dns_cache=300)
        self.session = ClientSession(
            timeout=self.timeout, trace_configs=[self.tracer], connector=self.connector, headers=self.headers
        )

        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:  # noqa: ANN001
        """Async context manager exit point. Closes the session if it's still open."""
        if self.session and not self.session.closed:
            await self.session.close()
        await asyncio.sleep(0)

    def _handle_response_errors(self, code: int, error: YouTubeDataAPIError) -> Never:
        """Handle the errors from the YouTube Data API. Docs: https://developers.google.com/youtube/v3/docs/errors."""
        if error.reason == "quotaExceeded":
            raise PyYouTubeQuotaReachedError(code, error.message)
        elif error.reason == "forbidden":
            raise PyYouTubeForbiddenError(code, error.message)
        else:
            raise PyYouTubeServiceError(code, error.message)

    async def _handle_error(self, response: ClientResponse) -> None:
        status: int = response.status

        data: dict[str, Any] | None = None
        with suppress(Exception):
            data = await response.json(loads=orjson.loads)

        if not data:
            raise PyYouTubeServiceError(status, "Unknown YouTube Data API error")

        try:
            errors: list[YouTubeDataAPIError] = []
            if status >= 400:  # noqa: PLR2004
                code: int = data["error"]["code"]
                errors = [
                    YouTubeDataAPIError(message=error["message"], domain=error["domain"], reason=error["reason"])
                    for error in data["error"]["errors"]
                ]
        except Exception as ex:
            raise PyYouTubeServiceError(status, "Unknown YouTube Data API error") from ex

        if not errors:
            raise PyYouTubeServiceError(status, "Unknown YouTube Data API error")

        for error in errors:
            self._handle_response_errors(code, error)

    async def list(
        self,
        resource: type[T],
        path: str,
        params: dict[str, str],
    ) -> T:
        """Make a request to the YouTube Data API v3 and return the deserialized response.

        Args:
            resource (type[T]): The Serializable class to deserialize the response into.
            path (str): The API endpoint path.
            params (dict[str, str]): Query parameters for the request.

        Returns:
            T: The deserialized response.

        Raises:
            PyYouTubeSessionError: If the async session is not initialized or closed.
            PyYouTubeServiceError: If there's an error with the API request or response.
        """
        # Check if the session is initialized and open
        if not self.session or self.session.closed:
            raise PyYouTubeSessionError("Async session is not initialized or closed")

        # Construct the full URL if necessary
        if not path.startswith("http"):
            path = f"{self.base_url}{path}"

        # Add API key to params if using APIKeyAuthentication
        if params and isinstance(self.auth, APIKeyAuthentication):
            params.update({"key": self.auth.api_key})

        # Remove None values from params
        if params:
            params = {key: value for key, value in params.items() if value is not None}

        # Make the API request
        async with (
            self.semaphore,
            self.session.get(
                url=path,
                params=params,
                proxy=self.proxy,
            ) as response,
        ):
            # Handle the response
            if response.status != 200:  # noqa: PLR2004
                await self._handle_error(response)

            try:
                data: dict[str, str] = await response.json(loads=orjson.loads)
            except Exception as ex:
                raise PyYouTubeServiceError(
                    response.status, f"Unable to read response message ({ex.__class__.__name__}): {ex}"
                ) from ex

            # Deserialize and return the response data
            return resource.deserialize(data)
