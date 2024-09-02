import pytest

from pyyoutube.models import (
    Channel,
    ChannelContentDetails,
    ChannelListResponse,
    ChannelSnippet,
    ChannelStatistics,
    ChannelStatus,
    RelatedPlaylists,
)

test = ChannelListResponse(
    kind="youtube#channelListResponse",
    etag="",
    items=[
        Channel(
            kind="youtube#channel",
            etag="",
            id="123456",
            snippet=ChannelSnippet(title="Test Title", description="Test Description"),
            contentDetails=ChannelContentDetails(relatedPlaylists=RelatedPlaylists(likes="likes", uploads="uploads")),
            statistics=ChannelStatistics(
                viewCount=1000, subscriberCount=1000, hiddenSubscriberCount=False, videoCount=1000
            ),
            status=ChannelStatus(
                longUploadsStatus="longUploadsStatus",
                madeForKids=False,
                selfDeclaredMadeForKids=False,
            ),
        ),
    ],
)


@pytest.mark.structure
def test_channel_list_response_serialization():
    """Test the `serialize` method of the `ChannelListResponse` class."""
    data = test.serialize()
    assert isinstance(data, dict)
    assert data["items"][0]["id"] == "123456"
    assert data["items"][0]["snippet"]["title"] == "Test Title"
    assert data["items"][0]["snippet"]["description"] == "Test Description"


@pytest.mark.structure
def test_channel_list_response_deserialization():
    """Test the `deserialize` method of the `ChannelListResponse` class."""
    data = test.serialize()
    assert isinstance(data, dict)
    assert data["items"][0]["id"] == "123456"
    assert data["items"][0]["snippet"]["title"] == "Test Title"
    assert data["items"][0]["snippet"]["description"] == "Test Description"

    deserialized = ChannelListResponse.deserialize(data)
    assert isinstance(deserialized, ChannelListResponse)
    assert deserialized.items[0].id == "123456"
    assert deserialized.items[0].snippet.title == "Test Title"
    assert deserialized.items[0].snippet.description == "Test Description"
    assert deserialized.items[0].contentDetails.relatedPlaylists.likes == "likes"
    assert deserialized.items[0].contentDetails.relatedPlaylists.uploads == "uploads"
    assert deserialized.items[0].statistics.viewCount == 1000
    assert deserialized.items[0].statistics.subscriberCount == 1000
