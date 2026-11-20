---
layout: base
hero: true
title: "Coffee price per kg in Kenya: Nairobi Coffee Exchange prices by grade, county and cooperative"
heading: Coffee prices per kg in Kenya
description: "How much is a kg of coffee in Kenya? Latest Nairobi Coffee Exchange price per kg and per 50 kg bag, prices by grade (AA, AB, PB, C), by county, and the average price per kg of every cooperative, factory and estate over the last 12 months."
lead: "What a kilo of Kenyan coffee fetches at the Nairobi Coffee Exchange, updated after every weekly sale: by grade, by county, and for each cooperative, factory and estate."
permalink: /coffee-prices-per-kg.html
extra_js:
  - /theme/js/table-filter.js
---
{% assign L = site.data.latest %}{% assign K = site.data.prices_kg %}
<section class="mk-section">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 mk-prose">
        <h2 id="price-per-kg">How much is a kg of coffee in Kenya?</h2>
        <p class="lead">At the latest Nairobi Coffee Exchange auction (Sale {{ L.sale }}, {{ L.date | date: "%-d %B %Y" }}), Kenyan coffee sold for an average of <strong>US${{ L.price | divided_by: 50.0 | round: 2 }} per kg</strong>, or US${{ L.price | round }} per 50 kg bag.</p>
        <p>Over the last 12 months ({{ K.from | date: "%B %Y" }} to {{ K.to | date: "%B %Y" }}, {{ K.sales }} sales, {% include num.html n=K.tonnes %} tonnes), the average was <strong>US${{ K.kg }} per kg</strong> (US${{ K.bag | round }} per 50 kg bag). The top grades fetch more: AA averaged US${% assign aa = K.grades | where: "grade", "AA" | first %}{{ aa.kg }} per kg and AB US${% assign ab = K.grades | where: "grade", "AB" | first %}{{ ab.kg }} per kg.</p>
        <p class="mk-note"><strong>What this price is:</strong> the auction price of <em>clean coffee</em> (green beans, hulled and graded), paid by exporters at the Nairobi Coffee Exchange. It is not what farmers are paid per kg of cherry, which comes after milling, marketing and cooperative costs, and it is not the price of roasted coffee in shops. The NCE quotes prices in US dollars per 50 kg bag; per kg = per bag ÷ 50.</p>
      </div>
      <div class="col-lg-4">
        <div class="mk-stats">
          <div class="mk-stat"><span class="mk-stat-value">US${{ L.price | divided_by: 50.0 | round: 2 }}</span><span class="mk-stat-label">per kg at the latest sale (US${{ L.price | round }} per 50 kg bag)</span></div>
          <div class="mk-stat"><span class="mk-stat-value">US${{ K.kg }}</span><span class="mk-stat-label">per kg, average of the last 12 months (US${{ K.bag | round }} per bag)</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="mk-section mk-section-alt">
  <div class="container">
    <h2 id="by-grade">Coffee price per kg by grade</h2>
    <p>Kenyan coffee is sold by grade: bean size, shape and quality. <a href="/projects/kenya-coffee-grades.html">What the grades mean</a>.</p>
    <div class="mk-table-wrap bg-white mb-2">
      <table class="mk-table">
        <caption>Average auction price by grade, US$ per kg and per 50 kg bag of clean coffee</caption>
        <thead><tr><th scope="col">Grade</th><th scope="col" class="num">Latest sale, US$/kg</th><th scope="col" class="num">Latest sale, US$/bag</th><th scope="col" class="num">12 months, US$/kg</th><th scope="col" class="num">12 months, US$/bag</th><th scope="col" class="num">Range, US$/kg</th><th scope="col" class="num">Tonnes (12 months)</th></tr></thead>
        <tbody>
          {% for g in K.grades %}{% assign lg = L.grades | where: "grade", g.grade | first %}
          <tr>
            <th scope="row"><a href="/projects/kenya-coffee-grades.html">{{ g.grade }}</a></th>
            <td class="num">{% if lg %}<strong>{{ lg.price | divided_by: 50.0 | round: 2 }}</strong>{% else %}–{% endif %}</td>
            <td class="num">{% if lg %}{{ lg.price | round }}{% else %}–{% endif %}</td>
            <td class="num"><strong>{{ g.kg }}</strong></td>
            <td class="num">{{ g.bag | round }}</td>
            <td class="num">{{ g.low }}–{{ g.high }}</td>
            <td class="num">{% include num.html n=g.tonnes %}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    <p class="mk-note">Latest sale: Sale {{ L.sale }} of {{ L.date | date: "%-d %B %Y" }}. Range = lowest and highest lot price over the 12 months. See <a href="/transactions.html">prices over time</a>.</p>
  </div>
