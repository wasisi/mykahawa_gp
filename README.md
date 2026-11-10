# mykahawa.org

MyKahawa is a market intelligence and discovery platform for Kenyan coffee:

- **Market intelligence**: Nairobi Coffee Exchange auction prices, grades, volumes and buyers (2015–2020), charts and market reports.
- **Industry discovery**: a directory of 2,783 growers (cooperative societies, factories, estates) with a map and a page for each grower, plus licensed exporters, dealers, millers, agents and warehousemen.
- **Guides**: Kenya coffee grades, laws and regulations, licensing, the value chain and a glossary.

The site is a static Jekyll site hosted free on **GitHub Pages** (branch `gh-pages`, custom domain `www.mykahawa.org` via `CNAME`). There is no server, database or paid service.

## How the site is organised

| Path | What it is |
|---|---|
| `index.html` | Homepage |
| `transactions.md` | Prices page (`/transactions.html`): charts and tables |
| `directory.md`, `dealers.md` | Directory hub and all licensed businesses |
| `directory/*.md` | Directory category pages (exporters, millers, cooperatives…) |
| `directory/county/*.md` | County pages: **generated**, do not edit |
| `list/producers.html` | Growers map and search (`/growers.html`) |
| `_growers/*.md` | One page per grower at `/producer/<id>/<slug>/` (the URLs of the old site): **generated**, do not edit |
| `_producers/*.md` | Hand-written grower profiles (text and photos). Set `grower_id:` and the profile appears on that grower's page. |
| `_reports/*.md` | Market reports (`/reports/<name>/`). Numbers come from `_data/market.json` and `_data/insights.json`. |
| `_projects/*.md` | Guides: grades, laws, licensing, glossary, value chain, quality, certification |
| `list/projects.md` | Guides hub (`/kenya-coffee.html`) |
| `get-listed.md` | "Get your farm listed" page with an email template |
| `_node/` | About-type pages: subscribe, terms, privacy |
| `_layouts/` | `base` (all pages), `directory`, `grower`, `report`, and `default` (sidebar pages) |
| `_includes/structure/` | Head (SEO tags), navigation, footer, scripts |
| `_data/navigation.yml` | Main menu |
| `_data/grade_standards.yml` | Official Kenya grades (Fifth Schedule of the Coffee Regulations) |
| `_data/glossary.yml` | Glossary entries (keep alphabetical) |
| `_data/*.json` | **Generated** by the data script |
| `theme/_sass/_mk.scss` | Site styles (loaded last; overrides the older theme) |
| `theme/js/` | Map (`growers-map.js`), grower search, charts, table filter |
| `theme/vendor/` | Self-hosted libraries: Leaflet 1.9.4, Chart.js 4.6.1, jQuery 3.7.1, Bootstrap 4.6.2 JS |
| `scripts/` | `build_data.py` (data pipeline) and `docker_build.sh` (local build) |

## Data

Raw data lives in `data/` and is **not published** on the website (see `exclude` in `_config.yml`). Only these derived files are served, because the browser needs them:

- `data/growers/growers.json`: grower search
- `data/growers/growers_map.geojson`: map points
- `data/market/sales.json`, `data/market/grade_prices.json`: charts

> The raw files are still in this repository's history on GitHub. To keep them private, move them to a private repository or keep them off GitHub. The site only needs the generated files.

### Updating the data

1. Update the raw files in `data/`. For example, append new auction results to `data/transactions/coffeetransactions.csv` using the same columns, or add growers to `data/growers/coffeegrowers.csv`.
2. Regenerate everything derived from them:

   ```
   python3 scripts/build_data.py
   ```

   This rewrites `_data/*.json`, the browser data files, `directory/county/*.md` and `_growers/*.md`. Prices, charts, grower pages and report figures all update automatically.
3. Build and check the site (below), then commit and push.

Notes on the data:

- Prices are US$ per 50 kg bag. Averages are weighted by volume.
- Seasons run 1 October to 30 September.
- Lots marked `BULK` mix several growers. They count in market totals but are excluded from grower and county figures.
- Text in the transactions file is Windows-1252, and some names were double-encoded. The script repairs this.

## Building locally

GitHub Pages builds the site automatically on every push to `gh-pages`. To preview locally, with no Ruby needed:

```
scripts/docker_build.sh                        # builds into .out/ (about 40 s)
cd .out && python3 -m http.server 4005         # open http://localhost:4005
```

Or with Ruby installed: `bundle install && bundle exec jekyll serve`.

## Common tasks

- **Add a grower profile**: create `_producers/<date>-<name>.md` with `grower_id: <id>` (the number in the grower's URL), `title`, optional `images:` (photo URLs) and the text. Rebuild data so the old profile URL redirects.
- **Add a report**: copy a file in `_reports/`, change `title`, `heading`, `lead`, `description` and `date`, and write the content. It appears on `/reports/` and the homepage automatically.
- **Edit the menu**: `_data/navigation.yml`.
- **Update licensing or legal guides**: `_projects/kenya_coffee_licensing.md` and `_projects/kenya_coffee_laws.md`. They summarise the Crops (Coffee) (General) Regulations, 2019 (amended to 2022) and the Capital Markets (Coffee Exchange) Regulations, 2020.

## Accounts and services

- **Analytics**: Google Tag Manager `GTM-N945XH3` (in `_includes/structure/head.html`).
- **Maps**: OpenStreetMap tiles (free, attribution required, light use only).
- **Email**: `wasisi.coffee@gmail.com`. The subscribe page and listing forms open the visitor's email app; the old Mailchimp list no longer exists.
- **Donations**: Ko-fi `L4L629RGA`.
- **Domain**: DNS at Gandi. The `www` CNAME points to `wasisi.github.io`; the apex A/AAAA records point to the GitHub Pages IPs.
