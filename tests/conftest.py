import pytest


@pytest.fixture(scope="session", autouse=True)
def initialize_test_environment(request) -> None:  # noqa: ANN001
    """Initialize the test environment dependencies."""
