#!/usr/bin/env python3
"""Build the derived data files the site uses from the raw CSVs in /data.

Run from the repo root:   python3 scripts/build_data.py

Inputs (raw, unchanged):
  data/growers/coffeegrowers.csv
  data/growers/coffeegrowers_location.geojson
  data/dealers/coffeedealers.csv
  data/counties/kenya_counties.csv
  data/grades/coffeegrades.csv
  data/transactions/coffeetransactions.csv

Outputs:
  _data/*.json          read by Jekyll at build time (static HTML tables, stats)
  data/growers/growers.json, data/growers/growers_map.geojson
  data/market/*.json    loaded by the charts in the browser

When new auction results arrive, append them to coffeetransactions.csv and
re-run this script; every page and chart picks up the new numbers.
"""
import csv
import json
import os
import re
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
JDATA = os.path.join(ROOT, "_data")
BAG_KG = 50  # NCE prices are quoted in US$ per 50 kg bag

GROWER_TYPES = {
    "Cooperative Society": "Cooperative society",
    "coop": "Cooperative society",
    "Factory": "Factory",
    "factory": "Factory",
    "Estate Producers": "Estate",
    "Small Estates": "Small estate",
    "estate_small": "Small estate",
}

PLURALS = {"Cooperative society": "Cooperative societies", "Factory": "Factories",
           "Estate": "Estates", "Small estate": "Small estates", "Other": "Other"}

DEALER_CATEGORIES = {
    # raw category: (slug, page title, short label)
    "Coffee Dealers": ("coffee-exporters", "Coffee exporters and dealers in Kenya", "Exporters and dealers"),
    "Coffee Millers": ("coffee-millers", "Coffee millers in Kenya", "Millers"),
    "Commercial Marketing Agents": ("marketing-agents", "Commercial coffee marketing agents in Kenya", "Commercial marketing agents"),
    "Grower Marketers": ("grower-marketers", "Coffee grower marketers in Kenya", "Grower marketers"),
    "Commercial Coffee Warehousemen": ("warehousemen", "Coffee warehousemen in Kenya", "Warehousemen"),
    "Private Coffee Warehousemen": ("warehousemen", "Coffee warehousemen in Kenya", "Warehousemen"),
    "Management Agents": ("management-agents", "Coffee management agents in Kenya", "Management agents"),
}


def fix_mojibake(s):
    """Undo text that was UTF-8 encoded and then read as Windows-1252 (e.g. 'Ã‚Â' for a non-breaking space)."""
    for _ in range(3):
        if "Ã" not in s and "Â" not in s:
            break
        try:
            s = s.encode("cp1252").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            break
    return s


def clean(s):
    if s is None:
        return ""
    s = fix_mojibake(s)
    s = re.sub(r"[\x00-\x1f\x7f-\x9f]", "", s.replace("\xa0", " ")).strip()
    return "" if s.upper() == "NULL" else re.sub(r"\s+", " ", s)


def num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def write_json(path, obj, compact=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        if compact:
            json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))
        else:
            json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def season_of(date):
    """Kenyan coffee year runs 1 Oct - 30 Sep."""
    y, m = int(date[:4]), int(date[5:7])
    start = y if m >= 10 else y - 1
    return f"{start}/{str(start + 1)[2:]}"


# ---------------------------------------------------------------- counties
counties = {}
with open(os.path.join(DATA, "counties/kenya_counties.csv"), encoding="utf-8") as f:
    for r in csv.DictReader(f):
        counties[r["id"]] = clean(r["county_name"])

# ---------------------------------------------------------------- growers
growers = []
with open(os.path.join(DATA, "growers/coffeegrowers.csv"), encoding="utf-8") as f:
    for r in csv.DictReader(f):
        code = clean(r["title"])
        if code.endswith("_temp"):
            code = ""
        name = clean(r["producer_name"]) or code
        if not name or name.upper() == "BULK":  # BULK = lots pooled from several growers, not a grower
            continue
        lat, lon = num(r["lat"]), num(r["lon"])
        slug = clean(r["slug"]) or slugify(name).replace("-", "_")
        growers.append({
            "id": int(r["id"]),
            "slug": slug,
            "url": f"/producer/{r['id']}/{slug}/",
            "lat": lat,
            "lon": lon,
            "verified": clean(r["location_accuracy"]).lower() in ("verified", "good"),
            "code": code,
            "name": name,
            "type": GROWER_TYPES.get(clean(r["actor"]), "Other"),
            "county": counties.get(r["county_name_id"], ""),
            "affiliation": clean(r["affiliation_name"]),
            "mapped": lat is not None and lon is not None,
        })
