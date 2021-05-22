"""Fetch info about the latest release of a package on PyPI."""

from typing import List, Optional, Union

import requests
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class Release(BaseModel):
    """The latest release information."""

    # pylint: disable=too-few-public-methods
    name: str
    author: Optional[str]
    author_email: Optional[str]
    description: Optional[str]
    home_page: Optional[str]
    keywords: Optional[Union[List[str], str]]
    summary: Optional[str]
    version: str
    release_url: str


def latest_release(project_name: str) -> Release:
    """Get the latest release of a project on PyPI.

    Args:
        project_name (str): the name of package whose info you want

    Returns:
        release (Release): the latest release
    """
    url = f"https://pypi.org/pypi/{project_name}/json"
    response_info = requests.get(url).json()["info"]
    return Release(**response_info)