</section>

<section class="mk-section">
  <div class="container">
    <h2 id="by-county">Coffee sold and price per kg by county</h2>
    <p>Coffee sold at the auction over the last 12 months by the county of the grower, with the average price per kg. Only lots that MyKahawa could link to a named cooperative, factory or estate are counted ({{ K.named_share }}% of the volume), so the tonnes show auction sales, not total production.</p>
    <div class="mk-table-wrap mb-2">
      <table class="mk-table">
        <caption>Auction sales by county, {{ K.from | date: "%B %Y" }} to {{ K.to | date: "%B %Y" }} (counties with at least 10 tonnes)</caption>
        <thead><tr><th scope="col">County</th><th scope="col" class="num">Tonnes</th><th scope="col" class="num">Growers</th><th scope="col" class="num">US$/kg</th><th scope="col" class="num">US$/bag</th><th scope="col" class="num">AA, US$/kg</th><th scope="col" class="num">AB, US$/kg</th></tr></thead>
        <tbody>
          {% for c in K.counties %}
          <tr>
            <th scope="row"><a href="/directory/county/{{ c.slug }}.html">{{ c.county }}</a></th>
            <td class="num">{% include num.html n=c.tonnes %}</td>
            <td class="num">{{ c.growers }}</td>
            <td class="num"><strong>{{ c.kg }}</strong></td>
            <td class="num">{{ c.bag | round }}</td>
            <td class="num">{% if c.aa %}{{ c.aa }}{% else %}–{% endif %}</td>
            <td class="num">{% if c.ab %}{{ c.ab }}{% else %}–{% endif %}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    <p class="mk-note">A county's average depends on its grade mix; compare AA with AA and AB with AB.</p>
  </div>
</section>

<section class="mk-section mk-section-alt">
  <div class="container">
    <h2 id="by-grower">Average price per kg by cooperative, factory and estate</h2>
    <p>Every grower that sold at least one tonne at the auction in the last 12 months. <strong>vs market</strong> compares each grower's lots with the average for the same grade at the same sale, so a different grade mix does not distort it. Open a grower for every lot.</p>
    <div class="form-group" style="max-width:28rem">
      <label for="kg-filter">Find a cooperative, factory, estate or county</label>
      <input type="search" id="kg-filter" class="form-control" data-filter-table="kg-table" data-filter-count="kg-count" data-filter-noun="growers" placeholder="Type a name or county…" autocomplete="off">
      <p id="kg-count" class="mk-note mt-1 mb-0" aria-live="polite"></p>
    </div>
    <div class="mk-table-wrap bg-white mb-2">
      <table class="mk-table" id="kg-table">
        <caption>Average auction price per grower, {{ K.from | date: "%B %Y" }} to {{ K.to | date: "%B %Y" }}, US$ per kg and per 50 kg bag</caption>
        <thead><tr><th scope="col">Grower</th><th scope="col">County</th><th scope="col" class="num">Tonnes</th><th scope="col" class="num">US$/kg</th><th scope="col" class="num">US$/bag</th><th scope="col" class="num">AA, US$/kg</th><th scope="col" class="num">AB, US$/kg</th><th scope="col" class="num">vs market</th></tr></thead>
        <tbody>
          {% for g in K.growers %}
          <tr>
            <td><a href="{{ g.url }}">{{ g.name }}</a> <span class="text-muted small">{{ g.type }}</span></td>
            <td>{{ g.county }}</td>
            <td class="num">{{ g.tonnes }}</td>
            <td class="num"><strong>{{ g.kg }}</strong></td>
            <td class="num">{{ g.bag | round }}</td>
            <td class="num">{% if g.aa %}{{ g.aa }}{% else %}–{% endif %}</td>
            <td class="num">{% if g.ab %}{{ g.ab }}{% else %}–{% endif %}</td>
            <td class="num">{% if g.vs_market > 0 %}+{% endif %}{{ g.vs_market }}%</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    <p class="mk-note">Source: Nairobi Coffee Exchange transaction listings, compiled by MyKahawa. Prices are volume-weighted. Bulk lots pooled from several growers are not included in grower or county figures. Is your cooperative missing or wrong? <a href="mailto:info@mykahawa.org">Tell us</a>.</p>
  </div>
</section>
