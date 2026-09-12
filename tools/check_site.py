#!/usr/bin/env python3
"""Validate links, metadata and sitemap coverage for the GitHub Pages portfolio."""

from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://lay007.github.io/"
REQUIRED_FILES = (
    Path("favicon.svg"),
    Path("robots.txt"),
    Path("sitemap.xml"),
    Path("assets/social-preview.png"),
)
REMOTE_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}
SOCIAL_META_PROPERTIES = ("og:title", "og:description", "og:image", "og:url")
URL_META_KEYS = ("og:image", "og:url", "twitter:image")
SITEMAP_LOC = "{http://www.sitemaps.org/schemas/sitemap/0.9}loc"


@dataclass(frozen=True)
class SiteReport:
    errors: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.errors


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lang: str | None = None
        self.title = ""
        self.references: list[str] = []
        self.ids: set[str] = set()
        self.meta: dict[str, str] = {}
        self.canonical_links: list[str] = []
        self.json_ld_blocks: list[str] = []
        self.images_without_alt: list[str] = []
        self.unsafe_blank_links: list[str] = []
        self._in_title = False
        self._json_ld: list[str] | None = None

    @property
    def noindex(self) -> bool:
        return "noindex" in self.meta.get("robots", "").lower()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        names = {key.lower() for key, _ in attrs}
        values = {key.lower(): value for key, value in attrs if value is not None}

        if "id" in values:
            self.ids.add(values["id"])
        if tag == "html":
            self.lang = values.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = values.get("name") or values.get("property")
            if key:
                self.meta[key.lower()] = values.get("content", "")
        elif tag == "script" and values.get("type", "").lower() == "application/ld+json":
            self._json_ld = []

        if tag in {"a", "link"} and "href" in values:
            self.references.append(values["href"])
        if tag in {"img", "script", "source"} and "src" in values:
            self.references.append(values["src"])
        if tag in {"img", "source"} and "srcset" in values:
            self.references.extend(_srcset_urls(values["srcset"]))
        if tag == "link" and "canonical" in values.get("rel", "").lower().split():
            if "href" in values:
                self.canonical_links.append(values["href"])
        if tag == "img" and "alt" not in names:
            self.images_without_alt.append(values.get("src", "<img>"))
        if tag == "a" and values.get("target") == "_blank":
            if "noopener" not in values.get("rel", "").lower().split():
                self.unsafe_blank_links.append(values.get("href", "<a>"))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._json_ld is not None:
            self.json_ld_blocks.append("".join(self._json_ld))
            self._json_ld = None

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data
        if self._json_ld is not None:
            self._json_ld.append(data)


def _srcset_urls(srcset: str) -> list[str]:
    return [candidate.split()[0] for candidate in srcset.split(",") if candidate.strip()]


def _page_url(page: Path) -> str:
    path = page.as_posix()
    return SITE_URL if path == "index.html" else SITE_URL + path


def _resolve(root: Path, page: Path, reference: str) -> tuple[Path | None, str]:
    """Map a reference to a repository file plus fragment; None means it is not local."""
    reference = reference.strip()
    if reference.startswith(SITE_URL):
        reference = "/" + reference[len(SITE_URL):]
    parts = urlsplit(reference)
    if parts.scheme.lower() in REMOTE_SCHEMES or parts.netloc:
        return None, ""

    decoded = unquote(parts.path)
    if not decoded:
        target = root / page
    else:
        base = root if decoded.startswith("/") else root / page.parent
        target = base / decoded.lstrip("/")
        if decoded.endswith("/"):
            target /= "index.html"
    return target.resolve(), parts.fragment


