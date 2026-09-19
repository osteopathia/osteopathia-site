# Osteopathia.ca — Phase 1

Static English/Russian website for Roman Dvulat. HTML and CSS only; no JavaScript, tracking, accounts, forms, external fonts or backend.

## Pages

English: `/`, `/about/`, `/approach/`, `/articles/`, `/contact/`.
Russian: `/ru/`, `/ru/about/`, `/ru/approach/`, `/ru/articles/`, `/ru/useful/`.

All links are relative: the site works at a GitHub Pages project URL and later at a custom domain. Language is selected explicitly; there is no automatic detection. Contact and Useful switch to the other language's home because they have no equivalent section.

## Editing

`assets/style.css` is shared by every page. `tools/build.py` is an optional, standard-library-only authoring helper containing the common header, navigation and footer, and the short page placeholders. Run `python tools/build.py` to regenerate the ten foundation pages; Python is not required on the host. Change these foundation pages in the helper so a rebuild does not overwrite manual edits.

Add future articles as `articles/slug/index.html` or `ru/articles/slug/index.html`, using the corresponding language's page shell with relative paths adjusted for depth. Add article links to the article index in the helper. New articles are not overwritten by the helper.

Replace the marked portrait placeholder only when the owner supplies a current photo. Provide accurate alt text. The old portrait and old contact details have not been published. The business name is retained as text. The logo in the supplied photograph is not a clean standalone asset; use an owner-approved logo file when supplied. The favicon is a temporary O monogram, not a recreation of the logo.

## Publishing and preservation

This is the new repository `osteopathia/osteopathia-site`. Enable GitHub Pages using `main` and `/(root)` to publish the static files. No build workflow is needed.

The existing `osteopathia/goods` repository, its history, `book1/`, CNAME and domain configuration remain untouched. Its inspected recovery commit is `65b8c34babc6bf6884f3180758dbd0dbaf50f6d2`.

No CNAME is included here while the domain still belongs to the old site. Move the custom domain only after the new site is checked and the owner approves the cutover. Do not change DNS as part of Phase 1 preparation.
