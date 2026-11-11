"""Tests for filter_spec.py.

Run with: python3 -m unittest discover -s .github/scripts -p 'test_filter_spec.py' -v
"""

import copy
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SCRIPT = os.path.join(HERE, "filter_spec.py")
SPEC_PATH = os.path.join(REPO, "spec", "openapi.json")
PACKAGES_PATH = os.path.join(REPO, "spec", "packages.json")

sys.path.insert(0, HERE)

import filter_spec  # noqa: E402

HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}

RULES = {"includeTagPrefixes": ["TikTok LIVE"], "includeTags": ["Accounts"]}

GENERAL_ONLY_TAGS = {
    "Analytics",
    "TikTok General",
    "TikTok Signing",
    "TikTok Captchas",
    "TikTok Users",
    "TikTok Videos",
}


def ref(section, name):
    return {"$ref": f"#/components/{section}/{name}"}


def operation(tags=None, schema=None):
    op = {"responses": {"200": {"description": "ok"}}}
    if tags is not None:
        op["tags"] = tags
    if schema is not None:
        op["responses"]["200"]["content"] = {
            "application/json": {"schema": ref("schemas", schema)}
        }
    return op


def base_spec():
    """LIVE Gifts -> A -> B -> B (self); Accounts; Users -> C."""
    return {
        "openapi": "3.0.0",
        "tags": [
            {"name": "TikTok LIVE Gifts"},
            {"name": "Accounts"},
            {"name": "TikTok Users"},
        ],
        "paths": {
            "/live/gifts": {"get": operation(["TikTok LIVE Gifts"], "A")},
            "/accounts/me": {"get": operation(["Accounts"])},
            "/users/x": {"get": operation(["TikTok Users"], "C")},
        },
        "components": {
            "securitySchemes": {"api_key_header": {"type": "apiKey"}},
            "schemas": {
                "A": {"type": "object", "properties": {"b": ref("schemas", "B")}},
                "B": {"type": "object", "properties": {"next": ref("schemas", "B")}},
                "C": {"type": "object"},
            },
        },
    }


def operations(spec):
    for path, item in spec["paths"].items():
        for method, op in item.items():
            if method in HTTP_METHODS:
                yield path, method, op


def all_refs(node, acc):
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "$ref" and isinstance(value, str):
                acc.add(value)
            else:
                all_refs(value, acc)
    elif isinstance(node, list):
        for value in node:
            all_refs(value, acc)
    return acc


