"""
This package includes shared entities that are used across the application.
"""

from .base import InternalEntity, PublicEntity, _InternalEntity, _PublicEntity
from .response import (
    ErrorDetail,
    ErrorResponse,
    ErrorResponseMulti,
    ErrorType,
    Response,
    ResponseMulti,
    _Response,
)

__all__ = (
    "InternalEntity",
    "_InternalEntity",
    "PublicEntity",
    "_PublicEntity",
    "ResponseMulti",
    "Response",
    "_Response",
    "ErrorType",
    "ErrorDetail",
    "ErrorResponse",
    "ErrorResponseMulti",
)
