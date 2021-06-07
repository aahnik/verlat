# verlat

Get info about the latest release of a package on PyPI.

[![Code Quality](https://github.com/aahnik/verlat/actions/workflows/quality.yml/badge.svg)](https://github.com/aahnik/verlat/actions/workflows/quality.yml)
[![Tests](https://github.com/aahnik/verlat/actions/workflows/test.yml/badge.svg)](https://github.com/aahnik/verlat/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/aahnik/verlat/branch/main/graph/badge.svg?token=RO18ZS775L)](https://codecov.io/gh/aahnik/verlat)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/verlat)

## Installation

```shell
pip install --upgrade verlat
```

## Usage

```python
from verlat import latest_release

package = "verlat" # name of the package on PyPI
release = latest_release(package)
print(release.version)
```

## Application

Many CLI apps like
[`pip`](https://pip.pypa.io/en/stable/)
or
[`gh`](https://cli.github.com/)
produce warnings if you are not using their latest release.

Using `verlat` you can fetch information about the latest release
of your package on PyPI.
You can then compare the version strings of the latest release and
the currently running program.
Based on whether it is a major or minor release, or whatever logic you have,
you can log useful information for the user.

For dealing with version strings, you may use the
[`packaging`](https://pypi.org/project/packaging/v)
library.

Here is an example code that demonstrates practical application of `verlat`.

> **NOTE** Assuming that you have build your python package using
[`poetry`](https://python-poetry.org/docs/),
and the `version` key exists under `[tool.poetry]` of your
[`pyproject.toml`](https://python-poetry.org/docs/pyproject/)
file.

```python
# __init__.py

import logging
from importlib.metadata import version

from verlat import latest_release

__version__ = version(__package__)
latest = latest_release(__package__)


def major(string):
    # based on semantic versioning
    return int(string.split(".", 1)[0])


if major(__version__) < major(latest.version):
    logging.warning(
        f"A new major release for {__package__} is availaible.\
        \nDownload it from {latest.release_url}"
    )

```