class FilterSpecTests(unittest.TestCase):
    def test_prefix_and_exact_tags_are_kept(self):
        spec = base_spec()
        filter_spec.filter_spec(spec, RULES)
        self.assertEqual(set(spec["paths"]), {"/live/gifts", "/accounts/me"})

    def test_prefix_is_not_substring_match(self):
        spec = base_spec()
        spec["paths"]["/a"] = {"get": operation(["My TikTok LIVE"])}
        spec["paths"]["/b"] = {"get": operation(["TikTok LIVEx"])}
        filter_spec.filter_spec(spec, RULES)
        self.assertNotIn("/a", spec["paths"])
        self.assertIn("/b", spec["paths"])

    def test_untagged_operation_is_dropped(self):
        spec = base_spec()
        spec["paths"]["/no-tags-key"] = {"get": operation()}
        spec["paths"]["/empty-tags"] = {"get": operation([])}
        filter_spec.filter_spec(spec, RULES)
        self.assertNotIn("/no-tags-key", spec["paths"])
        self.assertNotIn("/empty-tags", spec["paths"])

    def test_mixed_path_keeps_only_matching_methods(self):
        spec = base_spec()
        path_parameters = [{"name": "id", "in": "path", "required": True}]
        spec["paths"]["/mixed/{id}"] = {
            "parameters": path_parameters,
            "get": operation(["TikTok LIVE Gifts"]),
            "post": operation(["TikTok Users"]),
        }
        filter_spec.filter_spec(spec, RULES)
        item = spec["paths"]["/mixed/{id}"]
        self.assertIn("get", item)
        self.assertNotIn("post", item)
        self.assertEqual(item["parameters"], path_parameters)

    def test_transitive_and_cyclic_refs_are_kept(self):
        spec = base_spec()
        filter_spec.filter_spec(spec, RULES)
        self.assertEqual(set(spec["components"]["schemas"]), {"A", "B"})

    def test_all_component_sections_are_pruned(self):
        spec = base_spec()
        components = spec["components"]
        components["schemas"].update({"D": {"type": "object"}, "E": {"type": "object"}})
        components["parameters"] = {
            "UsedParam": {"name": "p", "in": "query"},
            "UnusedParam": {"name": "q", "in": "query"},
        }
        components["responses"] = {
            "UsedResp": {
                "description": "used",
                "headers": {"X-Used": ref("headers", "UsedHeader")},
                "content": {
                    "application/json": {
                        "schema": ref("schemas", "D"),
                        "examples": {"one": ref("examples", "UsedExample")},
                    }
                },
            },
            "UnusedResp": {
                "description": "unused",
                "content": {"application/json": {"schema": ref("schemas", "E")}},
            },
        }
        components["requestBodies"] = {
            "UsedBody": {"content": {}},
            "UnusedBody": {"content": {}},
        }
        components["examples"] = {"UsedExample": {"value": 1}, "UnusedExample": {"value": 2}}
        components["headers"] = {
            "UsedHeader": {"schema": {"type": "string"}},
            "UnusedHeader": {"schema": {"type": "string"}},
        }
        spec["paths"]["/accounts/me"]["get"].update(
            {
                "parameters": [ref("parameters", "UsedParam")],
                "requestBody": ref("requestBodies", "UsedBody"),
                "responses": {"200": ref("responses", "UsedResp")},
            }
        )
        security_before = copy.deepcopy(components["securitySchemes"])

        filter_spec.filter_spec(spec, RULES)

        self.assertEqual(set(components["parameters"]), {"UsedParam"})
        self.assertEqual(set(components["responses"]), {"UsedResp"})
        self.assertEqual(set(components["requestBodies"]), {"UsedBody"})
        self.assertEqual(set(components["examples"]), {"UsedExample"})
        self.assertEqual(set(components["headers"]), {"UsedHeader"})
        self.assertEqual(set(components["schemas"]), {"A", "B", "D"})
        self.assertEqual(components["securitySchemes"], security_before)

    def test_top_level_tags_are_pruned(self):
        spec = base_spec()
        filter_spec.filter_spec(spec, RULES)
        self.assertEqual(
            [tag["name"] for tag in spec["tags"]], ["TikTok LIVE Gifts", "Accounts"]
        )

    def test_empty_result_raises(self):
        spec = base_spec()
        rules = {"includeTagPrefixes": ["Nothing Starts Like This"], "includeTags": []}
        with self.assertRaises(ValueError) as caught:
            filter_spec.filter_spec(spec, rules)
        self.assertIn("no operations", str(caught.exception))

    def test_unmatched_include_tag_raises(self):
        spec = base_spec()
        rules = {"includeTagPrefixes": ["TikTok LIVE"], "includeTags": ["Acounts"]}
        with self.assertRaises(ValueError) as caught:
            filter_spec.filter_spec(spec, rules)
        self.assertIn("Acounts", str(caught.exception))

    def test_report_counts(self):
        spec = base_spec()
        spec["paths"]["/untagged"] = {"get": operation()}
        report = filter_spec.filter_spec(spec, RULES)
        self.assertEqual(
            report,
            {
                "kept": {"TikTok LIVE Gifts": 1, "Accounts": 1},
                "dropped": {"TikTok Users": 1, "<none>": 1},
            },
        )

    def test_committed_spec_live_package(self):
        with open(SPEC_PATH, encoding="utf-8") as fh:
            spec = json.load(fh)
        with open(PACKAGES_PATH, encoding="utf-8") as fh:
            rules = json.load(fh)["live"]

        filter_spec.filter_spec(spec, rules)

        kept = list(operations(spec))
        self.assertEqual(len(kept), 69)
        tags = {op["tags"][0] for _, _, op in kept}
        self.assertEqual(len(tags), 13)
        self.assertEqual(tags & GENERAL_ONLY_TAGS, set())

        for target in all_refs(spec, set()):
            self.assertTrue(target.startswith("#/components/"), target)
            _, _, section, name = target.split("/", 3)
            self.assertIn(name, spec["components"][section], target)


class FilterSpecCliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.spec_copy = os.path.join(self.tmp, "openapi.json")
        shutil.copy(SPEC_PATH, self.spec_copy)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_cli(self, package):
        return subprocess.run(
            [sys.executable, SCRIPT, self.spec_copy, PACKAGES_PATH, package],
            capture_output=True,
            text=True,
        )

    def test_cli_rewrites_file_in_place(self):
        result = self.run_cli("live")
        self.assertEqual(result.returncode, 0, result.stderr)
        with open(self.spec_copy, encoding="utf-8") as fh:
            spec = json.load(fh)
        self.assertEqual(len(list(operations(spec))), 69)
        self.assertIn("kept", result.stdout)
        self.assertIn("dropped", result.stdout)
        self.assertIn("TikTok LIVE Gifts", result.stdout)
        self.assertIn("TikTok Users", result.stdout)

    def test_cli_unknown_package_fails(self):
        result = self.run_cli("nope")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("nope", result.stderr)


if __name__ == "__main__":
    unittest.main()
