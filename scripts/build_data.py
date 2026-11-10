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


def clean(s):
    if s is None:
        return ""
    s = s.replace("\xa0", " ").strip()
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
        if not name:
            continue
        lat, lon = num(r["lat"]), num(r["lon"])
        growers.append({
            "id": int(r["id"]),
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
    {"i": g["id"], "c": g["code"], "n": g["name"], "t": g["type"], "k": g["county"], "a": g["affiliation"], "m": int(g["mapped"])}
    for g in growers
], compact=True)
write_json(os.path.join(JDATA, "growers.json"), growers, compact=True)

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
with open(os.path.join(DATA, "dealers/coffeedealers.csv"), encoding="latin-1") as f:
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

with open(os.path.join(DATA, "transactions/coffeetransactions.csv"), encoding="latin-1") as f:
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
        mark = clean(r["producer_name"])
        if mark:
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

print(f"growers: {len(growers)} ({sum(g['mapped'] for g in growers)} mapped), map points: {len(features)}")
print(f"dealers: {len(dealers)} in {len(dealer_groups)} groups")
print(f"sales: {len(sale_rows)} ({sale_rows[0]['date']} to {sale_rows[-1]['date']}), seasons: {len(seasons)}, buyers: {len(buyers)}")
