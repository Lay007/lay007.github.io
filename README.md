# lay007.github.io

Personal engineering website and portfolio for **Alexander / Lay007**.

This repository contains the source of the public GitHub Pages site used as a concise professional landing page for work related to:

- **digital signal processing (DSP)**
- **FPGA-oriented engineering**
- **communications and telemetry systems**
- **circuit design and applied electronics**
- **engineering software and technical R&D**

Live site: [lay007.github.io](https://lay007.github.io/)

Fast review page: [10-minute engineering portfolio review](https://lay007.github.io/portfolio-review.html)

---

## Overview

The website is designed as a clean, professional portfolio that presents:

- core engineering positioning;
- technical expertise and domains of work;
- selected GitHub projects;
- a fast 10-minute reviewer path;
- academic and applied background;
- contact points for collaboration and professional communication.

The current visual direction is intentionally restrained and technical: modern dark UI, strong first-screen positioning, clear project presentation, and a more premium engineering tone rather than a generic personal homepage.

---

## What this repository is for

This repository is the source for my **GitHub Pages business card / portfolio website**.

Its purpose is to:

- present my engineering profile in a clear public format;
- provide a single landing page for GitHub visitors;
- provide a fast reviewer page for technical screening;
- highlight practical areas of expertise;
- connect visitors to selected repositories and contact channels;
- keep the site lightweight, fast, and easy to maintain.

---

## Main sections of the site

The website currently includes sections such as:

- **Hero / intro** — primary positioning and short engineering summary;
- **Core expertise** — DSP, FPGA, communications, secure engineering, circuit design;
- **Selected projects** — representative repositories;
- **Portfolio review page** — fast route through proof artifacts;
- **Background** — degree, teaching, publications, inventions and patents;
- **Toolchain & platforms** — major languages, tools, and vendor ecosystems;
- **Contact** — GitHub, website, Telegram.

---

## Selected projects featured on the site

The portfolio currently highlights repositories such as:

- [`zynq-sdr-course`](https://github.com/Lay007/zynq-sdr-course) — bilingual SDR course from theory to implementation;
- [`zynq-lora-phy-positioning`](https://github.com/Lay007/zynq-lora-phy-positioning) — LoRa PHY, generated HDL, and ToA/TDoA positioning;
- [`network-quality-assessment`](https://github.com/Lay007/network-quality-assessment) — network performance testing with FPGA-based timing concepts;
- [`script-toolbox`](https://github.com/Lay007/script-toolbox) — practical Windows/SSH/Git automation scripts;
- [`cpp-dsp-showcase`](https://github.com/Lay007/cpp-dsp-showcase) — C++-focused DSP showcase and compact implementation examples.

---

## Technology

The site is intentionally simple and dependable.

Current approach:

- **plain HTML**;
- **embedded CSS**;
- minimal JavaScript;
- Open Graph and Twitter card metadata;
- JSON-LD structured data;
- static `robots.txt` and `sitemap.xml`;
- no heavy frontend framework;
- suitable for direct GitHub Pages hosting.

This keeps the website:

- easy to edit;
- easy to publish;
- easy to clone and preview locally;
- independent from external build tooling.

---

## Browser icon

The site includes a small branded SVG favicon:

```text
favicon.svg
```

The icon uses a compact `L7` / signal-wave / FPGA-grid motif so it remains readable at small browser-tab sizes while matching the dark technical visual style of the landing page.

---

## Repository structure

Typical structure is intentionally minimal:

```text
lay007.github.io/
|- assets/
|  `- social-preview.png
|- favicon.svg
|- index.html
|- portfolio-review.html
|- content-update-checklist.md
|- robots.txt
|- sitemap.xml
`- README.md
```

If the site grows later, the repository can be expanded with:

```text
lay007.github.io/
├─ index.html
├─ portfolio-review.html
├─ favicon.svg
├─ assets/
│  ├─ css/
│  ├─ js/
│  └─ img/
├─ docs/
└─ README.md
```

---

## Local preview

Because the site is static, local preview is straightforward.

### Option 1 — open directly

Open `index.html` or `portfolio-review.html` in a browser.

### Option 2 — run a lightweight local server

Using Python:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
http://localhost:8000/portfolio-review.html
```

---

## Editing workflow

Typical update flow:

1. Review [content-update-checklist.md](content-update-checklist.md)
2. Edit `index.html` or `portfolio-review.html`
3. Refresh local preview
4. Commit changes
5. Push to `main`
6. Wait for GitHub Pages to publish the update

Example:

```bash
git add index.html portfolio-review.html assets/social-preview.png robots.txt sitemap.xml README.md content-update-checklist.md
git commit -m "Update portfolio site"
git push origin main
```

---

## Content and tone

Keep the site concise, technical and evidence-oriented. The best pages should help a reviewer quickly answer: what was built, how it was verified, what is measured, and what is still only a roadmap.
