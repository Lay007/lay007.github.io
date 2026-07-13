from __future__ import annotations

import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from check_site import validate_site  # noqa: E402


INDEX = """<!doctype html>
<html><head>
<meta name="description" content="Portfolio">
<meta name="viewport" content="width=device-width">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:title" content="Portfolio">
<meta property="og:description" content="Engineering portfolio">
<meta property="og:image" content="https://example.invalid/preview.png">
<meta property="og:url" content="https://lay007.github.io/">
<link rel="canonical" href="https://lay007.github.io/">
<link rel="icon" href="/favicon.svg">
<script type="application/ld+json">{"@type":"Person"}</script>
</head><body><a href="portfolio-review.html">Review</a></body></html>
"""

REVIEW = """<!doctype html>
<html><body><a href="index.html#work">Home</a><img src="assets/social-preview.png"></body></html>
"""


def _make_site(root: Path) -> None:
    (root / "assets").mkdir(parents=True)
    (root / "index.html").write_text(INDEX, encoding="utf-8")
    (root / "portfolio-review.html").write_text(REVIEW, encoding="utf-8")
    (root / "favicon.svg").write_text("<svg/>", encoding="utf-8")
    (root / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
    (root / "sitemap.xml").write_text(
        "https://lay007.github.io/\nhttps://lay007.github.io/portfolio-review.html\n",
        encoding="utf-8",
    )
    (root / "assets" / "social-preview.png").write_bytes(b"PNG")


class SiteValidatorTests(unittest.TestCase):
    def test_accepts_complete_site(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            _make_site(root)

            report = validate_site(root)

            self.assertTrue(report.ok, report.errors)

    def test_rejects_missing_local_asset(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            _make_site(root)
            (root / "portfolio-review.html").write_text(
                REVIEW + '<img src="assets/missing.png">', encoding="utf-8"
            )

            report = validate_site(root)

            self.assertTrue(any("missing local target" in error for error in report.errors))

    def test_rejects_missing_social_metadata(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            _make_site(root)
            (root / "index.html").write_text(
                INDEX.replace('<meta property="og:title" content="Portfolio">', ""),
                encoding="utf-8",
            )

            report = validate_site(root)

            self.assertTrue(any("og:title" in error for error in report.errors))

    def test_rejects_incomplete_sitemap(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            _make_site(root)
            (root / "sitemap.xml").write_text(
                "https://lay007.github.io/\n", encoding="utf-8"
            )

            report = validate_site(root)

            self.assertTrue(any("portfolio-review.html" in error for error in report.errors))


if __name__ == "__main__":
    unittest.main()
