---
layout: base
hero: true
title: "Kenya coffee prices: Nairobi Coffee Exchange auction results 2015–2020"
heading: Kenya coffee auction prices
description: "Kenyan coffee prices at the Nairobi Coffee Exchange, 2015–2020: average price per sale, prices by grade (AA, AB, PB, C), volumes, values and top buyers. Free data download."
lead: "Prices, volumes and buyers at the Nairobi Coffee Exchange, from 131,000 auction lots sold between January 2015 and September 2020."
redirect_from:
  - "/analytics/dashboard/"
  - "/transactions/list/"
extra_js:
  - /theme/vendor/chartjs/chart.umd.min.js
  - /theme/js/market-charts.js
---
{% assign m = site.data.market %}
<section class="mk-section">
  <div class="container">
    <div class="mk-stats mb-4">
      <div class="mk-stat"><span class="mk-stat-value">US${{ m.price | round }}</span><span class="mk-stat-label">average price per 50 kg bag</span></div>
      <div class="mk-stat"><span class="mk-stat-value">{% include num.html n=m.tonnes %} t</span><span class="mk-stat-label">coffee sold</span></div>
      <div class="mk-stat"><span class="mk-stat-value">US${{ m.usd | divided_by: 1000000 }}m</span><span class="mk-stat-label">total value</span></div>
      <div class="mk-stat"><span class="mk-stat-value">{{ m.sales }}</span><span class="mk-stat-label">weekly auctions</span></div>
      <div class="mk-stat"><span class="mk-stat-value">{% include num.html n=m.lots %}</span><span class="mk-stat-label">lots sold</span></div>
    </div>

    <div class="mk-chart-card">
      <h2 id="price">Average price at each auction</h2>
      <p class="mk-note">Average price per sale in US dollars per 50 kg bag of clean coffee, weighted by volume. Hover to see each sale.</p>
      <div class="mk-chart"><canvas id="chart-price" role="img" aria-label="Line chart of the average auction price per sale, {{ m.first_sale | date: '%B %Y' }} to {{ m.last_sale | date: '%B %Y' }}. Season averages are in the table below."></canvas></div>
    </div>

    <div class="mk-chart-card">
      <h2 id="grades">Prices by grade</h2>
      <p class="mk-note">Average price of the four main grades in each coffee season (October to September), US$ per 50 kg bag. AA and AB are the large-bean grades that Kenya is known for. PB is peaberry. Learn more about <a href="/projects/kenya-coffee-grades.html">Kenyan coffee grades</a>.</p>
      <div class="mk-chart"><canvas id="chart-grades" role="img" aria-label="Line chart of average price by grade (AA, AB, PB, C) per season. Exact values are in the table below."></canvas></div>
      <div class="mk-table-wrap mt-3">
        <table class="mk-table">
          <caption>Average price by grade and season, US$ per 50 kg bag</caption>
          <thead><tr><th scope="col">Grade</th>{% for s in m.seasons %}<th scope="col" class="num">{{ s.season }}</th>{% endfor %}<th scope="col" class="num">All seasons</th><th scope="col" class="num">Tonnes sold</th></tr></thead>
          <tbody>
            {% for g in m.grades %}{% if g.tonnes >= 400 %}
            <tr>
              <th scope="row">{{ g.grade }}</th>
              {% for s in m.seasons %}{% assign v = g.by_season[s.season] %}<td class="num">{% if v %}{{ v | round }}{% else %}–{% endif %}</td>{% endfor %}
              <td class="num"><strong>{{ g.price | round }}</strong></td>
              <td class="num">{% include num.html n=g.tonnes %}</td>
            </tr>
            {% endif %}{% endfor %}
          </tbody>
        </table>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-6">
        <div class="mk-chart-card">
          <h2 id="volume" class="h3">Volume sold by season</h2>
          <div class="mk-chart" style="height:16rem"><canvas id="chart-volume" role="img" aria-label="Bar chart of tonnes sold per season. Values are in the table below."></canvas></div>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="mk-chart-card">
          <h2 id="value" class="h3">Value of sales by season</h2>
          <div class="mk-chart" style="height:16rem"><canvas id="chart-value" role="img" aria-label="Bar chart of the value of coffee sold per season in US dollars. Values are in the table below."></canvas></div>
        </div>
      </div>
    </div>

    <div class="mk-table-wrap mb-2">
      <table class="mk-table">
        <caption>Nairobi Coffee Exchange results by coffee season</caption>
        <thead><tr><th scope="col">Season</th><th scope="col" class="num">Auctions</th><th scope="col" class="num">Lots sold</th><th scope="col" class="num">Tonnes</th><th scope="col" class="num">Value (US$ m)</th><th scope="col" class="num">Avg price (US$/50 kg)</th></tr></thead>
        <tbody>
          {% for s in m.seasons %}
          <tr>
            <th scope="row">{{ s.season }}{% if forloop.first %}*{% endif %}</th>
            <td class="num">{{ s.sales }}</td>
            <td class="num">{% include num.html n=s.lots %}</td>
            <td class="num">{% include num.html n=s.tonnes %}</td>
            <td class="num">{{ s.usd | divided_by: 100000.0 | round | divided_by: 10.0 }}</td>
            <td class="num">{{ s.price | round }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    <p class="mk-note">* The 2014/15 season is partial: records start on {{ m.first_sale | date: "%-d %B %Y" }}.</p>
  </div>
</section>

<section class="mk-section mk-section-alt">
  <div class="container">
    <div class="row">
      <div class="col-lg-6 mb-4">
        <h2 id="buyers">Top buyers</h2>
        <p>The largest buyers at the auction by volume. <a href="/directory/coffee-buyers.html">See the full ranking</a>.</p>
        {% include top-buyers.html limit=10 short=true %}
      </div>
      <div class="col-lg-6 mb-4">
        <h2 id="marks">Top coffee marks</h2>
        <p>The factories and estates whose coffee sold in the largest volumes, by the mark on the lot.</p>
        <div class="mk-table-wrap bg-white">
          <table class="mk-table">
            <caption>Top 10 marks by volume sold</caption>
            <thead><tr><th scope="col">Mark</th><th scope="col" class="num">Tonnes</th><th scope="col" class="num">Avg price (US$/50 kg)</th></tr></thead>
            <tbody>
              {% for k in m.top_marks limit: 10 %}
              <tr><td>{{ k.name }}</td><td class="num">{% include num.html n=k.tonnes %}</td><td class="num">{{ k.price | round }}</td></tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="mk-section">
  <div class="container mk-prose">
    <h2 id="about-the-data">About the data</h2>
    <p>The Kenyan coffee season (crop year) runs from 1 October to 30 September. Picking usually peaks between October and December, with a smaller fly crop around April to June. Most Kenyan coffee is sold at the weekly auction of the <a href="http://nairobicoffeeexchange.co.ke" rel="noopener">Nairobi Coffee Exchange</a> (NCE), and the rest through direct sales between growers and buyers.</p>
    <p>These figures come from the sale results the NCE published after each auction from {{ m.first_sale | date: "%-d %B %Y" }} to {{ m.last_sale | date: "%-d %B %Y" }}. Prices are in US dollars per 50 kg bag of clean coffee. Averages are weighted by volume. MyKahawa aggregated the records, so small differences from NCE figures are possible; where they differ, the NCE figures prevail. Direct sales are not included.</p>
    <p>Need lot-level data, newer results or a custom analysis? <a href="/contact.html">Get in touch</a>.</p>
  </div>
</section>