growers.sort(key=lambda g: g["name"].lower())

# Slim JSON for the in-browser search (short keys keep it small).
write_json(os.path.join(DATA, "growers/growers.json"), [
    {"i": g["id"], "u": g["url"], "c": g["code"], "n": g["name"], "t": g["type"], "k": g["county"], "a": g["affiliation"], "m": int(g["mapped"])}
    for g in growers
], compact=True)
write_json(os.path.join(JDATA, "growers.json"),
           [{k: g[k] for k in ("id", "url", "code", "name", "type", "county", "affiliation", "mapped")} for g in growers],
           compact=True)

type_counts = Counter(g["type"] for g in growers)
county_counts = Counter(g["county"] for g in growers if g["county"])

# Map points: normalise types and keep only what the popups need.
with open(os.path.join(DATA, "growers/coffeegrowers_location.geojson"), encoding="utf-8") as f:
    gj = json.load(f)
features = []
for ft in gj["features"]:
    p = ft["properties"]
    lon, lat = ft["geometry"]["coordinates"][:2]
    acc = clean(p.get("Location accuracy"))
    features.append({
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [round(lon, 5), round(lat, 5)]},
        "properties": {
            "id": p.get("id"),
            "url": next((g["url"] for g in growers if g["id"] == p.get("id")), ""),
            "name": clean(p.get("producer_name")),
            "code": clean(p.get("cbk_growers_code")),
            "type": GROWER_TYPES.get(clean(p.get("Actor")), "Other"),
            "verified": acc.lower() in ("verified", "good"),
        },
    })
write_json(os.path.join(DATA, "growers/growers_map.geojson"),
           {"type": "FeatureCollection", "features": features}, compact=True)

# ---------------------------------------------------------------- dealers
dealers = []
with open(os.path.join(DATA, "dealers/coffeedealers.csv"), encoding="cp1252", errors="replace") as f:
    for r in csv.DictReader(f):
        cat = clean(r["category"])
        slug, _, label = DEALER_CATEGORIES.get(cat, ("other", "", cat))
        web = clean(r["website"])
        if web and not web.startswith("http"):
            web = "http://" + web
        dealers.append({
            "name": clean(r["title"]),
            "category": cat,
            "group": slug,
            "label": label,
            "license": clean(r["license_number"]),
            "website": web,
        })
dealers.sort(key=lambda d: d["name"].lower())
write_json(os.path.join(JDATA, "dealers.json"), dealers)

dealer_groups = []
seen = set()
for cat, (slug, title, label) in DEALER_CATEGORIES.items():
    if slug in seen:
        continue
    seen.add(slug)
    dealer_groups.append({"slug": slug, "title": title, "label": label,
                          "count": sum(1 for d in dealers if d["group"] == slug)})

# ---------------------------------------------------------------- grades
grades = []
with open(os.path.join(DATA, "grades/coffeegrades.csv"), encoding="utf-8") as f:
    for r in csv.DictReader(f):
        grades.append({k: clean(v) for k, v in r.items() if k != "id"})

# ---------------------------------------------------------------- transactions
sales = defaultdict(lambda: {"lots": 0, "kg": 0.0, "usd": 0.0})
by_season = defaultdict(lambda: {"lots": 0, "kg": 0.0, "usd": 0.0, "sales": set()})
grade_season = defaultdict(lambda: {"kg": 0.0, "usd": 0.0, "lots": 0})
grade_total = defaultdict(lambda: {"kg": 0.0, "usd": 0.0, "lots": 0})
buyers = defaultdict(lambda: {"kg": 0.0, "usd": 0.0, "lots": 0, "seasons": set()})
marks = defaultdict(lambda: {"kg": 0.0, "usd": 0.0, "lots": 0})
new_bucket = lambda: {"kg": 0.0, "usd": 0.0, "lots": 0}
gstats = defaultdict(lambda: {"tot": new_bucket(), "first": None, "last": None, "sales": set(),
                              "seasons": defaultdict(new_bucket), "grades": defaultdict(new_bucket),
                              "buyers": defaultdict(new_bucket), "marks": Counter()})