def _page_problems(
    root: Path, page: Path, parser: PageParser, parsed: dict[Path, PageParser]
) -> list[str]:
    problems: list[str] = []
    if not parser.lang:
        problems.append("missing <html lang>")
    if not parser.title.strip():
        problems.append("missing <title>")
    for name in ("description", "viewport"):
        if not parser.meta.get(name):
            problems.append(f"missing meta name={name!r}")

    references = list(parser.references)
    references.extend(parser.meta[key] for key in URL_META_KEYS if parser.meta.get(key))
    for reference in references:
        target, fragment = _resolve(root, page, reference)
        if target is None:
            continue
        if not target.is_relative_to(root):
            problems.append(f"reference escapes repository: {reference}")
            continue
        if not target.is_file():
            problems.append(f"missing local target: {reference}")
            continue
        target_parser = parsed.get(target.relative_to(root))
        if fragment and target_parser is not None and fragment not in target_parser.ids:
            problems.append(f"missing anchor: {reference}")

    for block in parser.json_ld_blocks:
        try:
            json.loads(block)
        except json.JSONDecodeError as error:
            problems.append(f"invalid JSON-LD: {error}")
    problems.extend(f"image without alt attribute: {src}" for src in parser.images_without_alt)
    problems.extend(
        f'target="_blank" link without rel="noopener": {href}'
        for href in parser.unsafe_blank_links
    )

    if parser.noindex:
        return problems

    expected_url = _page_url(page)
    if parser.canonical_links != [expected_url]:
        problems.append(f"canonical link must be exactly {expected_url}")
    for prop in SOCIAL_META_PROPERTIES:
        if not parser.meta.get(prop):
            problems.append(f"missing meta property={prop!r}")
    if parser.meta.get("og:url") and parser.meta["og:url"] != expected_url:
        problems.append(f"og:url must match canonical URL {expected_url}")
    if not parser.meta.get("twitter:card"):
        problems.append("missing meta name='twitter:card'")
    if page == Path("index.html") and not parser.json_ld_blocks:
        problems.append("missing JSON-LD structured data")
    return problems


def _sitemap_problems(root: Path, parsed: dict[Path, PageParser]) -> list[str]:
    sitemap = root / "sitemap.xml"
    if not sitemap.is_file():
        return []
    try:
        tree = ET.parse(sitemap)
    except ET.ParseError as error:
        return [f"sitemap.xml: invalid XML: {error}"]

    locs = [(element.text or "").strip() for element in tree.iter(SITEMAP_LOC)]
    problems: list[str] = []
    for loc in locs:
        target, _ = _resolve(root, Path("index.html"), loc)
        if not loc.startswith(SITE_URL) or target is None:
            problems.append(f"sitemap.xml: URL outside site: {loc}")
        elif not target.is_file():
            problems.append(f"sitemap.xml: URL has no page: {loc}")
        elif (page := parsed.get(target.relative_to(root))) is not None and page.noindex:
            problems.append(f"sitemap.xml: lists noindex page: {loc}")
    for duplicate in sorted({loc for loc in locs if locs.count(loc) > 1}):
        problems.append(f"sitemap.xml: duplicate URL {duplicate}")
    for page, parser in parsed.items():
        if not parser.noindex and _page_url(page) not in locs:
            problems.append(f"sitemap.xml: missing URL {_page_url(page)}")
    return problems


def _robots_problems(root: Path) -> list[str]:
    robots = root / "robots.txt"
    directive = f"Sitemap: {SITE_URL}sitemap.xml"
    if robots.is_file() and directive not in robots.read_text(encoding="utf-8"):
        return [f"robots.txt: missing {directive!r}"]
    return []


def validate_site(root: Path = ROOT) -> SiteReport:
    errors: list[str] = []
    root = root.resolve()

    for required in REQUIRED_FILES:
        path = root / required
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing required site file: {required.as_posix()}")

    parsed: dict[Path, PageParser] = {}
    for path in sorted(root.glob("*.html")):
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
        parsed[path.relative_to(root)] = parser
    if Path("index.html") not in parsed:
        errors.append("missing page: index.html")

    for page, parser in parsed.items():
        errors.extend(
            f"{page.as_posix()}: {problem}"
            for problem in _page_problems(root, page, parser, parsed)
        )
    errors.extend(_sitemap_problems(root, parsed))
    errors.extend(_robots_problems(root))
    return SiteReport(tuple(errors))


def main() -> int:
    report = validate_site()
    if report.ok:
        print("Static site validation passed.")
        return 0

    print("Static site validation failed:")
    for error in report.errors:
        print(f"  - {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
