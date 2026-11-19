---
layout: base
hero: true
title: "Coffee brokers in Kenya: marketing agents at the Nairobi Coffee Exchange"
heading: Coffee brokers in Kenya
description: "The coffee brokers (marketing agents) that sell growers' coffee at the Nairobi Coffee Exchange: volumes, growers served, counties and the prices they achieve compared with the same grade at the same sale."
lead: "Brokers take a cooperative's or estate's coffee to the weekly auction. Compare them by the growers they serve and the prices their coffee fetches."
breadcrumbs:
  - title: Directory
    url: /directory.html
permalink: /directory/coffee-brokers.html
---
{% assign B = site.data.brokers %}
<section class="mk-section">
  <div class="container">
    <div class="mk-prose mb-4">
      <p>Under the Coffee Act, 2026 and the Capital Markets (Coffee Exchange) Regulations, 2020, growers sell at the Nairobi Coffee Exchange through a <strong>coffee broker</strong> licensed by the Capital Markets Authority (CMA). The broker catalogues the coffee, offers it at the weekly auction and passes on the proceeds. Many brokers were licensed earlier as <a href="/directory/marketing-agents.html">commercial marketing agents</a>.</p>
      <p>From {{ B.first_sale | date: "%B %Y" }} to {{ B.last_sale | date: "%B %Y" }}, {{ B.brokers.size }} brokers offered coffee at the auction. <strong>vs market</strong> compares the prices a broker's lots fetched with the average for the same grade at the same sale: it reflects the quality of the coffee the broker brings and the buyers it attracts, not a fee. Brokers do not set prices; buyers bid for each lot.</p>
    </div>

    <div class="mk-table-wrap mb-4">
      <table class="mk-table">
        <caption>Coffee brokers at the Nairobi Coffee Exchange, {{ B.first_sale | date: "%B %Y" }} to {{ B.last_sale | date: "%B %Y" }}, by tonnes sold</caption>
        <thead><tr><th scope="col">Broker</th><th scope="col" class="num">Lots</th><th scope="col" class="num">Tonnes</th><th scope="col" class="num">Share {{ B.season }}</th><th scope="col" class="num">Growers</th><th scope="col" class="num">Avg price (US$/50 kg)</th><th scope="col" class="num">vs market</th><th scope="col">Main counties</th><th scope="col">CMA licence</th></tr></thead>
        <tbody>
          {% for b in B.brokers %}
          <tr>
            <th scope="row"><a href="#{{ b.slug }}">{{ b.name }}</a></th>
            <td class="num">{% include num.html n=b.lots %}</td>
            <td class="num">{% include num.html n=b.tonnes %}</td>
            <td class="num">{% if b.season_share %}{{ b.season_share }}%{% else %}–{% endif %}</td>
            <td class="num">{{ b.growers }}</td>
            <td class="num">{{ b.price | round }}</td>
            <td class="num">{% if b.vs_market > 0 %}+{% endif %}{{ b.vs_market }}%</td>
            <td>{{ b.counties | slice: 0, 2 | join: ", " }}</td>
            <td>{% if b.cma_licence != "" %}{{ b.cma_licence }}{% else %}<span class="text-muted">to confirm</span>{% endif %}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    <p class="mk-note">Prices are volume-weighted, in US dollars per 50 kg bag of clean coffee. Growers = named cooperatives, factories and estates; bulk lots pooled from several growers are counted in the totals only. Source: Nairobi Coffee Exchange transaction listings, compiled by MyKahawa.</p>
  </div>
</section>

<section class="mk-section mk-section-alt">
  <div class="container">
    <h2>Growers by broker</h2>
    <p>The growers whose coffee each broker sold in the largest volumes. Open a grower's page for every lot and its price against the same grade.</p>
    <div class="row">
      {% for b in B.brokers %}
      <div class="col-lg-6 mb-4">
        <div class="mk-chart-card h-100" id="{{ b.slug }}">
          <h3 class="h4">{{ b.name }}</h3>
          <p class="mk-note mb-2">{% include num.html n=b.tonnes %} tonnes in {% include num.html n=b.lots %} lots, {{ b.first_sale | date: "%b %Y" }} to {{ b.last_sale | date: "%b %Y" }} · {{ b.growers }} growers{% if b.bulk_share > 0 %} · {{ b.bulk_share }}% bulk{% endif %}{% if b.cma_licence != "" %} · CMA licence {{ b.cma_licence }}{% endif %}{% if b.website != "" %} · <a href="{{ b.website }}" rel="noopener" target="_blank">website<span class="sr-only"> (opens in a new tab)</span></a>{% endif %}</p>
          {% if b.top_growers.size > 0 %}
          <ol class="mk-ranked mb-0">
            {% for g in b.top_growers limit: 6 %}
            <li><a href="{{ g.url }}">{{ g.name }}</a>{% if g.county != "" %} <span class="text-muted small">{{ g.county }}</span>{% endif %} <span class="mk-ranked-value">{{ g.tonnes | round }} t</span></li>
            {% endfor %}
          </ol>
          {% endif %}
        </div>
      </div>
      {% endfor %}
    </div>
    <p class="mk-note">Are you a broker listed here, or missing? Send corrections and your CMA licence number to <a href="mailto:info@mykahawa.org">info@mykahawa.org</a>.</p>
  </div>
</section>
