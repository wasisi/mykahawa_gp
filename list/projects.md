---
layout: base
hero: true
title: "Kenya coffee: guides to the market, grades, laws and licensing"
heading: Kenya coffee guides
description: "Guides to Kenyan coffee: how the value chain works, coffee grades, the current laws and regulations, Coffee Board and county licensing, quality, certification and a glossary of trade terms."
lead: "Everything you need to understand how Kenyan coffee is grown, graded, regulated and sold, written in plain language and updated for the current regulations."
permalink: kenya-coffee.html
---
{% assign m = site.data.market %}
<section class="mk-section">
  <div class="container">
    <h2 class="sr-only">Guides</h2>
    <div class="mk-cards mb-5">
      <a class="mk-card" href="/projects/kenya-coffee-valuechain.html">
        <h3>The value chain</h3>
        <p>How coffee moves from cherry to parchment, through milling, the auction and payment, to export.</p>
        <span class="mk-card-meta">Read the guide →</span>
      </a>
      <a class="mk-card" href="/projects/kenya-coffee-grades.html">
        <h3>Coffee grades</h3>
        <p>The official Kenya grades (E, AA, AB, PB, C, TT, T…), how grading works and what each grade sells for.</p>
        <span class="mk-card-meta">Read the guide →</span>
      </a>
      <a class="mk-card" href="/projects/kenya-coffee-laws.html">
        <h3>Laws and regulations</h3>
        <p>The new Coffee Act, 2026, the Coffee Board of Kenya, payment and trading rules, the levy and penalties.</p>
        <span class="mk-card-meta">Read the guide →</span>
      </a>
      <a class="mk-card" href="/projects/kenya-coffee-licensing.html">
        <h3>Licensing</h3>
        <p>Which licences the Coffee Board, county governments and CMA issue under the Coffee Act, 2026.</p>
        <span class="mk-card-meta">Read the guide →</span>
      </a>
      <a class="mk-card" href="/projects/kenya-coffee-glossary.html">
        <h3>Glossary</h3>
        <p>Miller-marketer, prompt date, out-turn, warrant, buni and more, explained in plain language.</p>
        <span class="mk-card-meta">Look up a term →</span>
      </a>
      <a class="mk-card" href="/projects/coffee-quality.html">
        <h3>Coffee quality</h3>
        <p>How picking, pulping, fermentation and drying affect the quality of the cup.</p>
        <span class="mk-card-meta">Read the guide →</span>
      </a>
      <a class="mk-card" href="/projects/coffee-certification.html">
        <h3>Certification</h3>
        <p>Sustainability certification and verification schemes used for Kenyan coffee.</p>
        <span class="mk-card-meta">Read the guide →</span>
      </a>
      <a class="mk-card" href="/reports/">
        <h3>Market reports</h3>
        <p>MyKahawa's analysis of prices, grades, counties and buyers at the auction.</p>
        <span class="mk-card-meta">Read the reports →</span>
      </a>
    </div>

    <div class="row">
      <div class="col-lg-7 mk-prose">
        <h2>Kenyan coffee in brief</h2>
        <p>Coffee was introduced to Kenya in the 1890s by French and Scottish missionaries. Their trials gave rise to "French Mission" coffee. Breeding for quality and resistance to disease, pests and drought later produced the varieties Kenya is known for, including Scott Laboratories' <strong>SL28</strong> and <strong>SL34</strong>, K7, and the disease-resistant <strong>Ruiru 11</strong> and <strong>Batian</strong>.</p>
        <p>Kenya grows almost entirely <strong>washed Arabica</strong>, at 1,400–2,000 metres on the slopes of Mount Kenya, the Aberdares, Mount Elgon and other highland areas. It is prized for bright acidity, body and fruity, often blackcurrant-like flavours, and the large-bean grades <a href="/projects/kenya-coffee-grades.html">AA and AB</a> are sought after by specialty roasters worldwide.</p>
        <p>Most coffee is grown by smallholder farmers organised in <a href="/directory/cooperatives.html">cooperative societies</a>, alongside private <a href="/directory/estates.html">estates</a>. It is sold mainly at the weekly auction of the Nairobi Coffee Exchange, where between {{ m.first_sale | date: "%Y" }} and {{ m.last_sale | date: "%Y" }} the average price was <strong>US${{ m.price | round }}</strong> per 50 kg bag.</p>
      </div>
      <div class="col-lg-5">
        <div class="mk-chart-card">
          <h2 class="h3">Key facts</h2>
          <ul class="mb-0">
            <li>Coffee year: 1 October – 30 September</li>
            <li>Main crop: October–December; fly crop: April–June</li>
            <li>Altitude: 1,400–2,000 m</li>
            <li>Main varieties: SL28, SL34, Ruiru 11, Batian</li>
            <li>Auction: Nairobi Coffee Exchange, priced in US$ per 50 kg bag</li>
            <li>Regulators: <a href="/projects/kenya-coffee-licensing.html">Coffee Board of Kenya, county governments, CMA</a></li>
            <li>{% include num.html n=site.data.directory.growers_total %} growers in the <a href="/growers.html">MyKahawa directory</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>
