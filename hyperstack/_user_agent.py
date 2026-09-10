# coding: utf-8

"""Forced Hyperstack client identification headers.

Maintained in sdk-generator (util/python/_user_agent.py) and copied into the
generated package by the `add-hyperstack-headers` task. Do not edit in the SDK
repos -- changes there are overwritten on the next release.

The module name deliberately avoids the substring "hyperstack": the generator
pipeline rewrites absolute imports in this package tree, and keeping this file
out of that namespace makes it impossible for the rewrite to touch it.
"""

import platform
import sys

CLIENT_HEADER = "Hyperstack-Client"
USER_AGENT_HEADER = "User-Agent"

# Stamped by the sdk-generator Taskfile, per flavour:
#   python       -> hyperstack-python-sdk
#   python_async -> hyperstack-python-sdk-async
SDK_NAME = "hyperstack-python-sdk"

# Header names we always own, matched case-insensitively so a caller cannot
# smuggle in a second copy under different casing.
_FORCED = (CLIENT_HEADER.lower(), USER_AGENT_HEADER.lower())

_cache = None


def _sdk_version():
    # Imported lazily: this module is pulled in from api_client, which is itself
    # imported while the package __init__ is still executing.
    try:
        from . import __version__

        return __version__ or "unknown"
    except Exception:
        return "unknown"


def _normalize_os(value):
    v = (value or "").strip().lower()
    if v.startswith("darwin") or v.startswith("mac"):
        return "darwin"
    if v.startswith("win") or v == "cygwin":
        return "windows"
    if v.startswith("linux"):
        return "linux"
    return v.replace(" ", "-") or "unknown"


def _normalize_arch(value):
    v = (value or "").strip().lower()
    if v in ("x86_64", "x64", "amd64"):
        return "x86_64"
    if v in ("aarch64", "arm64"):
        return "arm64"
    if v in ("i386", "i686", "x86"):
        return "386"
    return v or "unknown"


def _sanitize(value):
    """Keep printable ASCII only, capped at 256 chars.

    Header values must not carry control characters (CR/LF would allow response
    splitting) and some HTTP stacks reject non-ASCII outright.
    """
    return "".join(c for c in value if 0x20 <= ord(c) < 0x7F)[:256]


def _build():
    client = _sanitize("%s/%s" % (SDK_NAME, _sdk_version()))
    try:
        runtime = "Python/%s" % platform.python_version()
    except Exception:
        runtime = "Python/unknown"
    try:
        os_name = _normalize_os(sys.platform)
        arch = _normalize_arch(platform.machine())
    except Exception:
        os_name, arch = "unknown", "unknown"
    user_agent = _sanitize("%s (%s; %s/%s)" % (client, runtime, os_name, arch))
    return {CLIENT_HEADER: client, USER_AGENT_HEADER: user_agent}


def hyperstack_headers():
    """Return the forced identification headers, computed once and cached."""
    global _cache
    if _cache is None:
        _cache = _build()
    return _cache


def apply_hyperstack_headers(header_params):
    """Force the identification headers onto a mutable header dict.

    Any caller-supplied variant is dropped first, so exactly one of each is sent.
    """
    if header_params is None:
        return header_params
    for key in [k for k in list(header_params) if str(k).lower() in _FORCED]:
        del header_params[key]
    header_params.update(hyperstack_headers())
    return header_params
