# Engineering blog: implementation plan

## Goal

Turn the existing engineering portfolio into a portfolio + technical journal without
losing any of the existing project, evidence or reviewer links.

The publication flow is:

Research -> verified evidence -> author-approved article -> this site -> LinkedIn/Habr announcements.

The authoring repository stays private. This public repository must never check out
that private repository during a build, request credentials to it, or accept draft
material as an implicit side effect of merging other work.

## Current baseline (do not break)

The live site is static HTML/CSS, served by GitHub Pages without a build step.
The working URLs include:

- /
- /case-studies.html
- /portfolio-review.html
- /assets/...
- /robots.txt and /sitemap.xml

Existing GitHub Pages settings, project cards, social previews, and the Python site
validator must keep working. Do not migrate the entire site just to add a blog.

## Proposed content and URLs

The new section should be called "Engineering notes" or "Engineering blog".
Canonical entry points:

- /posts/ — index of released articles
- /posts/en/{slug}/ — English technical article
- /posts/ru/{slug}/ — Russian technical article
- /research/ — published research, patents and citations ONLY when publicly safe

Every article should show title, date, language, tags, a useful abstract,
figure captions, experimental conditions, public evidence links, and an honest
limitations section. Similar work in RU/EN can cross-link with hreflang metadata;
a translation is not assumed to be technically identical.

## Content contract

Input is a manually reviewed artifact from the authoring pipeline:

    src/content/posts/en/example-slug.md
    public/posts/en/example-slug/figure.svg
    release-manifest.json

The generated Markdown frontmatter contains title, description, date, tags,
draft=false and language. The release manifest records article IDs and hashes.
No "draft" or "review" input is automatically published. If an article has not
passed explicit author approval, it must not enter this repository at all.

Public code and data repositories are referenced by stable URLs. Model outputs,
simulated illustrations and real RF measurements are clearly distinguished.

## Site implementation, in two safe increments

### Increment A: preparation (this branch)

- Agree on content URLs, release format, review gates, and site requirements.
- Keep the website unchanged and ready for the first approved article.
- Avoid placeholder posts, premature empty indexes, or public copies of drafts.

### Increment B: first approved article

Use Astro for Markdown, math rendering (remark-math + rehype-katex), layouts,
article tags, date ordering and social metadata. Options for integration:

1. Preferred first migration: build just the blog as a separate Astro app and
   combine its generated /posts/ output with the existing static root site.
   Preserve all current HTML and asset paths. Ensure deployment has no collisions.
2. Later, if justified: migrate the entire site to Astro after the existing
   static site validator and URLs have been ported to the new source structure.

Do not install a framework into the current root and immediately replace the
entire site. The current site has a tested static delivery path; preserve it.

## Required gates for public PRs

- Never automatically fetch the private authoring repository in GitHub Actions.
- A release PR must contain the article's rendered Markdown + explicit assets
  from an approved bundle, and a release-manifest.json identifying the snapshot.
- Validate frontmatter fields, local links, figures and assets; reject unexpected
  files and any article marked draft.
- Review public availability of every evidence link by a human author.
- Run privacy/secret scanning on article content AND assets; understand that
  these checks cannot replace manual review.
- Check KaTeX formula output, desktop/mobile figures, alt text and table overflow.
- Check old URLs and both existing static site tests before merge.
- After merge, check the real URL, canonical, OG preview, sitemap and RSS (if added).
- Write LinkedIn and Habr announcements only after the live page has been verified.

## Next milestone

Select one existing reviewed engineering article, prepare a sanitized English
website version, review its results and illustrations, and then implement the
Astro blog integration alongside that one article in a reviewable PR.

Nothing in this planning branch deploys or publishes an article.
