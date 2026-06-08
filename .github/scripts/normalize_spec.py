#!/usr/bin/env python3
"""Normalize a downloaded OpenAPI spec for code generation.

The live spec at https://tiktok.eulerstream.com/dashboard/openapi occasionally
tags a single operation with more than one tag (e.g. an operation under both
"TikTok LIVE Rooms" and "TikTok LIVE Premium"). The per-tag SDK generators
(C#, Go, Java, TypeScript) emit one API class per tag, so a multi-tagged
operation produces the *same* request/response types in two classes, which then
collide at compile time:

    The namespace 'EulerApiSdk.Api' already contains a definition for
    'ISendRoomChatApiResponse'
    ApiRetrieveBulkLiveCheckRequest redeclared in this block

OpenAPI permits multiple tags, but these generators cannot represent the same
operation in two API groups. This script collapses every operation to its first
tag so each operation lands in exactly one generated class, making generation
deterministic regardless of which spec variant the server returns.

Usage: python3 normalize_spec.py <path-to-openapi.json>
"""

import json
import sys

HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: normalize_spec.py <path-to-openapi.json>")

    spec_path = sys.argv[1]
    with open(spec_path, encoding="utf-8") as fh:
        spec = json.load(fh)

    collapsed = []
    for path, item in (spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for method, op in item.items():
            if method.lower() not in HTTP_METHODS or not isinstance(op, dict):
                continue
            tags = op.get("tags")
            if isinstance(tags, list) and len(tags) > 1:
                op["tags"] = [tags[0]]
                collapsed.append(
                    f"  {method.upper()} {path}: {tags} -> [{tags[0]!r}]"
                )

    with open(spec_path, "w", encoding="utf-8") as fh:
        json.dump(spec, fh)
        fh.write("\n")

    if collapsed:
        print(f"normalize_spec: collapsed {len(collapsed)} multi-tagged operation(s):")
        print("\n".join(collapsed))
    else:
        print("normalize_spec: no multi-tagged operations found.")


if __name__ == "__main__":
    main()