with open(os.path.join(DATA, "transactions/coffeetransactions.csv"), encoding="cp1252", errors="replace") as f:
    for r in csv.DictReader(f):
        kg, price, date = num(r["weightbought_kgr"]), num(r["price"]), clean(r["isodate"])
        if not kg or not price or not date:
            continue
        usd = kg / BAG_KG * price
        season = season_of(date)
        grade = clean(r["grade"])
        buyer = clean(r["buyer"])
        for bucket in (sales[date], by_season[season]):
            bucket["lots"] += 1
            bucket["kg"] += kg
            bucket["usd"] += usd
        by_season[season]["sales"].add(date)
        if grade and grade != "#N/A":
            for bucket in (grade_season[(grade, season)], grade_total[grade]):
                bucket["kg"] += kg
                bucket["usd"] += usd
                bucket["lots"] += 1
        if buyer:
            b = buyers[buyer]
            b["kg"] += kg
            b["usd"] += usd
            b["lots"] += 1
            b["seasons"].add(season)
        gid = num(r["producercode_id"])
        if gid:
            gs = gstats[int(gid)]
            buckets = [gs["tot"], gs["seasons"][season]]
            if grade and grade != "#N/A":
                buckets.append(gs["grades"][grade])
            if buyer:
                buckets.append(gs["buyers"][buyer])
            for bucket in buckets:
                bucket["kg"] += kg
                bucket["usd"] += usd
                bucket["lots"] += 1
            gs["sales"].add(date)
            gs["first"] = min(gs["first"] or date, date)
            gs["last"] = max(gs["last"] or date, date)
            gs["marks"][clean(r["marks2"]) or clean(r["marks"])] += 1
        mark = clean(r["producer_name"])
        if mark and mark.upper() != "BULK":  # BULK = pooled lots, not a single grower
            m = marks[mark]
            m["kg"] += kg
            m["usd"] += usd
            m["lots"] += 1


def avg_price(b):
    return round(b["usd"] / (b["kg"] / BAG_KG), 2) if b["kg"] else None


sale_rows = [{"date": d, "season": season_of(d), "lots": s["lots"], "bags": round(s["kg"] / BAG_KG),
              "tonnes": round(s["kg"] / 1000, 1), "usd": round(s["usd"]), "price": avg_price(s)}
             for d, s in sorted(sales.items())]
write_json(os.path.join(DATA, "market/sales.json"), sale_rows, compact=True)

seasons = sorted(by_season)
season_rows = [{"season": s, "sales": len(by_season[s]["sales"]), "lots": by_season[s]["lots"],
                "tonnes": round(by_season[s]["kg"] / 1000), "usd": round(by_season[s]["usd"]),
                "price": avg_price(by_season[s])} for s in seasons]

main_grades = ["AA", "AB", "PB", "C", "E", "TT", "T", "HE", "MH", "ML", "SB", "UG1", "UG2"]
grade_rows = []
for g in sorted(grade_total, key=lambda g: -grade_total[g]["kg"]):
    t = grade_total[g]
    grade_rows.append({"grade": g, "lots": t["lots"], "tonnes": round(t["kg"] / 1000),
                       "price": avg_price(t),
                       "by_season": {s: avg_price(grade_season[(g, s)]) for s in seasons
                                     if grade_season[(g, s)]["kg"]}})
write_json(os.path.join(DATA, "market/grade_prices.json"), {
    "seasons": seasons,
    "grades": [{"grade": g["grade"], "prices": [g["by_season"].get(s) for s in seasons]}
               for g in grade_rows if g["grade"] in main_grades],
}, compact=True)

total_kg = sum(b["kg"] for b in buyers.values())
buyer_rows = sorted(({"name": n, "lots": b["lots"], "tonnes": round(b["kg"] / 1000),
                      "usd": round(b["usd"]), "share": round(100 * b["kg"] / total_kg, 1),
                      "price": avg_price(b), "seasons": len(b["seasons"])}
                     for n, b in buyers.items()), key=lambda r: -r["tonnes"])
