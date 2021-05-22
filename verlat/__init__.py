"""Package verlat.

Get info about the latest release of a package on PyPI.

MIT License

Copyright (c) 2021 Aahnik Daw

https://github.com/aahnik/verlat
"""

from importlib.metadata import version

from verlat.verlat import Release, latest_release

__version__ = version(__package__)
