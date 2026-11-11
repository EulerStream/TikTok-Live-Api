#!/usr/bin/env python3
"""Rename tags in an OpenAPI spec, in place, for one generator.

A generator names an API group after its tag by its own rules, and those rules
can read an acronym badly: openapi-python-client splits a tag at every capital,
so "TikTok OAuth" becomes api.tik_tok_o_auth. Renaming the tag for that
generator alone ("TikTok Oauth" gives api.tik_tok_oauth) fixes the name there
without touching the spec the other SDKs are generated from.

The mapping file is a JSON object from a tag as the spec spells it to the tag
the generator should see:

    {"TikTok OAuth": "TikTok Oauth"}

A tag the spec does not use is ignored, so a mapping can be committed before
the server starts sending the tag. Renaming two tags to the same name merges
them into one group.

Run this after filter_spec.py, which matches tags as the spec spells them.

Usage: python3 rename_tags.py <path-to-openapi.json> <path-to-tag-names.json>
"""

import json
import sys

HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}


def renamed_once(tags, names):
    """The tags under their new names, in order, each kept once."""
    result = []
    for tag in tags:
        name = names.get(tag, tag)
        if name not in result:
            result.append(name)
    return result


def rename_tags(spec, names):
    """Rename tags on every operation and in the top-level list. Returns how many
    of the mapped tags the spec used."""
    used = set()

    for item in spec.get("paths", {}).values():
        for method, operation in item.items():
            if method not in HTTP_METHODS or not isinstance(operation, dict):
                continue
            tags = operation.get("tags")
            if not tags:
                continue
            used.update(tag for tag in tags if tag in names)
            operation["tags"] = renamed_once(tags, names)

    entries = []
    seen = set()
    for entry in spec.get("tags", []):
        if entry.get("name") in names:
            used.add(entry["name"])
            entry["name"] = names[entry["name"]]
        if entry.get("name") not in seen:
            seen.add(entry.get("name"))
            entries.append(entry)
    if "tags" in spec:
        spec["tags"] = entries

    return len(used)


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(f"Usage: {sys.argv[0]} <path-to-openapi.json> <path-to-tag-names.json>")

    spec_path, names_path = sys.argv[1:]

    with open(spec_path, encoding="utf-8") as fh:
        spec = json.load(fh)
    with open(names_path, encoding="utf-8") as fh:
        names = json.load(fh)

    renamed = rename_tags(spec, names)

    with open(spec_path, "w", encoding="utf-8") as fh:
        json.dump(spec, fh)

    print(f"Renamed {renamed} of {len(names)} mapped tag(s) in {spec_path}")


if __name__ == "__main__":
    main()