mark_rows = sorted(({"name": n, "lots": m["lots"], "tonnes": round(m["kg"] / 1000),
                     "price": avg_price(m)} for n, m in marks.items()),
                   key=lambda r: -r["tonnes"])

all_kg = sum(s["kg"] for s in sales.values())
all_usd = sum(s["usd"] for s in sales.values())
all_price = all_usd / (all_kg / BAG_KG)
write_json(os.path.join(JDATA, "market.json"), {
    "first_sale": sale_rows[0]["date"],
    "last_sale": sale_rows[-1]["date"],
    "sales": len(sale_rows),
    "lots": sum(s["lots"] for s in sales.values()),
    "tonnes": round(all_kg / 1000),
    "usd": round(all_usd),
    "price": round(all_usd / (all_kg / BAG_KG), 2),
    "buyer_count": len(buyers),
    "mark_count": len(marks),
    "seasons": season_rows,
    "grades": grade_rows,
    "top_buyers": buyer_rows[:30],
    "top_marks": mark_rows[:50],
})

write_json(os.path.join(JDATA, "directory.json"), {
    "growers_total": len(growers),
    "growers_mapped": sum(g["mapped"] for g in growers),
    "grower_types": [{"type": t, "plural": PLURALS.get(t, t), "count": c} for t, c in type_counts.most_common()],
    "grower_counties": [{"county": c, "slug": slugify(c), "count": n} for c, n in county_counts.most_common()],
    "dealers_total": len(dealers),
    "dealer_groups": dealer_groups,
    "grades": grades,
})

# ---------------------------------------------------------------- report insights
# Figures for the market reports in /reports, derived from the per-grower stats.
grower_by_id = {g["id"]: g for g in growers}


def summarise(stats_list):
    tot = new_bucket()
    grades_ = defaultdict(new_bucket)
    for st in stats_list:
        for k in ("kg", "usd", "lots"):
            tot[k] += st["tot"][k]
        for gr, b in st["grades"].items():
            for k in ("kg", "usd", "lots"):
                grades_[gr][k] += b[k]
    top = sum(grades_[x]["kg"] for x in ("E", "AA", "AB", "PB"))
    return {
        "tonnes": round(tot["kg"] / 1000), "usd": round(tot["usd"]), "lots": tot["lots"],
        "price": avg_price(tot),
        "aa": avg_price(grades_["AA"]), "ab": avg_price(grades_["AB"]), "c": avg_price(grades_["C"]),
        "top_share": round(100 * top / tot["kg"]) if tot["kg"] else None,
    }


county_groups = defaultdict(list)
type_groups = defaultdict(list)
for gid, st in gstats.items():
    g = grower_by_id.get(gid)
    if not g:
        continue
    type_groups[g["type"]].append(st)
    if g["county"]:
        county_groups[g["county"]].append(st)

county_rows = []
for c, sts in county_groups.items():
    row = summarise(sts)
    row.update({"county": c, "slug": slugify(c), "growers": len(sts)})
    county_rows.append(row)
county_rows.sort(key=lambda r: -r["tonnes"])
type_rows = []
for t, sts in type_groups.items():
    if t == "Other":
        continue
    row = summarise(sts)
    row.update({"type": t, "plural": PLURALS.get(t, t), "growers": len(sts)})
    type_rows.append(row)
type_rows.sort(key=lambda r: -r["tonnes"])

# Buyer concentration by season (share of the top 4 buyers and Herfindahl-Hirschman index).
season_buyers = defaultdict(lambda: defaultdict(float))
with open(os.path.join(DATA, "transactions/coffeetransactions.csv"), encoding="cp1252", errors="replace") as f:
    for r in csv.DictReader(f):
        kg, date, buyer = num(r["weightbought_kgr"]), clean(r["isodate"]), clean(r["buyer"])
        if kg and date and buyer and num(r["price"]):
            season_buyers[season_of(date)][buyer] += kg
concentration = []
for s in seasons:
    shares = sorted((v / sum(season_buyers[s].values()) for v in season_buyers[s].values()), reverse=True)
    concentration.append({"season": s, "buyers": len(shares), "top4": round(100 * sum(shares[:4]), 1),
                          "hhi": round(sum((100 * x) ** 2 for x in shares))})

