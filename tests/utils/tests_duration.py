import pytest

from pyyoutube.utils.duration import get_video_duration


@pytest.mark.structure
@pytest.mark.parametrize(
    "duration_string, expected_seconds",
    [
        ("PT1H", 3600),
        ("PT1M", 60),
        ("PT1S", 1),
        ("PT1H30M", 5400),
        ("PT1H30M15S", 5415),
        ("P1DT2H3M4S", 93784),
        ("PT", 0),
    ],
)
def test_get_video_duration_valid(duration_string: str, expected_seconds: int):
    """Test the `get_video_duration` function with valid duration strings."""
    assert get_video_duration(duration_string) == expected_seconds


@pytest.mark.structure
def test_get_video_duration_invalid():
    """Test the `get_video_duration` function with invalid duration strings."""
    with pytest.raises(ValueError):
        get_video_duration("Invalid")
