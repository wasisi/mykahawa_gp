# www.mykahawa.org: notes for Claude

Brand rules come from the `mykahawa-brand` plugin (repo `wasisi/mykahawa_brand`, see
`.claude/settings.json`). Follow it for anything user-facing.

This site is **Jekyll on GitHub Pages** (published from the `gh-pages` branch; domain in
`CNAME`). Content collections: `_growers`, `_producers`, `_traders`, `_projects`,
`_reports`; data in `_data/` and `data/`.

Styling:

- Sass lives in `theme/_sass/` (wired up in `_config.yml`); entry points
  `theme/css/main.scss` and `theme/css/site.scss`.
- `theme/_sass/_mk.scss` is the 2026 refresh. It loads last and overrides the older theme
  files (`_styles.scss`, `_site.scss`, …). Put new styles there and use its `$mk-*`
  variables (`$mk-green` #4b8030 = brand green, `$mk-coffee` #3b2a20 = brand brown-dark,
  `$mk-cream` #f7f3ee).
- Known gap: the site still uses Merriweather / Source Sans (and Raleway / Open Sans in
  old files), not the brand's Helvetica Neue + Bebas Neue. Don't copy those fonts into
  new work. Switching the whole site over is a separate, deliberate change, so ask first.

Brand assets in this project:

- Logos are copies in `theme/img/` (`logo.png`, `logo.svg`, `logo-md-inv.png` = on dark,
  `logo_on_coffee*.png`, `og-image.jpg` for social previews); favicons in the repo root.
  `_config.yml` points to `/theme/img/logo.png` and `/theme/img/logo-152.png`.
- Copy new assets from the brand package into `theme/img/`. Never link to the brand repo
  from the site, and never add the Bernound font files here (the site is public).
