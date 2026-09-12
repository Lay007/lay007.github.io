# Portfolio Content Update Checklist

Use this checklist when updating the public portfolio site.

## Before editing

- [ ] Decide which page is affected: `index.html`, `portfolio-review.html`, or both.
- [ ] Identify the repository evidence that changed.
- [ ] Confirm that every linked repository is public (private repositories return 404 to visitors).
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
http://localhost:8000/404.html
```

Check the pages at desktop width and at a phone width of about 390 px.

## Validation

```bash
python -m unittest discover -s tests -p "test_site_validator.py" -v
python tools/check_site.py
```

If the positioning, flagship projects or favicon changed, update `tools/social-preview.html` and regenerate the raster assets:

```bash
python tools/render_assets.py
```

## Release check

- [ ] Validator and tests pass.
- [ ] Links to GitHub repositories open correctly.
- [ ] Mobile first screen remains readable.
- [ ] Open Graph preview image still matches the current positioning.
- [ ] `lastmod` in `sitemap.xml` is updated for changed pages; new indexable pages are added.
- [ ] README is synchronized with new site structure when files are added.

## Tone rule

Keep the site technical, compact and evidence-oriented. The portfolio should not sound like a generic CV; it should help a reviewer quickly find proof artifacts.
