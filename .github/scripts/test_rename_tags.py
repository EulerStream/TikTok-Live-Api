"""Tests for rename_tags.py.

Run with: python3 -m unittest discover -s .github/scripts -p 'test_rename_tags.py' -v
"""

import json
import os
import unittest

from rename_tags import rename_tags

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))

PYTHON_TAG_NAMES = os.path.join(REPO, "sdk", "python", "common", "tag_names.json")


def spec_with(*tags):
    """A spec with one operation per tag, and a top-level entry for each."""
    return {
        "tags": [{"name": tag, "description": f"About {tag}."} for tag in tags],
        "paths": {
            f"/{index}": {"get": {"operationId": f"Op{index}", "tags": [tag]}}
            for index, tag in enumerate(tags)
        },
    }


def operation_tags(spec):
    return [operation["tags"] for item in spec["paths"].values() for operation in item.values()]


class RenameTagsTests(unittest.TestCase):
    def test_renames_the_tag_on_operations_and_in_the_tag_list(self):
        spec = spec_with("TikTok OAuth", "TikTok Users")

        renamed = rename_tags(spec, {"TikTok OAuth": "TikTok Oauth"})

        self.assertEqual(renamed, 1)
        self.assertEqual(operation_tags(spec), [["TikTok Oauth"], ["TikTok Users"]])
        self.assertEqual([tag["name"] for tag in spec["tags"]], ["TikTok Oauth", "TikTok Users"])
        self.assertEqual(spec["tags"][0]["description"], "About TikTok OAuth.")

    def test_ignores_a_tag_the_spec_does_not_use(self):
        spec = spec_with("TikTok General", "TikTok Users")
        before = json.dumps(spec, sort_keys=True)

        renamed = rename_tags(spec, {"TikTok OAuth": "TikTok Oauth"})

        self.assertEqual(renamed, 0)
        self.assertEqual(json.dumps(spec, sort_keys=True), before)

    def test_two_tags_renamed_to_one_leave_a_single_tag(self):
        spec = spec_with("TikTok General", "TikTok OAuth")
        spec["paths"]["/both"] = {"get": {"operationId": "Both", "tags": ["TikTok General", "TikTok OAuth"]}}

        rename_tags(spec, {"TikTok General": "TikTok Oauth", "TikTok OAuth": "TikTok Oauth"})

        self.assertEqual(operation_tags(spec), [["TikTok Oauth"], ["TikTok Oauth"], ["TikTok Oauth"]])
        self.assertEqual([tag["name"] for tag in spec["tags"]], ["TikTok Oauth"])

    def test_leaves_non_operation_path_keys_alone(self):
        spec = spec_with("TikTok OAuth")
        spec["paths"]["/0"]["parameters"] = [{"name": "id", "in": "query"}]

        rename_tags(spec, {"TikTok OAuth": "TikTok Oauth"})

        self.assertEqual(spec["paths"]["/0"]["parameters"], [{"name": "id", "in": "query"}])


class PythonTagNamesTests(unittest.TestCase):
    def test_the_oauth_tag_is_spelled_so_python_reads_it_as_one_word(self):
        # openapi-python-client names a group by splitting its tag at capitals:
        # "TikTok OAuth" becomes api.tik_tok_o_auth, "TikTok Oauth" api.tik_tok_oauth.
        with open(PYTHON_TAG_NAMES, encoding="utf-8") as fh:
            names = json.load(fh)

        self.assertEqual(names.get("TikTok OAuth"), "TikTok Oauth")


if __name__ == "__main__":
    unittest.main()
