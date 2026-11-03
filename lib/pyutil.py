#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""pyutil.py: small Python helpers that behave the same in CPython and in the in-browser engine
(Brython 3.12), shared by the store's checks.

- get_or_set(d, k, default): what d.setdefault(k, default) does. Brython 3.12's dict.setdefault
  stores int keys as strings, so a check written with setdefault gives different results in the
  browser; this helper uses plain item assignment, which both engines get right. As with
  setdefault, `default` is evaluated by the caller whether or not it is used.

Pure functions; no I/O at import.
"""

__all__ = ["get_or_set"]


def get_or_set(d, k, default):
    """d[k], after setting it to `default` when k is not yet a key (dict.setdefault)."""
    if k not in d:
        d[k] = default
    return d[k]
