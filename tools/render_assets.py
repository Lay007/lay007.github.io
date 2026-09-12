#!/usr/bin/env python3
"""Render raster site assets with a headless Chromium-based browser.

Outputs:
  assets/social-preview.png   from tools/social-preview.html (1200x630)
  assets/apple-touch-icon.png from favicon.svg (180x180)

Requirements: Microsoft Edge, Google Chrome or Chromium (or CHROME_PATH), and Pillow:
  python -m pip install pillow
  python tools/render_assets.py
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover - depends on the local environment
    raise SystemExit("Pillow is required: python -m pip install pillow")

ROOT = Path(__file__).resolve().parents[1]
BROWSER_CANDIDATES = (
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome",
    "chromium",
    "chromium-browser",
    "microsoft-edge",
)
# Headless Chromium enforces a minimum window width, so small assets are
# rendered on a larger canvas and downsampled.
TOUCH_ICON_CANVAS = 720


def find_browser() -> str:
    configured = os.environ.get("CHROME_PATH")
    for candidate in (configured,) if configured else BROWSER_CANDIDATES:
        if Path(candidate).is_file():
            return candidate
        if found := shutil.which(candidate):
            return found
    raise SystemExit("No Chromium-based browser found; set CHROME_PATH.")


def render(
    browser: str,
    url: str,
    window: tuple[int, int],
    output: Path,
    size: tuple[int, int],
    scale: int = 1,
) -> None:
    with tempfile.TemporaryDirectory() as directory:
        raw = Path(directory) / "raw.png"
        subprocess.run(
            [
                browser,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--no-first-run",
                f"--user-data-dir={Path(directory) / 'profile'}",
                f"--force-device-scale-factor={scale}",
                f"--window-size={window[0]},{window[1]}",
                "--virtual-time-budget=2000",
                f"--screenshot={raw}",
                url,
            ],
            check=True,
            capture_output=True,
            timeout=120,
        )
        with Image.open(raw) as image:
            expected = (window[0] * scale, window[1] * scale)
            if image.size != expected:
                raise SystemExit(f"{output.name}: browser produced {image.size}, expected {expected}")
            image.convert("RGB").resize(size, Image.LANCZOS).save(output, optimize=True)
    print(f"wrote {output.relative_to(ROOT).as_posix()} {size[0]}x{size[1]}")


def main() -> int:
    browser = find_browser()
    render(
        browser,
        (ROOT / "tools" / "social-preview.html").as_uri(),
        window=(1200, 630),
        output=ROOT / "assets" / "social-preview.png",
        size=(1200, 630),
        scale=2,
    )

    with tempfile.TemporaryDirectory() as directory:
        page = Path(directory) / "touch-icon.html"
        page.write_text(
            '<html><body style="margin:0;background:#08111f">'
            f'<img src="{(ROOT / "favicon.svg").as_uri()}" '
            f'style="display:block;width:{TOUCH_ICON_CANVAS}px;height:{TOUCH_ICON_CANVAS}px">'
            "</body></html>",
            encoding="utf-8",
        )
        render(
            browser,
            page.as_uri(),
            window=(TOUCH_ICON_CANVAS, TOUCH_ICON_CANVAS),
            output=ROOT / "assets" / "apple-touch-icon.png",
            size=(180, 180),
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
