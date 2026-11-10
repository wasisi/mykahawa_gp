---
layout: report
title: "Who buys Kenyan coffee? Buyer concentration at the Nairobi Coffee Exchange"
heading: "Who buys Kenyan coffee? Buyer concentration at the auction"
description: "The biggest buyers of Kenyan coffee at the Nairobi Coffee Exchange, their market shares and the prices they pay, and how concentrated the buying side of the auction became between 2015 and 2020."
lead: "A handful of exporters buy most of Kenya's auction coffee, and their combined share grew between 2015 and 2020. Their average prices show very different strategies."
date: 2026-11-10
---
{% assign m = site.data.market %}{% assign ins = site.data.insights %}
{% assign c0 = ins.concentration | first %}{% assign cmax = ins.concentration | sort: "top4" | last %}{% assign clast = ins.concentration | last %}
{% assign b = m.top_buyers %}

## Key findings

<ul class="mk-findings">
<li><strong>{{ m.buyer_count }} buyers</strong> bought coffee at the auction between {{ m.first_sale | date: "%B %Y" }} and {{ m.last_sale | date: "%B %Y" }}, but typically only around 45–55 were active in any one season.</li>
<li>The four largest buyers, <strong>{{ b[0].name }}, {{ b[1].name }}, {{ b[2].name }} and {{ b[3].name }}</strong>, together bought <strong>{{ b[0].share | plus: b[1].share | plus: b[2].share | plus: b[3].share | round }}%</strong> of all coffee sold.</li>
<li>Concentration rose: the top four's share grew from <strong>{{ c0.top4 | round }}% in {{ c0.season }}</strong> to <strong>{{ cmax.top4 | round }}% in {{ cmax.season }}</strong> ({{ clast.top4 | round }}% in {{ clast.season }}).</li>
<li>Average prices paid range from about <strong>US${% assign lowp = b | slice: 0, 10 | sort: "price" | first %}{{ lowp.price | round }}</strong> to <strong>US${% assign highp = b | slice: 0, 10 | sort: "price" | last %}{{ highp.price | round }}</strong> per bag among the top ten. This reflects buyers specialising in different grades and markets, from mass-market blends to specialty AA.</li>
</ul>

## The biggest buyers

{% include top-buyers.html limit=20 %}

A buyer's average price says more about *what* it buys than about how generously it pays. Buyers with high averages, such as {{ highp.name }}, focus on top grades for specialty roasters. Those with low averages buy large volumes of lower grades (mbuni, ungraded and T) for blends.

## Concentration over time

<div class="mk-table-wrap">
<table class="mk-table">
<caption>Buyer concentration by coffee season</caption>
<thead><tr><th scope="col">Season</th><th scope="col" class="num">Active buyers</th><th scope="col">Top 4 share of volume</th><th scope="col" class="num">HHI</th></tr></thead>
<tbody>
{% for c in ins.concentration %}
<tr><th scope="row">{{ c.season }}</th><td class="num">{{ c.buyers }}</td><td><span class="mk-bar"><span class="mk-bar-fill" style="width:{{ c.top4 | times: 2 | round }}px" aria-hidden="true"></span>{{ c.top4 }}%</span></td><td class="num">{% include num.html n=c.hhi %}</td></tr>
{% endfor %}
</tbody>
</table>
</div>

The **Herfindahl-Hirschman Index (HHI)** adds up the squared market shares of all buyers. It ranges from close to 0 (many small buyers) to 10,000 (a single buyer). It rose from {% include num.html n=c0.hhi %} to {% include num.html n=cmax.hhi %} over the period. That is still a market with real competition, but one where the largest exporters carry growing weight in price discovery.

## Why it matters

- **For growers:** when fewer buyers compete for a lot, prices are more exposed to the strategies of a few firms. Direct sales, and selling more top grades that attract specialty buyers, widen the pool of bidders.
- **For buyers:** smaller and newer exporters can find opportunity in grades and marks that the largest buyers do not target.
- **For regulators:** the 2019 Regulations separate buying from milling and marketing, banning cross-ownership and shared directorships. Monitoring concentration on the buying side complements those rules. See [Kenya coffee laws](/projects/kenya-coffee-laws.html).

See all [licensed exporters and dealers](/directory/coffee-exporters.html), and read the [auction review](/reports/kenya-coffee-auction-review-2015-2020/) and [prices by county](/reports/kenya-coffee-prices-by-county/).
