#!/usr/bin/env python3
"""Cut a normalized OpenAPI spec down to the operations one SDK package ships.

The TypeScript and Python SDKs are published twice: a general package built
from the full spec, and a TikTok LIVE package built from a subset. Which tags
the subset keeps is declared once, in spec/packages.json, so both languages
agree:

    {
      "live": {
        "includeTagPrefixes": ["TikTok LIVE"],
        "includeTags": ["TikTok WebSocket API", "Accounts", "Authentication"]
      }
    }

An operation is kept when one of its tags starts with a listed prefix or
equals a listed name. A tag the rules do not mention is dropped, so a new
"TikTok LIVE ..." tag joins the LIVE package automatically and any other new
tag stays general-only.

Run this after normalize_spec.py, which leaves every operation with exactly
one tag. It then:

  * removes the operations that do not match, and any path left without one,
  * removes every component (schemas, parameters, responses, request bodies,
    examples, headers) that the kept operations no longer reach, following
    $ref transitively so the generators emit no orphaned models,
  * removes top-level tag entries that no kept operation uses, and
  * prints the kept and dropped tags with their operation counts.

securitySchemes are left alone: they are referenced by name, not by $ref.

It fails if nothing is left, or if an includeTags entry matches no tag in
the spec (a typo guard; it does not fire when the spec gains a new tag).

Usage: python3 filter_spec.py <path-to-openapi.json> <path-to-packages.json> <package>
"""

import json
import sys

HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}

# Counted under this name in the report when an operation has no tag.
UNTAGGED = "<none>"

COMPONENTS_PREFIX = "#/components/"

# Referenced by name from `security` requirements rather than by $ref, so
# reachability cannot see them. Never pruned.
UNPRUNED_SECTIONS = {"securitySchemes"}


def matches(tag, rules):
    """True when the rules keep operations carrying this tag."""
    if tag in rules.get("includeTags", []):
        return True
    return any(tag.startswith(prefix) for prefix in rules.get("includeTagPrefixes", []))


def iter_operations(spec):
    """Yield (path, method, operation) for every HTTP operation in the spec."""
    for path, item in (spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for method, op in list(item.items()):
            if method.lower() in HTTP_METHODS and isinstance(op, dict):
                yield path, method, op


def collect_refs(node, found):
    """Add every $ref string under node to found."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "$ref" and isinstance(value, str):
                found.add(value)
            else:
                collect_refs(value, found)
    elif isinstance(node, list):
        for value in node:
            collect_refs(value, found)
    return found


def reachable_components(spec):
    """Every '#/components/<section>/<name>' the remaining paths reach."""
    components = spec.get("components") or {}
    pending = list(collect_refs(spec.get("paths") or {}, set()))
    reached = set()
    while pending:
        target = pending.pop()
        if target in reached or not target.startswith(COMPONENTS_PREFIX):
            continue
        reached.add(target)
        section, _, name = target[len(COMPONENTS_PREFIX):].partition("/")
        node = (components.get(section) or {}).get(name)
        if node is not None:
            pending.extend(collect_refs(node, set()))
    return reached


def filter_spec(spec, rules):
    """Filter spec in place and return {"kept": {tag: n}, "dropped": {tag: n}}."""
    present = set()
    for _, _, op in iter_operations(spec):
        present.update(op.get("tags") or [])
    unmatched = [tag for tag in rules.get("includeTags", []) if tag not in present]
    if unmatched:
        raise ValueError(f"includeTags entries match no tag in the spec: {unmatched}")

    kept, dropped, used_tags = {}, {}, set()
    paths = spec.get("paths") or {}
    for path, method, op in list(iter_operations(spec)):
        tags = op.get("tags") or []
        label = tags[0] if tags else UNTAGGED
        if any(matches(tag, rules) for tag in tags):
            kept[label] = kept.get(label, 0) + 1
            used_tags.update(tags)
            continue
        dropped[label] = dropped.get(label, 0) + 1
        del paths[path][method]
        if not any(key.lower() in HTTP_METHODS for key in paths[path]):
            del paths[path]

    if not kept:
        raise ValueError("the rules left no operations in the spec")

    reached = reachable_components(spec)
    for section, entries in (spec.get("components") or {}).items():
        if section in UNPRUNED_SECTIONS or not isinstance(entries, dict):
            continue
        for name in list(entries):
            if f"{COMPONENTS_PREFIX}{section}/{name}" not in reached:
                del entries[name]

    if isinstance(spec.get("tags"), list):
        spec["tags"] = [
            tag
            for tag in spec["tags"]
            if not isinstance(tag, dict) or tag.get("name") in used_tags
        ]

    return {"kept": kept, "dropped": dropped}


def main() -> None:
    if len(sys.argv) != 4:
        sys.exit(
            "usage: filter_spec.py <path-to-openapi.json> <path-to-packages.json> <package>"
        )
    spec_path, packages_path, package = sys.argv[1:]

    with open(packages_path, encoding="utf-8") as fh:
        packages = json.load(fh)
    if package not in packages:
        sys.exit(
            f"filter_spec: unknown package {package!r}; "
            f"{packages_path} defines {sorted(packages)}"
        )

    with open(spec_path, encoding="utf-8") as fh:
        spec = json.load(fh)

    try:
        report = filter_spec(spec, packages[package])
    except ValueError as exc:
        sys.exit(f"filter_spec: {exc}")

    with open(spec_path, "w", encoding="utf-8") as fh:
        json.dump(spec, fh)
        fh.write("\n")

    for outcome in ("kept", "dropped"):
        counts = report[outcome]
        total = sum(counts.values())
        print(f"filter_spec: {package}: {outcome} {total} operation(s) in {len(counts)} tag(s):")
        for tag in sorted(counts):
            print(f"  {counts[tag]:>3}  {tag}")


if __name__ == "__main__":
    main()
