from abc import ABC

from ..protocols import APIClientProto


class Resource(ABC):
    """Resource base class."""

    _name: str
    """The name of the resource that is used to access it from the API client."""

    _client: APIClientProto
    """The API client that is used to access the resource."""

    def __init__(self, client: APIClientProto) -> None:
        self._client = client
