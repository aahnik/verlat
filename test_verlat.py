#!/usr/bin/env python

# pylint: skip-file

from verlat import Release, latest_release


def test_release_object():
    release = Release(
        **{
            "name": "demo",
            "author": "Aahnik Daw",
            "version": "0.0.1",
            "release_url": "https://aahnik.dev",
        }
    )  # a fake release object

    assert release.name == "demo"
    assert release.author == "Aahnik Daw"
    assert release.version == "0.0.1"
    assert release.release_url == "https://aahnik.dev"


def test_latest_release():
    release = latest_release("requests")
    assert release.version is not None
    assert release.name == "requests"
