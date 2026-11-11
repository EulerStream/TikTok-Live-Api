#!/usr/bin/env python3
"""Print the version that follows a given one for a patch, minor or major bump.

The TypeScript and Python SDKs each publish two packages (the TikTok LIVE package
and the full API package) that always carry the same version number. That number
lives in sdk/<language>/version.txt, and the release and dry-run workflows use
this script to work out the next one once, for both packages.

Usage: python3 next_version.py <current-version> <patch|minor|major>
"""

import re
import sys

VERSION = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def next_version(current, bump):
    """Return the version after `current` for the given bump level."""
    match = VERSION.match(current.strip())
    if not match:
        raise ValueError(f"not a MAJOR.MINOR.PATCH version: {current.strip()!r}")
    major, minor, patch = (int(part) for part in match.groups())
    if bump == "major":
        return f"{major + 1}.0.0"
    if bump == "minor":
        return f"{major}.{minor + 1}.0"
    if bump == "patch":
        return f"{major}.{minor}.{patch + 1}"
    raise ValueError(f"bump must be patch, minor or major, got {bump!r}")


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: next_version.py <current-version> <patch|minor|major>")
    try:
        print(next_version(sys.argv[1], sys.argv[2]))
    except ValueError as exc:
        sys.exit(f"next_version: {exc}")


if __name__ == "__main__":
    main()
