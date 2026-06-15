#!/usr/bin/env python3
"""Normalize a downloaded OpenAPI spec for code generation.

The live spec at https://api.eulerstream.com/dashboard/openapi is served
through a cache and is not always consistent between requests. Two variants
have been observed to break the per-tag SDK generators (C#, Go, Java, and
TypeScript), which emit one API class — and one ``I{OperationId}ApiResponse``
interface / ``Api{OperationId}Request`` type — per tag/operation:

1. Multi-tagged operations. A single operation tagged with more than one tag
   (e.g. both "TikTok LIVE Rooms" and "TikTok LIVE Premium") is generated into
   two API classes, so its request/response types are declared twice.

2. Duplicate operationIds. A stale variant still exposes the legacy
   "TikTok LIVE Premium" umbrella operations alongside the same operations under
   their newer granular tags ("TikTok LIVE", "Rooms", "Anchors", ...). The
   operationIds repeat, so the generated ``I{OperationId}ApiResponse`` interface
   is declared twice and the build fails:

       The namespace 'EulerApiSdk.Api' already contains a definition for
       'IRetrieveBulkLiveCheckApiResponse'
       ApiRetrieveBulkLiveCheckRequest redeclared in this block

This script makes generation deterministic by:

  * collapsing every operation to a single tag, and
  * dropping duplicate operationIds, keeping one occurrence per operationId.

In both cases the legacy "TikTok LIVE Premium" grouping is de-prioritized so the
granular tags survive.

Usage: python3 normalize_spec.py <path-to-openapi.json>
"""

import json
import sys

HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}

# Legacy umbrella tag whose operations duplicate the newer granular ones. When a
# tag or operationId conflict must be resolved, prefer to drop this one.
LEGACY_TAG = "TikTok LIVE Premium"


def preferred_tag(tags):
    """Pick the single tag to keep, de-prioritizing the legacy umbrella tag."""
    non_legacy = [t for t in tags if t != LEGACY_TAG]
    return non_legacy[0] if non_legacy else tags[0]


def iter_operations(spec):
    """Yield (path, method, operation) for every HTTP operation in the spec."""
    for path, item in (spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for method, op in list(item.items()):
            if method.lower() in HTTP_METHODS and isinstance(op, dict):
                yield path, method, op


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: normalize_spec.py <path-to-openapi.json>")

    spec_path = sys.argv[1]
    with open(spec_path, encoding="utf-8") as fh:
        spec = json.load(fh)

    # Pass 1: collapse multi-tagged operations to a single tag.
    collapsed = []
    for path, method, op in iter_operations(spec):
        tags = op.get("tags")
        if isinstance(tags, list) and len(tags) > 1:
            keep = preferred_tag(tags)
            op["tags"] = [keep]
            collapsed.append(f"  {method.upper()} {path}: {tags} -> [{keep!r}]")

    # Pass 2: drop duplicate operationIds. Decide the keeper per operationId
    # first (preferring a non-legacy tag), then remove the other occurrences.
    by_opid = {}
    for path, method, op in iter_operations(spec):
        opid = op.get("operationId")
        if opid:
            by_opid.setdefault(opid, []).append((path, method, op))

    drop = set()  # (path, method) pairs to remove
    dropped_log = []
    for opid, occurrences in by_opid.items():
        if len(occurrences) < 2:
            continue

        def rank(item):
            _, _, o = item
            tags = o.get("tags") or []
            return 1 if (tags and tags[0] == LEGACY_TAG) else 0

        keeper = min(occurrences, key=rank)  # rank 0 (non-legacy) wins
        for path, method, o in occurrences:
            if (path, method) == (keeper[0], keeper[1]):
                continue
            drop.add((path, method))
            tag = (o.get("tags") or ["<none>"])[0]
            dropped_log.append(
                f"  {method.upper()} {path} (operationId={opid}, tag={tag!r})"
            )

    paths = spec.get("paths") or {}
    for path, method in drop:
        item = paths.get(path)
        if isinstance(item, dict) and method in item:
            del item[method]
            # Remove the path entirely if it has no remaining operations.
            if not any(m.lower() in HTTP_METHODS for m in item):
                del paths[path]

    with open(spec_path, "w", encoding="utf-8") as fh:
        json.dump(spec, fh)
        fh.write("\n")

    if collapsed:
        print(f"normalize_spec: collapsed {len(collapsed)} multi-tagged operation(s):")
        print("\n".join(collapsed))
    else:
        print("normalize_spec: no multi-tagged operations found.")

    if dropped_log:
        print(f"normalize_spec: dropped {len(dropped_log)} duplicate operation(s):")
        print("\n".join(dropped_log))
    else:
        print("normalize_spec: no duplicate operationIds found.")


if __name__ == "__main__":
    main()
