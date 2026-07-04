# Portfolio Content Update Checklist

Use this checklist when updating the public portfolio site.

## Before editing

- [ ] Decide which page is affected: `index.html`, `portfolio-review.html`, or both.
- [ ] Identify the repository evidence that changed.
- [ ] Prefer linking to stable README sections, reports, checklists or generated artifacts.
- [ ] Avoid adding claims that are only planned and not yet supported by repository evidence.

## Evidence quality

A project card or review entry should answer:

| Question | Good answer |
|---|---|
| What was built? | short project scope and engineering problem |
| How was it verified? | CI, tests, deterministic vectors, scripts, reports or metrics |
| What can a reviewer open first? | README, reviewer guide, evidence map or acceptance checklist |
| What is still pending? | clear limitation or next proof point |

## Local preview

```bash
python -m http.server 8000
```

Open:

```text
http://localhost:8000
http://localhost:8000/portfolio-review.html
```

## Release check

- [ ] Links to GitHub repositories open correctly.
- [ ] External links are still relevant.
- [ ] Mobile first screen remains readable.
- [ ] Open Graph preview image still matches the current positioning.
- [ ] `sitemap.xml` and `robots.txt` do not need updates.
- [ ] README is synchronized with new site structure when files are added.

## Tone rule

Keep the site technical, compact and evidence-oriented. The portfolio should not sound like a generic CV; it should help a reviewer quickly find proof artifacts.