# Grade premiums by season.
premiums = []
for s in seasons:
    aa, ab, c = (avg_price(grade_season[(g, s)]) for g in ("AA", "AB", "C"))
    premiums.append({"season": s, "aa": aa, "ab": ab, "c": c,
                     "aa_over_ab": round(100 * (aa / ab - 1)) if aa and ab else None,
                     "ab_over_c": round(100 * (ab / c - 1)) if ab and c else None})

# Price swings: lowest and highest sale average in each season.
swings = []
for s in seasons:
    rows = [r for r in sale_rows if r["season"] == s]
    lo, hi = min(rows, key=lambda r: r["price"]), max(rows, key=lambda r: r["price"])
    swings.append({"season": s, "low": lo["price"], "low_date": lo["date"], "high": hi["price"], "high_date": hi["date"]})

top_growers = [{"name": g["name"], "url": g["url"], "type": g["type"], "county": g["county"],
                "tonnes": round(gstats[g["id"]]["tot"]["kg"] / 1000), "price": avg_price(gstats[g["id"]]["tot"])}
               for g in sorted((g for g in growers if g["id"] in gstats),
                               key=lambda g: -gstats[g["id"]]["tot"]["kg"])[:15]]
# Best-paid AA producers with meaningful volume (at least 20 tonnes of AA).
aa_leaders = sorted(
    ({"name": grower_by_id[gid]["name"], "url": grower_by_id[gid]["url"], "county": grower_by_id[gid]["county"],
      "tonnes": round(st["grades"]["AA"]["kg"] / 1000), "price": avg_price(st["grades"]["AA"])}
     for gid, st in gstats.items() if gid in grower_by_id and st["grades"]["AA"]["kg"] >= 20000),
    key=lambda r: -r["price"])[:15]

bulk_kg = sum(st["tot"]["kg"] for gid, st in gstats.items() if gid not in grower_by_id)
write_json(os.path.join(JDATA, "insights.json"), {
    "bulk_share": round(100 * bulk_kg / all_kg),
    "counties": county_rows,
    "types": type_rows,
    "concentration": concentration,
    "premiums": premiums,
    "swings": swings,
    "top_growers": top_growers,
    "aa_leaders": aa_leaders,
})

# ---------------------------------------------------------------- county pages
county_dir = os.path.join(ROOT, "directory/county")
os.makedirs(county_dir, exist_ok=True)
for c, n in county_counts.most_common():
    by_type = Counter(g["type"] for g in growers if g["county"] == c)
    parts = ", ".join(f"{v} {PLURALS[t].lower() if v != 1 else t.lower()}"
                      for t, v in by_type.most_common() if t != "Other")
    with open(os.path.join(county_dir, slugify(c) + ".md"), "w", encoding="utf-8") as f:
        f.write(f"""---
# Generated by scripts/build_data.py - edit the script, not this file.
layout: directory
title: "Coffee growers in {c} County"
heading: "Coffee cooperatives, factories and estates in {c} County"
description: "{n} coffee growers in {c} County, Kenya: {parts}. Names and growers (CBK) codes."
lead: "MyKahawa lists {n} coffee growers in {c} County: {parts}."
county: "{c}"
breadcrumbs:
  - title: Directory
    url: /directory.html
  - title: Counties
    url: /directory.html#counties
permalink: /directory/county/{slugify(c)}.html
---
""")

# ---------------------------------------------------------------- grower pages
# One page per grower at the URL the old site used: /producer/<id>/<slug>/
grower_dir = os.path.join(ROOT, "_growers")
os.makedirs(grower_dir, exist_ok=True)
for old in os.listdir(grower_dir):
    if old.endswith(".md"):
        os.remove(os.path.join(grower_dir, old))

ranked = sorted((g for g in growers if g["id"] in gstats), key=lambda g: -gstats[g["id"]]["tot"]["kg"])
rank = {g["id"]: i + 1 for i, g in enumerate(ranked)}
grade_market = {g["grade"]: g["price"] for g in grade_rows}
by_county = defaultdict(list)
for g in ranked:
    if g["county"]:
        by_county[g["county"]].append(g)


