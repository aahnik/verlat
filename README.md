# verlat

Get info about the latest release of a package on PyPI.

[![Code Quality](https://github.com/aahnik/verlat/actions/workflows/quality.yml/badge.svg)](https://github.com/aahnik/verlat/actions/workflows/quality.yml)
[![Tests](https://github.com/aahnik/verlat/actions/workflows/test.yml/badge.svg)](https://github.com/aahnik/verlat/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/aahnik/verlat/branch/main/graph/badge.svg?token=RO18ZS775L)](https://codecov.io/gh/aahnik/verlat)

## Installation

```shell
pip install verlat
```

## Usage

```python
from verlat import latest_version

release = latest_version("verlat")

print(release.version)
```
