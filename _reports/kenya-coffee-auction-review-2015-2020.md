---
layout: report
title: "Kenya coffee auction review 2015–2020: prices, volumes and grade premiums"
heading: "Kenya coffee auction review, 2015–2020"
description: "Six seasons of Nairobi Coffee Exchange results: how Kenyan coffee prices and volumes moved, the widening premium for AA, seasonal price swings, and what it means for growers and buyers."
lead: "Six seasons of Nairobi Coffee Exchange results show prices peaking in 2016/17, collapsing in 2018/19 and recovering in 2019/20, while the premium for top grades widened sharply."
date: 2026-11-10
---
{% assign m = site.data.market %}{% assign ins = site.data.insights %}
{% assign s1617 = m.seasons | where: "season", "2016/17" | first %}{% assign s1819 = m.seasons | where: "season", "2018/19" | first %}{% assign s1920 = m.seasons | where: "season", "2019/20" | first %}{% assign s1516 = m.seasons | where: "season", "2015/16" | first %}
{% assign p1 = ins.premiums | where: "season", "2015/16" | first %}{% assign p2 = ins.premiums | where: "season", "2019/20" | first %}

## Key findings

<ul class="mk-findings">
<li>Between {{ m.first_sale | date: "%B %Y" }} and {{ m.last_sale | date: "%B %Y" }}, the Nairobi Coffee Exchange sold <strong>{% include num.html n=m.tonnes %} tonnes</strong> of clean coffee for <strong>US${{ m.usd | divided_by: 1000000 }} million</strong>, at an average of <strong>US${{ m.price | round }}</strong> per 50 kg bag.</li>
<li>Prices peaked in <strong>2016/17 (US${{ s1617.price | round }})</strong> and fell to <strong>US${{ s1819.price | round }} in 2018/19</strong>, the lowest season average in the period, before recovering to US${{ s1920.price | round }} in 2019/20.</li>
<li>Volumes swung between <strong>{% include num.html n=s1516.tonnes %} tonnes (2015/16)</strong> and <strong>{% include num.html n=s1920.tonnes %} tonnes (2019/20)</strong>. The value of coffee sold fell from US${{ s1617.usd | divided_by: 1000000 }} million in 2016/17 to US${{ s1920.usd | divided_by: 1000000 }} million in 2019/20.</li>
<li>The <strong>premium for AA over AB widened</strong> from {{ p1.aa_over_ab }}% in 2015/16 to {{ p2.aa_over_ab }}% in 2019/20. When prices fell, the lower grades lost the most.</li>
<li>Prices follow a clear <strong>seasonal pattern</strong>: in five of six seasons the best sale average came in January or February, and in every season the lowest came between April and June.</li>
<li><strong>{{ ins.bulk_share }}% of the volume</strong> was sold as bulked lots that mix several growers' coffee, so it cannot be traced to a single factory or estate.</li>
</ul>

## Prices and volumes by season

<div class="mk-table-wrap">
<table class="mk-table">
<caption>Nairobi Coffee Exchange results by coffee season</caption>
<thead><tr><th scope="col">Season</th><th scope="col" class="num">Auctions</th><th scope="col" class="num">Tonnes sold</th><th scope="col" class="num">Value (US$ m)</th><th scope="col">Avg price (US$/50 kg)</th></tr></thead>
<tbody>
{% for s in m.seasons %}
<tr><th scope="row">{{ s.season }}{% if forloop.first %}*{% endif %}</th><td class="num">{{ s.sales }}</td><td class="num">{% include num.html n=s.tonnes %}</td><td class="num">{{ s.usd | divided_by: 100000.0 | round | divided_by: 10.0 }}</td>
<td><span class="mk-bar"><span class="mk-bar-fill" style="width:{{ s.price | divided_by: 3.0 | round }}px" aria-hidden="true"></span>{{ s.price | round }}</span></td></tr>
{% endfor %}
</tbody>
</table>
</div>
<p class="mk-note">* Partial season: records start on {{ m.first_sale | date: "%-d %B %Y" }}.</p>

Prices at the Nairobi auction broadly follow world Arabica prices, but quality drives most of the variation. In 2018/19 world coffee prices hit multi-year lows, and Kenyan averages fell by more than a third from their 2016/17 peak. Volumes do not simply follow price. They depend on the size of each harvest, and on how much coffee goes through direct sales instead of the auction.

## Top grades pulled away from the rest

The gap between the grades widened sharply after 2016/17. AA held its value much better than AB and C. For growers, this makes quality (picking ripe cherry, careful processing and grading) worth more than ever.

<div class="mk-table-wrap">
<table class="mk-table">
<caption>Average price of the main grades and the AA and AB premiums, US$ per 50 kg bag</caption>
<thead><tr><th scope="col">Season</th><th scope="col" class="num">AA</th><th scope="col" class="num">AB</th><th scope="col" class="num">C</th><th scope="col" class="num">AA over AB</th><th scope="col" class="num">AB over C</th></tr></thead>
<tbody>
{% for p in ins.premiums %}
<tr><th scope="row">{{ p.season }}</th><td class="num">{{ p.aa | round }}</td><td class="num">{{ p.ab | round }}</td><td class="num">{{ p.c | round }}</td><td class="num">+{{ p.aa_over_ab }}%</td><td class="num">+{{ p.ab_over_c }}%</td></tr>
{% endfor %}
</tbody>
</table>
</div>

See the [guide to Kenyan coffee grades](/projects/kenya-coffee-grades.html) for what each grade means.

## When to sell: prices swing within each season

The average price at individual auctions varies a lot within a season. The early-season sales in January and February, which carry the best main-crop coffee, usually fetch the highest averages. The April–June sales, with more fly-crop and lower-grade lots, fetch the lowest. Part of this is the grade mix rather than the market itself, but it matters for when cooperatives offer their best lots.

<div class="mk-table-wrap">
<table class="mk-table">
<caption>Lowest and highest auction averages in each season, US$ per 50 kg bag</caption>
<thead><tr><th scope="col">Season</th><th scope="col" class="num">Lowest sale</th><th scope="col">Date</th><th scope="col" class="num">Highest sale</th><th scope="col">Date</th></tr></thead>
<tbody>
{% for s in ins.swings %}
<tr><th scope="row">{{ s.season }}</th><td class="num">{{ s.low | round }}</td><td>{{ s.low_date | date: "%-d %b %Y" }}</td><td class="num">{{ s.high | round }}</td><td>{{ s.high_date | date: "%-d %b %Y" }}</td></tr>
{% endfor %}
</tbody>
</table>
</div>

## What it means

- **For growers and cooperatives:** grade mix explains a large part of the price gap between growers. Raising the share of AA and AB, and reducing mbuni and ungraded coffee, has the biggest effect on income. Compare your own results on your [grower page](/growers.html).
- **For buyers:** early-season auctions carry the best lots and the strongest competition. Later sales can offer value in AB and PB.
- **For policymakers:** most coffee still sold as anonymous bulk lots reduces traceability, at a time when buyers and the EU deforestation rules increasingly demand it.

Explore the full data on the [prices page](/transactions.html), and read the companion reports on [prices by county](/reports/kenya-coffee-prices-by-county/) and [buyer concentration](/reports/who-buys-kenyan-coffee/).
