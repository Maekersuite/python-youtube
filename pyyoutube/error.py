__all__ = ["PyYouTubeIncorrectParamsError", "PyYouTubeSessionError", "PyYouTubeServiceError"]


class PyYouTubeIncorrectParamsError(Exception):
    """Raised when there are incorrect or missing parameters for a request."""


class PyYouTubeSessionError(Exception):
    """Raised when the retrieval session (`ClientSession`) is closed or not initialized."""


class PyYouTubeServiceError(Exception):
    """Raise when YouTube service returns an error response."""

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f"HTTP error {self.status_code}: {self.message}"


class PyYouTubeQuotaReachedError(Exception):
    """Raise when YouTube service hits the quota limit."""

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f"Quota reached: {self.status_code} - {self.message}"


class PyYouTubeForbiddenError(Exception):
    """Raise when YouTube service returns a 403 Forbidden error."""

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f"Forbidden: {self.status_code} - {self.message}"
