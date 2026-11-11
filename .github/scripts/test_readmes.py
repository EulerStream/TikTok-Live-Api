"""Guard the READMEs of the split TypeScript and Python SDKs.

Each language publishes two packages, one with only TikTok LIVE and one with
everything: tiktok-live-api-sdk and tiktok-api-sdk on npm, TikTokLiveApiSdk and
TikTokApiSdk on PyPI. Their READMEs are what the registries show,
so each must name its own package, show its own client, avoid the deprecated
names in examples, and, for the LIVE package, never show a call that the
package no longer contains.

The Python READMEs are Jinja templates rendered by the generator; the two
placeholders they use are filled in from the package's sdk.json before
checking.

Run with: python3 -m unittest discover -s .github/scripts -p 'test_readmes.py' -v
"""

import json
import os
import re
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))

UNOFFICIAL = (
    "Unofficial: this project is not affiliated with, endorsed by, or connected to "
    "TikTok or ByteDance."
)

# Calls and client groups that exist only in the full package, plus the gift
# catalog, which needs a paid plan and so must not lead a quick start.
NOT_IN_LIVE = [
    "tikTokUsers",
    "tik_tok_users",
    "tikTokVideos",
    "client.signing",
    "client.captchas",
    "client.general",
    "client.analytics",
    "listWebcastGifts",
    "list_webcast_gifts",
]

DEPRECATED_IN_CODE = ["EulerStreamApiClient", "import EulerApiSdk", "from EulerApiSdk"]

READMES = {
    "typescript-live": {
        "path": "sdk/typescript/live/README.md",
        "live": True,
        "heading": "# TikTok LIVE API SDK for Node.js & TypeScript",
        "install": "npm install tiktok-live-api-sdk",
        "client": "TikTokLiveApiSdk",
        "other_package": "tiktok-api-sdk",
        "migration_heading": "## Migrating from 0.x",
    },
    "typescript-api": {
        "path": "sdk/typescript/api/README.md",
        "live": False,
        "heading": "# TikTok API SDK for Node.js & TypeScript",
        "install": "npm install tiktok-api-sdk",
        "client": "TikTokApiSdk",
        "other_package": "tiktok-live-api-sdk",
        "migration_heading": "## Migrating",
    },
    "python-live": {
        "path": "sdk/python/live/templates/README.md.jinja",
        "sdk_json": "sdk/python/live/sdk.json",
        "live": True,
        "heading": "# TikTok LIVE API SDK for Python",
        "install": "pip install TikTokLiveApiSdk",
        "client": "TikTokLiveApiSdk",
        "other_package": "TikTokApiSdk",
        "migration_heading": "## Migrating from EulerApiSdk",
    },
    "python-api": {
        "path": "sdk/python/api/templates/README.md.jinja",
        "sdk_json": "sdk/python/api/sdk.json",
        "live": False,
        "heading": "# TikTok API SDK for Python",
        "install": "pip install TikTokApiSdk",
        "client": "TikTokApiSdk",
        "other_package": "TikTokLiveApiSdk",
        "migration_heading": "## Migrating",
    },
}

# READMEs that link to the TypeScript and Python packages from elsewhere.
CROSS_LINKING = [
    "README.md",
    "sdk/csharp/README.md",
    "sdk/java/README.md",
    "sdk/go/README.md",
]


def read(relative_path):
    with open(os.path.join(REPO, relative_path), encoding="utf-8") as fh:
        return fh.read()


def load(spec):
    """The README text, with the Jinja placeholders of a Python template filled in."""
    text = read(spec["path"])
    if "sdk_json" in spec:
        sdk = json.loads(read(spec["sdk_json"]))
        text = text.replace("{{ project_name }}", sdk["projectName"])
        text = text.replace("{{ package_name }}", sdk["packageName"])
    return text


def code_blocks(text):
    """The contents of every triple-backtick fence, joined."""
    return "\n".join(re.findall(r"```[^\n]*\n(.*?)```", text, flags=re.DOTALL))


class ReadmeTests(unittest.TestCase):
    def check_each(self, check):
        """Run check(spec, text) against every README, each as its own sub-test."""
        for name, spec in READMES.items():
            with self.subTest(readme=name):
                check(spec, load(spec))

    def test_no_unrendered_placeholders(self):
        self.check_each(lambda spec, text: self.assertNotIn("{{", text))

    def test_unofficial_line(self):
        self.check_each(lambda spec, text: self.assertIn(UNOFFICIAL, text))

    def test_first_heading(self):
        def check(spec, text):
            headings = [line for line in text.splitlines() if line.startswith("# ")]
            self.assertEqual(headings[0], spec["heading"])

        self.check_each(check)

    def test_install_line(self):
        self.check_each(lambda spec, text: self.assertIn(spec["install"], code_blocks(text)))

    def test_examples_use_the_current_name(self):
        self.check_each(lambda spec, text: self.assertIn(spec["client"], code_blocks(text)))

    def test_examples_avoid_deprecated_names(self):
        def check(spec, text):
            code = code_blocks(text)
            for deprecated in DEPRECATED_IN_CODE:
                self.assertNotIn(deprecated, code)

        self.check_each(check)

    def test_live_readmes_show_nothing_the_live_package_lacks(self):
        def check(spec, text):
            if not spec["live"]:
                return
            for missing in NOT_IN_LIVE:
                self.assertNotIn(missing, text)

        self.check_each(check)

    def test_mentions_the_other_package(self):
        self.check_each(lambda spec, text: self.assertIn(spec["other_package"], text))

    def test_migration_section(self):
        self.check_each(
            lambda spec, text: self.assertIn(spec["migration_heading"], text.splitlines())
        )


class CrossLinkTests(unittest.TestCase):
    def test_no_links_to_the_retired_python_package(self):
        for path in CROSS_LINKING:
            with self.subTest(readme=path):
                text = read(path)
                self.assertNotIn("pypi.org/project/EulerApiSdk", text)
                self.assertNotIn("pip install EulerApiSdk", text)

    def test_both_packages_are_listed(self):
        for path in CROSS_LINKING:
            with self.subTest(readme=path):
                text = read(path)
                for url in (
                    "npmjs.com/package/tiktok-api-sdk",
                    "npmjs.com/package/tiktok-live-api-sdk",
                    "pypi.org/project/TikTokApiSdk",
                    "pypi.org/project/TikTokLiveApiSdk",
                ):
                    self.assertIn(url, text)


if __name__ == "__main__":
    unittest.main()
