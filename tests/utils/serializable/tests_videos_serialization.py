import pytest

from pyyoutube.models import (
    Player,
    RegionRestriction,
    Thumbnails,
    Video,
    VideoContentDetails,
    VideoSnippet,
    VideoStatistics,
    VideoStatus,
    VideoTopicDetails,
)
from pyyoutube.models.common import Thumbnail

test = Video(
    kind="youtube#video",
    etag="",
    id="123456",
    snippet=VideoSnippet(
        publishedAt="2024-01-01T00:00:00Z",
        channelId="123456",
        title="Test",
        description="Test",
        thumbnails=Thumbnails(
            default=Thumbnail(
                url="https://www.youtube.com/watch?v=123456",
                width=1280,
                height=720,
            ),
            medium=Thumbnail(
                url="https://www.youtube.com/watch?v=123456",
                width=1280,
                height=720,
            ),
            high=Thumbnail(
                url="https://www.youtube.com/watch?v=123456",
                width=1280,
                height=720,
            ),
        ),
    ),
    contentDetails=VideoContentDetails(
        duration="PT1H1M1S",
        dimension="hd",
        definition="hd",
        caption="true",
        licensedContent=True,
        regionRestriction=RegionRestriction(
            allowed=["US"],
        ),
    ),
    statistics=VideoStatistics(
        viewCount=1000,
        likeCount=1000,
        commentCount=1000,
    ),
    status=VideoStatus(
        uploadStatus="uploaded",
        privacyStatus="public",
    ),
    topicDetails=VideoTopicDetails(
        topicCategories=["123456"],
    ),
    player=Player(
        embedHtml="",
    ),
)


@pytest.mark.structure
def test_video_serialization():
    serialized = test.serialize()
    assert isinstance(serialized, dict)
    assert "snippet" in serialized
    assert "statistics" in serialized
    assert "status" in serialized
    assert "topicDetails" in serialized
    assert "player" in serialized
    assert "contentDetails" in serialized

    assert serialized["snippet"]["publishedAt"] == "2024-01-01T00:00:00Z"
    assert serialized["snippet"]["channelId"] == "123456"
    assert serialized["snippet"]["title"] == "Test"
    assert serialized["snippet"]["description"] == "Test"
    assert serialized["snippet"]["thumbnails"]["default"]["url"] == "https://www.youtube.com/watch?v=123456"
    assert serialized["snippet"]["thumbnails"]["default"]["width"] == 1280
    assert serialized["snippet"]["thumbnails"]["default"]["height"] == 720
    assert serialized["snippet"]["thumbnails"]["medium"]["url"] == "https://www.youtube.com/watch?v=123456"


@pytest.mark.structure
def test_video_deserialization():
    """Verify that all video fields and their types are correctly deserialized."""
    serialized = test.serialize()
    deserialized = Video.deserialize(serialized)
    assert isinstance(deserialized, Video)
    assert isinstance(deserialized.snippet, VideoSnippet)
    assert isinstance(deserialized.statistics, VideoStatistics)
    assert isinstance(deserialized.status, VideoStatus)
    assert isinstance(deserialized.topicDetails, VideoTopicDetails)
    assert isinstance(deserialized.player, Player)
    assert isinstance(deserialized.contentDetails, VideoContentDetails)

    assert deserialized.snippet.publishedAt == "2024-01-01T00:00:00Z"
    assert deserialized.snippet.channelId == "123456"
    assert deserialized.snippet.title == "Test"
    assert deserialized.snippet.description == "Test"
    assert deserialized.snippet.thumbnails.default.url == "https://www.youtube.com/watch?v=123456"
    assert deserialized.snippet.thumbnails.default.width == 1280
    assert deserialized.snippet.thumbnails.default.height == 720
    assert deserialized.snippet.thumbnails.medium.url == "https://www.youtube.com/watch?v=123456"

    assert deserialized.contentDetails.duration == "PT1H1M1S"
    assert deserialized.contentDetails.dimension == "hd"
    assert deserialized.contentDetails.definition == "hd"
    assert deserialized.contentDetails.caption == "true"
    assert deserialized.contentDetails.licensedContent is True
    assert deserialized.contentDetails.regionRestriction.allowed == ["US"]

    assert deserialized.statistics.viewCount == 1000
    assert deserialized.statistics.likeCount == 1000
    assert deserialized.statistics.commentCount == 1000

    assert deserialized.status.uploadStatus == "uploaded"
    assert deserialized.status.privacyStatus == "public"

    assert deserialized.topicDetails.topicCategories == ["123456"]

    assert deserialized.player.embedHtml == ""
