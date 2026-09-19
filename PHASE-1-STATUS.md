# Phase 1 status — 2026-09-19 UTC

Target: osteopathia/osteopathia-site (new, empty repository).

## Implemented locally
- 10 semantic HTML pages, separate English and Russian experiences.
- Explicit EN | RU switch, English at root, no language detection.
- Shared header/footer generated from tools/build.py and shared CSS.
- Responsive CSS at 800px and 560px, mobile navigation without JavaScript.
- Neutral labeled photo placeholder; no old portrait or old contact details.
- Navy, blue, light blue and white inspired by the supplied business card.
- Temporary favicon; Canada U-Paramed Service retained as text.
- Short placeholder copy only; no invented biography or medical claims.

## Files
index.html
about/index.html
approach/index.html
articles/index.html
contact/index.html
ru/index.html
ru/about/index.html
ru/approach/index.html
ru/articles/index.html
ru/useful/index.html
assets/style.css
assets/favicon.svg
.nojekyll
tools/build.py
README.md
PHASE-1-STATUS.md

## Validation
PASS: all ten pages have one H1, correct lang, working local href/asset targets and skip links, and no scripts.
Responsive CSS implemented, but browser visual/mobile checks remain pending: cloud browser could not access the local preview. Do not report real iPhone/iPad validation as completed.

## Publication blocker
GitHub metadata reports the linked user's admin/push permissions. Actual create_file request for README.md returned HTTP 403 Resource not accessible by integration. No successful remote write or deployment occurred. Repository-level user rights do not establish integration write permission.

## Preservation
Nothing removed or replaced in osteopathia/goods. Its CNAME, book1 and history remain untouched. Previously inspected recovery commit: 65b8c34babc6bf6884f3180758dbd0dbaf50f6d2.
No CNAME added to the new site, no DNS changes, no changes to Roman Health.

## Remaining
Upload these files to the new repository, enable Pages (main, root), check the public project URL and responsive layout. Only after review, decide on moving osteopathia.ca from goods. Final text, current portrait and a clean standalone logo asset remain owner-supplied items.
