"""function's params checker."""

import logging
from typing import Optional, Union

from pyyoutube.utils.constants import RESOURCE_PARTS_MAPPING

from ..error import PyYouTubeIncorrectParamsError

logger = logging.getLogger(__name__)


def enf_comma_separated(
    field: str,
    value: Optional[Union[str, list]],
) -> Optional[str]:
    """Check to see if field's value type belong to correct type. If it is, return api need value.

    Returns:
        Api needed string
    """
    if value is None:
        return None

    try:
        if isinstance(value, str):
            return value
        elif isinstance(value, list):
            return ",".join(value)
    except (TypeError, ValueError) as ex:
        raise PyYouTubeIncorrectParamsError(
            f"Parameter ({field}) must be single str,comma-separated str,list,tuple or set"
        ) from ex


def enf_parts(resource: str, value: Optional[Union[str, list]], check: bool = True) -> str:
    """Check to see if value type belong to correct type, and if resource support the given part. If it is, return api need value.

    Args:
        resource (str):
            Name of the resource you want to retrieve.
        value (str, list, tuple, set, Optional):
            Value for the part.
        check (bool, optional):
            Whether check the resource properties.

    Returns:
        Api needed part string
    """  # noqa: E501
    if value is None:
        parts = RESOURCE_PARTS_MAPPING[resource]

    elif isinstance(value, str):
        parts = set(value.split(","))
    elif isinstance(value, list):
        parts = set(value)

    # Remove leading/trailing whitespaces
    parts = set({part.strip() for part in parts})

    # Check parts whether support
    if check:
        support_parts = RESOURCE_PARTS_MAPPING[resource]
        if not support_parts.issuperset(parts):
            not_support_parts = ",".join(parts.difference(support_parts))
            raise PyYouTubeIncorrectParamsError(f"Parts {not_support_parts} for resource {resource} not support")
    return ",".join(parts)
