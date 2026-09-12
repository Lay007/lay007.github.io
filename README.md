# lay007.github.io

[![Site check](https://github.com/Lay007/lay007.github.io/actions/workflows/site-check.yml/badge.svg)](https://github.com/Lay007/lay007.github.io/actions/workflows/site-check.yml)

Personal engineering website and portfolio for **Alexander / Lay007**.

- Live site: [lay007.github.io](https://lay007.github.io/)
- Fast reviewer path: [10-minute engineering portfolio review](https://lay007.github.io/portfolio-review.html)

---

## What the site covers

- **digital signal processing (DSP)**
- **FPGA-oriented engineering**
- **SDR, communications and telemetry systems**
- **circuit design and applied electronics**
- **engineering software and technical R&D**

The site is evidence-oriented: every project card names the repository documents a reviewer should open first, and the review page states current limits next to the results.

---

## Pages

| Page | Purpose |
|---|---|
| `index.html` | Main portfolio: positioning, engineering pipeline, expertise, selected projects, background, toolchain and contacts |
| `portfolio-review.html` | 10-minute reviewer path: what to open first in each repository, evidence links and current limits |
| `404.html` | GitHub Pages not-found page (not indexed) |

---

## Selected projects featured on the site

- [`zynq-sdr-course`](https://github.com/Lay007/zynq-sdr-course) — bilingual SDR course from DSP models to Zynq RF measurements;
- [`zynq-lora-phy-positioning`](https://github.com/Lay007/zynq-lora-phy-positioning) — LoRa PHY, generated HDL, and ToA/TDoA positioning;
- [`cpp-dsp-showcase`](https://github.com/Lay007/cpp-dsp-showcase) — C++17 DSP kernels with deterministic tests and benchmarks;
- [`network-quality-assessment`](https://github.com/Lay007/network-quality-assessment) — network SLA measurement with FPGA timestamping concepts;
- [`script-toolbox`](https://github.com/Lay007/script-toolbox) — Windows/SSH/Git automation with PowerShell quality gates.

Only public repositories are linked. `optical-demodulator` is still private and is described in [docs/projects.md](docs/projects.md) without a link.

---

## Technology

The site is intentionally simple and dependable:

- plain HTML pages with one shared stylesheet, `assets/css/site.css`;
- minimal JavaScript (footer year only);
- Open Graph and Twitter card metadata, JSON-LD structured data;
- `robots.txt`, `sitemap.xml` and a custom `404.html`;
- no framework and no build step: GitHub Pages serves the repository as is (`.nojekyll`).

---

## Repository structure

```text
lay007.github.io/
|- index.html                          main portfolio page
|- portfolio-review.html               10-minute reviewer path
|- 404.html                            not-found page
|- favicon.svg                         L7 / signal-wave favicon
|- robots.txt
|- sitemap.xml
|- assets/
|  |- css/site.css                     shared styles
|  |- engineering_pipeline.svg         pipeline diagram (desktop)
|  |- engineering_pipeline_mobile.svg  pipeline diagram (phones)
|  |- projects/                        project cover images
|  |- social-preview.png               Open Graph image (rendered)
|  `- apple-touch-icon.png             touch icon (rendered)
|- docs/
|  |- content-update-checklist.md
|  |- engineering-proof.md
|  |- projects.md
|  `- research.md
|- tools/
|  |- check_site.py                    static site validator
|  |- render_assets.py                 renders PNG assets with headless Chromium
|  `- social-preview.html              source of social-preview.png
|- tests/
|  `- test_site_validator.py
`- .github/workflows/
   |- site-check.yml                   validator and tests on push and pull request
   `- link-check.yml                   weekly external link check (lychee)
```

---

## Local preview

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
http://localhost:8000/portfolio-review.html
```

`index.html` and `portfolio-review.html` also work when opened directly from disk; `404.html` uses root-relative paths and needs the server.

---

## Validation

```bash
python -m unittest discover -s tests -p "test_site_validator.py" -v
python tools/check_site.py
```

The validator checks every HTML page in the repository root for:

- local links, images, `srcset` sources and `#anchor` targets;
- own-domain absolute URLs (canonical, `og:image`) mapped to repository files;
- `lang`, title, description, canonical and social metadata on indexable pages;
- valid JSON-LD, `alt` attributes on images, `rel="noopener"` on `target="_blank"` links;
- sitemap coverage (every indexable page listed, no missing or `noindex` pages) and the `robots.txt` sitemap directive.

External links are checked weekly by `link-check.yml`; the workflow can also be started manually from the Actions tab.

---

## Rendered assets

`assets/social-preview.png` and `assets/apple-touch-icon.png` are generated from `tools/social-preview.html` and `favicon.svg`:

```bash
python -m pip install pillow
python tools/render_assets.py
```

The script needs Microsoft Edge, Google Chrome or Chromium. Set `CHROME_PATH` if the browser is not found.

---

## Editing workflow

1. Review [docs/content-update-checklist.md](docs/content-update-checklist.md).
2. Edit the page and, if needed, `assets/css/site.css`.
3. Run the validation commands.
4. Update `lastmod` in `sitemap.xml` for changed pages.
5. Commit, push to `main`, and wait for GitHub Pages to publish the update.

---

## Documentation

- [Projects and proof assets](docs/projects.md)
- [Engineering proof matrix and site status](docs/engineering-proof.md)
- [Research focus](docs/research.md)
- [Content update checklist](docs/content-update-checklist.md)

---

## Content and tone

Keep the site concise, technical and evidence-oriented. The best pages should help a reviewer quickly answer: what was built, how it was verified, what is measured, and what is still only a roadmap.
