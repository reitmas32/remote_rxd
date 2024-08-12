from fastapi import Header
from fastapi.requests import Request

from core.settings import settings
from core.utils.exceptions import NotAuthorizationException


def check_authorization(
    request: Request,
    X_Service_Name: str = Header(...),  # noqa: N803
    X_API_Key: str = Header(...),  # noqa: N803
):
    """
    Check authorization headers for API requests.

    This function checks the authorization headers provided in the request for API authentication.

    Args:
        request (Request): FastAPI request object.
        X_Service_Name (str): Service name header.
        X_API_Key (str): API key header.

    Returns:
        bool: True if authorization is successful, False otherwise.
    """

    return _check_root_authorization(
        X_API_Key=X_API_Key,
        X_Service_Name=X_Service_Name,
    )


def _check_root_authorization(
    X_API_Key: str = "",  # noqa: N803
    X_Service_Name: str = "",  # noqa: N803,
):
    """
    Check root authorization for API requests.

    This function checks the root authorization headers provided in the request for API authentication.

    Args:
        X_API_Key (str): API key header.
        X_Service_Name (str): Service name header.

    Returns:
        bool: True if root authorization is successful, False otherwise.

    Raises:
        NotAuthorizationException: If root authorization fails.
    """
    if X_API_Key != settings.ROOT_API_KEY or X_Service_Name != settings.ROOT_SERVICE_NAME:
        raise NotAuthorizationException(resource="/api/v1/services")
    return True
