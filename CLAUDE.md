# MyKahawa shop: notes for Claude

Brand rules come from the `mykahawa-brand` plugin (repo `wasisi/mykahawa_brand`, see
`.claude/settings.json`). Follow it for anything user-facing.

Brand assets in this project:

- Theme: `wp-content/themes/mykahawa/` (child of Twenty Twenty-Five). Tokens live in
  `theme.json` (colours `green`, `green-dark`, `brown`, `brown-dark`, `cream`, `slate`,
  `grey`; fonts `helvetica`, `bebas`); extra CSS in `style.css`.
- `wp-content/themes/mykahawa/assets/` holds copies from the brand package:
  `logo.png` = color, `logo-white.png` = blanco-verde, `logo-black.png` = negro,
  `fonts/bebas-neue-400.woff2`, favicons = black-on-white package. Copy new assets here;
  never link to the brand repo from the site.
- Shop behaviour (delivery zones, checkout fields, badges, product import): 
  `wp-content/plugins/mykahawa-shop/`. Maintenance and product workflow: `README.md`.
