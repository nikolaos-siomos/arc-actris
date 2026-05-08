"""ARC: Algorithm for Rayleigh and Raman Calculations."""

from .core import arc

try:
    from .version import __version__
except ImportError:
    __version__ = "unknown"

__all__ = ["arc", "__version__"]
