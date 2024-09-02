from typing import Protocol, TypeVar

from .utils.serializable import Serializable

T = TypeVar("T", bound=Serializable)


class APIClientProto(Protocol):
    """Protocol for YouTube API client."""

    async def list(
        self,
        resource: type[T],
        path: str,
        params: dict[str, str],
    ) -> T:
        """Make a request to the YouTube Data API v3 and return the deserialized response.

        The `resource` argument must be a class that inherits from `Serializable`.

        Returns:
            T: The deserialized response.
        """
        ...
