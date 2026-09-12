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
<html lang="en"><head>
<title>Portfolio</title>
<meta name="description" content="Portfolio">
<meta name="viewport" content="width=device-width">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:title" content="Portfolio">
<meta property="og:description" content="Engineering portfolio">
<meta property="og:image" content="https://lay007.github.io/assets/social-preview.png">
<meta property="og:url" content="https://lay007.github.io/">
<link rel="canonical" href="https://lay007.github.io/">
<link rel="icon" href="/favicon.svg">
<script type="application/ld+json">{"@type":"Person"}</script>
</head><body id="top">
<a href="portfolio-review.html#steps">Review</a>
<a href="https://github.com/Lay007" target="_blank" rel="noopener noreferrer">GitHub</a>
<img src="assets/social-preview.png" alt="">
</body></html>
"""

REVIEW = """<!doctype html>
<html lang="en"><head>
<title>Review</title>
<meta name="description" content="Review path">
<meta name="viewport" content="width=device-width">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:title" content="Review">
<meta property="og:description" content="Review path">
<meta property="og:image" content="https://lay007.github.io/assets/social-preview.png">
<meta property="og:url" content="https://lay007.github.io/portfolio-review.html">
<link rel="canonical" href="https://lay007.github.io/portfolio-review.html">
</head><body><section id="steps"><a href="index.html#top">Home</a></section></body></html>
"""

NOT_FOUND = """<!doctype html>
<html lang="en"><head>
<title>Not found</title>
<meta name="description" content="Page not found">
<meta name="viewport" content="width=device-width">
<meta name="robots" content="noindex">
</head><body><a href="/">Home</a></body></html>
"""

SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://lay007.github.io/</loc></url>
  <url><loc>https://lay007.github.io/portfolio-review.html</loc></url>
</urlset>
"""

ROBOTS = "User-agent: *\nAllow: /\n\nSitemap: https://lay007.github.io/sitemap.xml\n"


def _make_site(root: Path, overrides: dict[str, str]) -> None:
    files = {
        "index.html": INDEX,
        "portfolio-review.html": REVIEW,
        "404.html": NOT_FOUND,
        "favicon.svg": "<svg/>",
        "robots.txt": ROBOTS,
        "sitemap.xml": SITEMAP,
        **overrides,
    }
    for name, content in files.items():
        (root / name).write_text(content, encoding="utf-8")
    (root / "assets").mkdir()
    (root / "assets" / "social-preview.png").write_bytes(b"PNG")


class SiteValidatorTests(unittest.TestCase):
    def errors_for(self, overrides: dict[str, str] | None = None) -> tuple[str, ...]:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            _make_site(root, overrides or {})
            return validate_site(root).errors

    def assertError(self, errors: tuple[str, ...], fragment: str) -> None:
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_accepts_complete_site(self) -> None:
        self.assertEqual(self.errors_for(), ())

    def test_rejects_missing_local_asset(self) -> None:
        review = REVIEW.replace("</body>", '<img src="assets/missing.png" alt=""></body>')

        self.assertError(self.errors_for({"portfolio-review.html": review}), "missing local target")

    def test_rejects_missing_social_metadata(self) -> None:
        index = INDEX.replace('<meta property="og:title" content="Portfolio">', "")

        self.assertError(self.errors_for({"index.html": index}), "og:title")

    def test_rejects_page_missing_from_sitemap(self) -> None:
        sitemap = SITEMAP.replace(
            "<url><loc>https://lay007.github.io/portfolio-review.html</loc></url>", ""
        )

        self.assertError(
            self.errors_for({"sitemap.xml": sitemap}),
            "missing URL https://lay007.github.io/portfolio-review.html",
        )

    def test_rejects_sitemap_url_without_page(self) -> None:
        sitemap = SITEMAP.replace(
            "</urlset>", "<url><loc>https://lay007.github.io/research.html</loc></url></urlset>"
        )

        self.assertError(self.errors_for({"sitemap.xml": sitemap}), "URL has no page")

    def test_rejects_noindex_page_in_sitemap(self) -> None:
        sitemap = SITEMAP.replace(
            "</urlset>", "<url><loc>https://lay007.github.io/404.html</loc></url></urlset>"
        )

        self.assertError(self.errors_for({"sitemap.xml": sitemap}), "lists noindex page")

    def test_rejects_broken_anchor(self) -> None:
        index = INDEX.replace("portfolio-review.html#steps", "portfolio-review.html#missing")

        self.assertError(self.errors_for({"index.html": index}), "missing anchor")

    def test_rejects_missing_own_domain_image(self) -> None:
        index = INDEX.replace(
            'content="https://lay007.github.io/assets/social-preview.png"',
            'content="https://lay007.github.io/assets/missing.png"',
        )

        self.assertError(self.errors_for({"index.html": index}), "missing local target")

    def test_rejects_invalid_json_ld(self) -> None:
        index = INDEX.replace('{"@type":"Person"}', '{"@type":')

        self.assertError(self.errors_for({"index.html": index}), "invalid JSON-LD")

    def test_rejects_blank_target_without_noopener(self) -> None:
        index = INDEX.replace(' rel="noopener noreferrer"', "")

        self.assertError(self.errors_for({"index.html": index}), "noopener")

    def test_rejects_image_without_alt(self) -> None:
        index = INDEX.replace(' alt=""', "")

        self.assertError(self.errors_for({"index.html": index}), "without alt")

    def test_rejects_reference_outside_repository(self) -> None:
        review = REVIEW.replace("</body>", '<a href="../secret.txt">Secret</a></body>')

        self.assertError(self.errors_for({"portfolio-review.html": review}), "escapes repository")

    def test_rejects_mismatched_canonical(self) -> None:
        review = REVIEW.replace(
            '<link rel="canonical" href="https://lay007.github.io/portfolio-review.html">',
            '<link rel="canonical" href="https://lay007.github.io/">',
        )

        self.assertError(self.errors_for({"portfolio-review.html": review}), "canonical link")

    def test_rejects_missing_lang(self) -> None:
        review = REVIEW.replace('<html lang="en">', "<html>")

        self.assertError(self.errors_for({"portfolio-review.html": review}), "lang")

    def test_rejects_robots_without_sitemap(self) -> None:
        errors = self.errors_for({"robots.txt": "User-agent: *\nAllow: /\n"})

        self.assertError(errors, "robots.txt")


if __name__ == "__main__":
    unittest.main()
