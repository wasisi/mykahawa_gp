---
layout: base
hero: true
title: "Coffee buyers in Kenya: top buyers at the Nairobi Coffee Exchange"
heading: Top coffee buyers in Kenya
description: "Ranking of the biggest coffee buyers at the Nairobi Coffee Exchange auction by tonnes bought, market share and average price, 2015–2020."
lead: "Who buys Kenya's coffee? The companies that bought the most at the Nairobi Coffee Exchange auction, ranked by volume."
breadcrumbs:
  - title: Directory
    url: /directory.html
permalink: /directory/coffee-buyers.html
---
{% assign m = site.data.market %}
<section class="mk-section">
  <div class="container">
    <div class="mk-prose mb-4">
      <p>Between {{ m.first_sale | date: "%-d %B %Y" }} and {{ m.last_sale | date: "%-d %B %Y" }}, {{ m.buyer_count }} buyers bought {% include num.html n=m.tonnes %} tonnes of coffee at {{ m.sales }} weekly auctions of the Nairobi Coffee Exchange (NCE). The four largest buyers took more than half of the volume. A buyer's average price shows the quality mix it buys: buyers that focus on top grades such as AA and AB pay well above the market average of US${{ m.price | round }} per 50 kg bag.</p>
      <p>Coffee sold through direct sales outside the auction is not included. For the full list of licensed companies, see <a href="/directory/coffee-exporters.html">coffee exporters and dealers in Kenya</a>.</p>
    </div>
    {% include top-buyers.html limit=30 %}
    <p class="mk-note mt-3">Average price is weighted by volume, in US dollars per 50 kg bag of clean coffee. Value = tonnes × price. Source: Nairobi Coffee Exchange sale results, compiled by MyKahawa.</p>
  </div>
</section>
