#!/usr/bin/env python3
"""Validate local links and essential metadata for the GitHub Pages portfolio."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = (Path("index.html"), Path("portfolio-review.html"))
REQUIRED_FILES = (
    Path("favicon.svg"),
    Path("robots.txt"),
    Path("sitemap.xml"),
    Path("assets/social-preview.png"),
)
REMOTE_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


@dataclass(frozen=True)
class SiteReport:
    errors: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.errors


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[str] = []
        self.meta_names: set[str] = set()
        self.meta_properties: set[str] = set()
        self.canonical_links: list[str] = []
        self.has_json_ld = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): value for key, value in attrs if value is not None}
        if tag in {"a", "link"} and "href" in values:
            self.references.append(values["href"])
        if tag in {"img", "script", "source"} and "src" in values:
            self.references.append(values["src"])
        if tag == "meta":
            if "name" in values:
                self.meta_names.add(values["name"].lower())
            if "property" in values:
                self.meta_properties.add(values["property"].lower())
        if tag == "link" and values.get("rel", "").lower() == "canonical":
            if "href" in values:
                self.canonical_links.append(values["href"])
        if tag == "script" and values.get("type", "").lower() == "application/ld+json":
            self.has_json_ld = True


def _local_target(root: Path, page: Path, reference: str) -> Path | None:
    parts = urlsplit(reference.strip())
    if parts.scheme.lower() in REMOTE_SCHEMES or parts.netloc:
        return None
    if not parts.path:
        return None

    decoded = unquote(parts.path)
    if decoded.startswith("/"):
        target = root / decoded.lstrip("/")
    else:
        target = root / page.parent / decoded
    if decoded.endswith("/"):
        target /= "index.html"
    return target.resolve()


def validate_site(root: Path = ROOT) -> SiteReport:
    errors: list[str] = []
    root_resolved = root.resolve()

    for required in REQUIRED_FILES:
        path = root / required
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing required site file: {required.as_posix()}")

    for page in PAGES:
        page_path = root / page
        if not page_path.is_file():
            errors.append(f"missing page: {page.as_posix()}")
            continue

        parser = ReferenceParser()
        parser.feed(page_path.read_text(encoding="utf-8"))

        for reference in parser.references:
            target = _local_target(root, page, reference)
            if target is None:
                continue
            try:
                target.relative_to(root_resolved)
            except ValueError:
                errors.append(f"{page.as_posix()}: reference escapes repository: {reference}")
                continue
            if not target.is_file():
                errors.append(f"{page.as_posix()}: missing local target: {reference}")

        if page == Path("index.html"):
            required_meta_names = {"description", "viewport", "twitter:card"}
            required_meta_properties = {"og:title", "og:description", "og:image", "og:url"}
            for name in sorted(required_meta_names - parser.meta_names):
                errors.append(f"index.html: missing meta name={name!r}")
            for prop in sorted(required_meta_properties - parser.meta_properties):
                errors.append(f"index.html: missing meta property={prop!r}")
            if not parser.canonical_links:
                errors.append("index.html: missing canonical link")
            if not parser.has_json_ld:
                errors.append("index.html: missing JSON-LD structured data")

    sitemap = root / "sitemap.xml"
    if sitemap.is_file():
        sitemap_text = sitemap.read_text(encoding="utf-8")
        for url in (
            "https://lay007.github.io/",
            "https://lay007.github.io/portfolio-review.html",
        ):
            if url not in sitemap_text:
                errors.append(f"sitemap.xml: missing URL {url}")

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
