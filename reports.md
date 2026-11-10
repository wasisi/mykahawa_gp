---
layout: base
hero: true
title: "Kenya coffee market reports"
heading: Market reports
description: "MyKahawa's free market intelligence reports on Kenyan coffee: auction prices and volumes, grade premiums, prices by county and buyer concentration at the Nairobi Coffee Exchange."
lead: "Independent analysis of the Kenyan coffee market, based on Nairobi Coffee Exchange auction results. Each report can be saved as a PDF."
permalink: /reports/
---
<section class="mk-section">
  <div class="container">
    <h2 class="sr-only">All reports</h2>
    <div class="mk-cards" style="grid-template-columns: repeat(auto-fill, minmax(20rem, 1fr));">
      {% assign reports = site.reports | sort: "date" | reverse %}
      {% for r in reports %}
      <a class="mk-card" href="{{ r.url }}">
        <h3>{{ r.heading | default: r.title }}</h3>
        <p>{{ r.lead }}</p>
        <span class="mk-card-meta">Read the report →</span>
      </a>
      {% endfor %}
    </div>
    <div class="mk-chart-card mt-5" style="max-width:48rem">
      <h2 class="h3">Custom analysis</h2>
      <p class="mb-0">Need figures for a specific cooperative, county, grade or buyer, or a briefing for your organisation? <a href="/contact.html">Contact MyKahawa</a>.</p>
    </div>
  </div>
</section>
