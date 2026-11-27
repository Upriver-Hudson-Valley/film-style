# Local Fonts (Gitignored)

Licensed font files are intentionally excluded from git.

`templates/title-card.html`, `templates/lower-third.html`, and `templates/vendor-tag.html` automatically check your locally installed macOS `Recoleta` font first (`local('Recoleta')`). For guaranteed deterministic headless Chromium renders across machines, also drop your licensed font files here:

- `Recoleta-Regular.woff2` (or `Recoleta-Regular.otf`)
