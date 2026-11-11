---
layout: base
hero: true
title: Kenya coffee directory
heading: Kenya coffee directory
description: "Directory of Kenya's coffee industry: exporters and dealers, millers, marketing agents, warehousemen, cooperatives, factories and estates, by type and county."
lead: "Find the businesses behind Kenyan coffee, from the cooperatives and estates that grow it to the millers, marketing agents and exporters that bring it to market."
permalink: /directory.html
redirect_from:
  - /directory/
---
{% assign d = site.data.directory %}
<section class="mk-section">
  <div class="container">
    <h2>Licensed coffee businesses</h2>
    <p class="mk-note">{{ d.dealers_total }} coffee businesses: {{ d.dealers_total | minus: d.dealers_proposed }} licensed by AFA (licensing has passed to the Coffee Board of Kenya under the Coffee Act, 2026), and {{ d.dealers_proposed }} proposed for a licence in the Kenya Gazette since August 2025.</p>
    <div class="mk-cards mb-5">
      {% for g in d.dealer_groups %}
      <a class="mk-card" href="/directory/{{ g.slug }}.html">
        <h3>{{ g.label }}</h3>
        <p>{{ g.title }}</p>
        <span class="mk-card-meta">{{ g.count }} listed →</span>
      </a>
      {% endfor %}
      <a class="mk-card" href="/directory/coffee-buyers.html">
        <h3>Top buyers</h3>
        <p>The biggest buyers at the Nairobi Coffee Exchange, ranked by volume</p>
        <span class="mk-card-meta">{{ site.data.market.buyer_count }} buyers →</span>
      </a>
    </div>

    <h2>Coffee growers</h2>
    <p class="mk-note">{% include num.html n=d.growers_total %} growers, {{ d.growers_mapped }} of them on the <a href="/growers.html">map</a>.</p>
    <div class="mk-cards mb-5">
      {% assign coops = d.grower_types | where: "type", "Cooperative society" | first %}
      {% assign facs = d.grower_types | where: "type", "Factory" | first %}
      {% assign est = d.grower_types | where: "type", "Estate" | first %}
      {% assign sest = d.grower_types | where: "type", "Small estate" | first %}
      <a class="mk-card" href="/directory/cooperatives.html">
        <h3>Cooperative societies</h3>
        <p>Smallholder farmers' cooperatives</p>
        <span class="mk-card-meta">{{ coops.count }} listed →</span>
      </a>
      <a class="mk-card" href="/directory/factories.html">
        <h3>Factories (wet mills)</h3>
        <p>Washing stations where farmers deliver cherry</p>
        <span class="mk-card-meta">{{ facs.count }} listed →</span>
      </a>
      <a class="mk-card" href="/directory/estates.html">
        <h3>Estates and farms</h3>
        <p>Privately owned estates and small estates</p>
        <span class="mk-card-meta">{{ est.count | plus: sest.count }} listed →</span>
      </a>
      <a class="mk-card" href="/growers.html">
        <h3>Map and search</h3>
        <p>Search every grower by name, code or county</p>
        <span class="mk-card-meta">Open the map →</span>
      </a>
    </div>

    <h2 id="counties">Coffee growers by county</h2>
    <div class="mk-table-wrap" style="max-width:40rem">
      <table class="mk-table">
        <thead><tr><th scope="col">County</th><th scope="col" class="num">Growers listed</th></tr></thead>
        <tbody>
          {% assign counties = d.grower_counties | sort: "county" %}
          {% for c in counties %}
          <tr><td><a href="/directory/county/{{ c.slug }}.html">{{ c.county }}</a></td><td class="num">{{ c.count }}</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    <p class="mk-note mt-3">The directory is based on Nairobi Coffee Exchange transactions from 2015 to 2020 and the 2012 Kenya Coffee Directory of the Kenya Coffee Traders Association. To add, correct or remove a listing, email <a href="mailto:wasisi.coffee@gmail.com">wasisi.coffee@gmail.com</a>. Listings are free.</p>
  </div>
</section>
