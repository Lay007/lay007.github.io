# lay007.github.io

Personal engineering website and portfolio for **Alexander / Lay007**.

This repository contains the source of the public GitHub Pages site used as a concise professional landing page for work related to:

- **digital signal processing (DSP)**
- **FPGA-oriented engineering**
- **communications and telemetry systems**
- **circuit design and applied electronics**
- **engineering software and technical R&D**

Live site: [lay007.github.io](https://lay007.github.io/)

---

## Overview

The website is designed as a clean, professional one-page portfolio that presents:

- core engineering positioning;
- technical expertise and domains of work;
- selected GitHub projects;
- academic and applied background;
- contact points for collaboration and professional communication.

The current visual direction is intentionally restrained and technical: modern dark UI, strong first-screen positioning, clear project presentation, and a more premium engineering tone rather than a generic personal homepage.

---

## What this repository is for

This repository is the source for my **GitHub Pages business card / portfolio website**.

Its purpose is to:

- present my engineering profile in a clear public format;
- provide a single landing page for GitHub visitors;
- highlight practical areas of expertise;
- connect visitors to selected repositories and contact channels;
- keep the site lightweight, fast, and easy to maintain.

---

## Main sections of the site

The website currently includes sections such as:

- **Hero / intro** — primary positioning and short engineering summary;
- **Core expertise** — DSP, FPGA, communications, secure engineering, circuit design;
- **Selected projects** — representative repositories;
- **Background** — degree, teaching, publications, inventions and patents;
- **Toolchain & platforms** — major languages, tools, and vendor ecosystems;
- **Contact** — GitHub, website, Telegram.

---

## Selected projects featured on the site

The portfolio currently highlights repositories such as:

- [`zynq-sdr-course`](https://github.com/Lay007/zynq-sdr-course) — bilingual SDR course from theory to implementation;
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
- no heavy frontend framework;
- suitable for direct GitHub Pages hosting.

This keeps the website:

- easy to edit;
- easy to publish;
- easy to clone and preview locally;
- independent from external build tooling.

---

## Repository structure

Typical structure is intentionally minimal:

```text
lay007.github.io/
├─ index.html
└─ README.md
```

If the site grows later, the repository can be expanded with:

```text
lay007.github.io/
├─ index.html
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

Open `index.html` in a browser.

### Option 2 — run a lightweight local server

Using Python:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

---

## Editing workflow

Typical update flow:

1. Edit `index.html`
2. Refresh local preview
3. Commit changes
4. Push to `main`
5. Wait for GitHub Pages to publish the update

Example:

```bash
git add index.html README.md
git commit -m "Update portfolio site"
git push origin main
```

---

## Content and tone

This site is not intended to be a generic blog or a multi-page marketing website.

The design goal is a **compact engineering landing page** with:

- strong professional positioning;
- technical credibility;
- clean visual hierarchy;
- minimal maintenance overhead;
- clear links to real work.

---

## Future improvements

Possible next steps for the repository:

- split CSS into separate files if the site grows;
- add project visuals or diagrams;
- add bilingual support;
- add a downloadable CV/resume;
- add Open Graph preview image;
- add favicon and structured metadata;
- move repeated styles and assets into dedicated folders.

---

## Contact

- GitHub: [Lay007](https://github.com/Lay007)
- Website: [lay007.github.io](https://lay007.github.io/)
- Telegram: [@laymob](https://t.me/laymob)

---

## License

Unless noted otherwise, the site content and source in this repository are maintained by the repository owner.
If you want, a dedicated `LICENSE` file can be added separately.
