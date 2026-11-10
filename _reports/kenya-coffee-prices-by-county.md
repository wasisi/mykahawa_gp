---
layout: report
title: "Kenya coffee prices by county: where the best-paid coffee comes from"
heading: "Kenya coffee prices by county and grower type"
description: "Which Kenyan counties and growers earn the most per bag of coffee at the Nairobi Coffee Exchange: average prices by county, AA and AB prices, cooperatives vs estates, and the best-paid AA producers."
lead: "Coffee from Kirinyaga earns the highest average price at the auction, followed by Embu, Bungoma and Murang'a. Cooperative factories out-earn estates on average, largely because they sell more top grades."
date: 2026-11-10
---
{% assign m = site.data.market %}{% assign ins = site.data.insights %}
{% assign big = ins.counties | where_exp: "c", "c.tonnes >= 2000" %}
{% assign by_price = big | sort: "price" | reverse %}
{% assign best = by_price | first %}{% assign worst = by_price | last %}
{% assign kiambu = ins.counties | where: "county", "Kiambu" | first %}
{% assign fac = ins.types | where: "type", "Factory" | first %}{% assign est = ins.types | where: "type", "Estate" | first %}

## Key findings

<ul class="mk-findings">
<li>Among the main coffee counties (over 2,000 tonnes sold), <strong>{{ best.county }}</strong> earned the highest average price, <strong>US${{ best.price | round }}</strong> per 50 kg bag, against <strong>US${{ worst.price | round }} in {{ worst.county }}</strong>. The market average was US${{ m.price | round }}.</li>
<li>The gap holds grade for grade: {{ best.county }} AA averaged US${{ best.aa | round }}, compared with US${{ worst.aa | round }} for AA from {{ worst.county }}. Origin and cup quality matter, not just bean size.</li>
<li><strong>Kiambu</strong> sold the most coffee ({% include num.html n=kiambu.tonnes %} tonnes), much of it from large estates, at an average close to the market (US${{ kiambu.price | round }}).</li>
<li>Coffee from <strong>cooperative factories averaged US${{ fac.price | round }}</strong>, above <strong>estates at US${{ est.price | round }}</strong>. {{ fac.top_share }}% of factory volume was top grades (E, AA, AB, PB), against {{ est.top_share }}% for estates.</li>
<li>The best-paid AA came almost entirely from cooperative factories and societies in <strong>Kirinyaga, Nyeri and Kiambu</strong>.</li>
</ul>

## Prices by county

<div class="mk-table-wrap">
<table class="mk-table">
<caption>Auction results by county of the grower, {{ m.first_sale | date: "%Y" }}–{{ m.last_sale | date: "%Y" }}. Prices in US$ per 50 kg bag.</caption>
<thead><tr><th scope="col">County</th><th scope="col" class="num">Growers selling</th><th scope="col" class="num">Tonnes</th><th scope="col">Avg price</th><th scope="col" class="num">AA</th><th scope="col" class="num">AB</th><th scope="col" class="num">Top grades share</th></tr></thead>
<tbody>
{% for c in ins.counties %}
<tr>
<th scope="row"><a href="/directory/county/{{ c.slug }}.html">{{ c.county }}</a></th>
<td class="num">{{ c.growers }}</td>
<td class="num">{% include num.html n=c.tonnes %}</td>
<td><span class="mk-bar"><span class="mk-bar-fill" style="width:{{ c.price | divided_by: 3.0 | round }}px" aria-hidden="true"></span>{{ c.price | round }}</span></td>
<td class="num">{% if c.aa %}{{ c.aa | round }}{% else %}–{% endif %}</td>
<td class="num">{% if c.ab %}{{ c.ab | round }}{% else %}–{% endif %}</td>
<td class="num">{{ c.top_share }}%</td>
</tr>
{% endfor %}
</tbody>
</table>
</div>
<p class="mk-note">"Top grades share" is the share of a county's volume sold as E, AA, AB or PB. Counties with small volumes can swing a lot from a handful of lots. {{ ins.bulk_share }}% of all coffee was sold in bulked lots that mix several growers and is not included in the county figures.</p>

## Cooperatives and estates

<div class="mk-table-wrap">
<table class="mk-table">
<caption>Auction results by type of grower, US$ per 50 kg bag</caption>
<thead><tr><th scope="col">Grower type</th><th scope="col" class="num">Growers selling</th><th scope="col" class="num">Tonnes</th><th scope="col" class="num">Avg price</th><th scope="col" class="num">AA</th><th scope="col" class="num">AB</th><th scope="col" class="num">C</th><th scope="col" class="num">Top grades share</th></tr></thead>
<tbody>
{% for t in ins.types %}
<tr><th scope="row">{{ t.plural }}</th><td class="num">{{ t.growers }}</td><td class="num">{% include num.html n=t.tonnes %}</td><td class="num">{{ t.price | round }}</td><td class="num">{{ t.aa | round }}</td><td class="num">{{ t.ab | round }}</td><td class="num">{{ t.c | round }}</td><td class="num">{{ t.top_share }}%</td></tr>
{% endfor %}
</tbody>
</table>
</div>

Factories (the cooperative wet mills where smallholders deliver cherry) sell under their own marks, and many have built reputations with specialty buyers. Estates sell larger volumes, often with a wider grade mix. The difference in average price comes partly from grade mix, and partly from a premium for the best-known factory marks.

## The best-paid AA producers

Growers that sold at least 20 tonnes of AA, ranked by their average AA price:

<div class="mk-table-wrap">
<table class="mk-table">
<caption>Highest average AA prices, US$ per 50 kg bag (minimum 20 tonnes of AA sold)</caption>
<thead><tr><th scope="col">#</th><th scope="col">Grower</th><th scope="col">County</th><th scope="col" class="num">AA tonnes</th><th scope="col" class="num">AA avg price</th></tr></thead>
<tbody>
{% for g in ins.aa_leaders %}
<tr><td>{{ forloop.index }}</td><td><a href="{{ g.url }}">{{ g.name }}</a></td><td>{{ g.county }}</td><td class="num">{{ g.tonnes }}</td><td class="num">{{ g.price | round }}</td></tr>
{% endfor %}
</tbody>
</table>
</div>

The market average for AA over the period was US${% assign aa = m.grades | where: "grade", "AA" | first %}{{ aa.price | round }}. The best-paid grower earned roughly {{ ins.aa_leaders[0].price | divided_by: aa.price | times: 10 | round | divided_by: 10.0 }} times that.

## What it means

- **For cooperatives:** the price gap between neighbouring factories shows that processing and quality control, not location alone, drive earnings. Benchmark against the leaders in your county on the [county pages](/directory.html#counties).
- **For buyers and roasters:** counties such as Kirinyaga, Embu and Nyeri consistently deliver top-priced AA. Many smaller counties offer good value at lower prices.
- **For county governments:** extension services and investment in factory processing can raise the share of top grades. That share is the biggest single driver of average price.

Look up any grower's grade-by-grade prices in the [growers directory](/growers.html), and read the [auction review](/reports/kenya-coffee-auction-review-2015-2020/) and the [buyers report](/reports/who-buys-kenyan-coffee/).
