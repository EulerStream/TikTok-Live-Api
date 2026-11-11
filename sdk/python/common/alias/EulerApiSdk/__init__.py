"""Deprecated import name. Use ``TikTokApiSdk`` or ``TikTokLiveApiSdk``.

This SDK used to be published as ``EulerApiSdk``. It is now two packages:
``tiktok-api-sdk`` (imported as ``TikTokApiSdk``, every route) and
``tiktok-live-api-sdk`` (imported as ``TikTokLiveApiSdk``, TikTok LIVE only).
Both ship this module so existing ``import EulerApiSdk`` code keeps working:
every ``EulerApiSdk`` and ``EulerApiSdk.*`` import is redirected to the
installed package, to the very same module objects, with a
``DeprecationWarning``.

When both packages are installed the general one wins, since it contains
everything the LIVE one does. This file is byte-identical in both packages so
that either may own it on disk.

Threads: import ``EulerApiSdk`` once (on the main thread is simplest) before
starting threads that import through this name. On Python 3.13 and earlier the
interpreter makes a package visible to other threads before its ``__init__``
has run, so two threads whose very first SDK imports are different
``EulerApiSdk.*`` paths can race the redirect below and get a
``ModuleNotFoundError``. Once the first import has completed, imports from any
thread are safe. The new import names are not affected.
"""

import importlib
import importlib.abc
import importlib.util
import sys
import warnings

_ALIAS = __name__
_TARGETS = ("TikTokApiSdk", "TikTokLiveApiSdk")


def _pick_target():
    for name in _TARGETS:
        if importlib.util.find_spec(name) is not None:
            return name
    raise ImportError(
        "EulerApiSdk is a deprecated alias and needs tiktok-api-sdk or "
        "tiktok-live-api-sdk to be installed."
    )


_TARGET = _pick_target()


class _AliasFinder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    """Resolve ``EulerApiSdk.x`` to the already-imported ``<target>.x`` module.

    It sits first on ``sys.meta_path`` so it answers before the normal path
    finder, which would otherwise load a second copy of each submodule (or
    stale files a previous ``EulerApiSdk`` install left in this folder).
    """

    def __init__(self):
        self._real_specs = {}

    def find_spec(self, fullname, path=None, target=None):
        if fullname == _ALIAS or fullname.startswith(_ALIAS + "."):
            return importlib.util.spec_from_loader(fullname, self)
        return None

    def create_module(self, spec):
        real = importlib.import_module(_TARGET + spec.name[len(_ALIAS):])
        self._real_specs[spec.name] = real.__spec__
        return real

    def exec_module(self, module):
        # The import system has just pointed the real module's __spec__ at the
        # alias name. Put the real one back.
        module.__spec__ = self._real_specs.pop(module.__spec__.name)


if not any(isinstance(finder, _AliasFinder) for finder in sys.meta_path):
    sys.meta_path.insert(0, _AliasFinder())

warnings.warn(
    f"EulerApiSdk is deprecated; import {_TARGET} instead.",
    DeprecationWarning,
    stacklevel=2,
)

sys.modules[_ALIAS] = importlib.import_module(_TARGET)
