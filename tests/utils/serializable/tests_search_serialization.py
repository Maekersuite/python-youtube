import pytest

from pyyoutube.models import SearchListResponse, SearchResult, SearchResultId, SearchResultSnippet

test = SearchListResponse(
    kind="youtube#searchListResponse",
    etag="",
    items=[
        SearchResult(
            kind="youtube#searchResult",
            etag="",
            id=SearchResultId(kind="youtube#video", videoId="123456"),
            snippet=SearchResultSnippet(title="Test Title", description="Test Description"),
        ),
        SearchResult(
            kind="youtube#searchResult",
            etag="",
            id=SearchResultId(kind="youtube#video", videoId="7891011"),
            snippet=SearchResultSnippet(title="Test Title 2", description="Test Description 2"),
        ),
        SearchResult(
            kind="youtube#searchResult",
            etag="",
            id=SearchResultId(kind="youtube#video", videoId="123456"),
            snippet=SearchResultSnippet(title="Test Title", description="Test Description"),
        ),
    ],
)


@pytest.mark.structure
def test_search_list_response_serialization():
    """Test the `serialize` method of the `SearchResponse` class."""
    data = test.serialize()
    assert isinstance(data, dict)
    assert data["items"][0]["id"]["videoId"] == "123456"
    assert data["items"][0]["snippet"]["title"] == "Test Title"
    assert data["items"][0]["snippet"]["description"] == "Test Description"
    assert data["items"][1]["id"]["videoId"] == "7891011"
    assert data["items"][1]["snippet"]["title"] == "Test Title 2"
    assert data["items"][1]["snippet"]["description"] == "Test Description 2"
    assert data["items"][2]["id"]["videoId"] == "123456"
    assert data["items"][2]["snippet"]["title"] == "Test Title"
    assert data["items"][2]["snippet"]["description"] == "Test Description"


@pytest.mark.structure
def test_search_list_response_deserialization():
    """Test the `deserialize` method of the `SearchResult` class."""
    data = test.serialize()
    assert isinstance(data, dict)

    deserialized = SearchListResponse.deserialize(data)
    assert isinstance(deserialized, SearchListResponse)
    assert deserialized.items[0].id.videoId == "123456"
    assert deserialized.items[0].snippet.title == "Test Title"
    assert deserialized.items[0].snippet.description == "Test Description"
    assert deserialized.items[1].id.videoId == "7891011"
    assert deserialized.items[1].snippet.title == "Test Title 2"
    assert deserialized.items[1].snippet.description == "Test Description 2"
    assert deserialized.items[2].id.videoId == "123456"
    assert deserialized.items[2].snippet.title == "Test Title"