# Old profile pages (_producers) now redirect to the grower page.
profile_redirects = defaultdict(list)
for fn in os.listdir(os.path.join(ROOT, "_producers")):
    with open(os.path.join(ROOT, "_producers", fn), encoding="utf-8") as f:
        m = re.search(r"^grower_id:\s*(\d+)", f.read(), re.M)
    if m:
        profile_redirects[int(m.group(1))].append("/producers/" + slugify(fn[:-3]) + ".html")


def yaml_val(v):
    return json.dumps(v, ensure_ascii=False)


for g in growers:
    st = gstats.get(g["id"])
    fm = {
        "layout": "grower",
        "title": f"{g['name']}" + (f" ({g['code']})" if g["code"] else ""),
        "grower_id": g["id"],
        "name": g["name"],
        "code": g["code"],
        "type": g["type"],
        "county": g["county"],
        "county_slug": slugify(g["county"]) if g["county"] else "",
        "affiliation": g["affiliation"],
        "mapped": g["mapped"],
        "verified": g["verified"],
        "permalink": g["url"],
    }
    if g["mapped"]:
        fm["lat"], fm["lon"] = round(g["lat"], 5), round(g["lon"], 5)
    where = f" in {g['county']} County" if g["county"] else ""
    if st:
        t = st["tot"]
        price = avg_price(t)
        fm.update({
            "has_sales": True,
            "rank": rank[g["id"]],
            "ranked_of": len(ranked),
            "lots": t["lots"],
            "tonnes": round(t["kg"] / 1000, 1),
            "usd": round(t["usd"]),
            "price": price,
            "premium": round(100 * (price / all_price - 1)),
            "first_sale": st["first"],
            "last_sale": st["last"],
            "sale_count": len(st["sales"]),
            "marks": [m for m, _ in st["marks"].most_common(5) if m],
            "seasons": [{"season": s, "lots": b["lots"], "tonnes": round(b["kg"] / 1000, 1), "price": avg_price(b)}
                        for s, b in sorted(st["seasons"].items())],
            "grades": [{"grade": k, "lots": b["lots"], "tonnes": round(b["kg"] / 1000, 1), "price": avg_price(b),
                        "market": grade_market.get(k)}
                       for k, b in sorted(st["grades"].items(), key=lambda kv: -kv[1]["kg"])],
            "buyers": [{"name": k, "lots": b["lots"], "tonnes": round(b["kg"] / 1000, 1),
                        "share": round(100 * b["kg"] / t["kg"]), "price": avg_price(b)}
                       for k, b in sorted(st["buyers"].items(), key=lambda kv: -kv[1]["kg"])[:8]],
        })
        fm["description"] = (f"{g['name']}, a coffee {g['type'].lower()}{where}, Kenya: {t['lots']:,} lots and "
                             f"{t['kg']/1000:,.0f} tonnes sold at the Nairobi Coffee Exchange, average price "
                             f"US${price:,.0f} per 50 kg bag, prices by grade and top buyers.")
    else:
        fm["has_sales"] = False
        fm["description"] = (f"{g['name']}" + (f" (growers code {g['code']})" if g["code"] else "") +
                             f", a coffee {g['type'].lower()}{where}, Kenya. Listed in the MyKahawa coffee directory.")
        fm["sitemap"] = False  # thin page: keep it reachable but out of the sitemap
    if profile_redirects.get(g["id"]):
        fm["redirect_from"] = profile_redirects[g["id"]]
        fm.pop("sitemap", None)
    neighbours = [n for n in by_county.get(g["county"], []) if n["id"] != g["id"]][:8]
    fm["nearby"] = [{"name": n["name"], "url": n["url"], "type": n["type"]} for n in neighbours]
    with open(os.path.join(grower_dir, f"{g['id']}.md"), "w", encoding="utf-8") as f:
        f.write("---\n# Generated by scripts/build_data.py - do not edit.\n")
        for k, v in fm.items():
            f.write(f"{k}: {yaml_val(v)}\n")
        f.write("---\n")

print(f"grower pages: {len(growers)} ({len(ranked)} with auction sales)")
print(f"growers: {len(growers)} ({sum(g['mapped'] for g in growers)} mapped), map points: {len(features)}")
print(f"dealers: {len(dealers)} in {len(dealer_groups)} groups")
print(f"sales: {len(sale_rows)} ({sale_rows[0]['date']} to {sale_rows[-1]['date']}), seasons: {len(seasons)}, buyers: {len(buyers)}")
