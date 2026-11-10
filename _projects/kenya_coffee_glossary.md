---
title: "Kenya coffee glossary: terms used in the Kenyan coffee trade"
heading: Kenya coffee glossary
description: "Plain-language definitions of the terms used in Kenya's coffee trade and regulations: miller-marketer, grower marketer, direct settlement system, prompt date, parchment, buni, out-turn, warrant and more."
---

Key terms used in the Kenyan coffee trade, in plain language. The definitions follow the [current coffee regulations](/projects/kenya-coffee-laws.html) (Crops (Coffee) (General) Regulations, 2019, as amended to 2022, and the Capital Markets (Coffee Exchange) Regulations, 2020). The 2022 amendments removed "agent" and "broker" from the coffee regulations. Coffee brokers are now licensed under the capital markets rules, and miller-marketers took over the role of marketing agents.

{% assign letters = "" %}{% for t in site.data.glossary %}{% assign l = t.term | slice: 0 %}{% unless letters contains l %}{% assign letters = letters | append: l %}{% endunless %}{% endfor %}
<p class="mk-glossary-index">{% assign ls = letters | split: "" %}{% for l in ls %}<a href="#letter-{{ l | downcase }}">{{ l }}</a> {% endfor %}</p>

{% assign current = "" %}
{% for t in site.data.glossary %}{% assign l = t.term | slice: 0 %}{% if l != current %}{% unless forloop.first %}</dl>{% endunless %}{% assign current = l %}
<h2 id="letter-{{ l | downcase }}" class="h4 mt-4">{{ l }}</h2>
<dl class="mk-glossary">{% endif %}
<dt id="{{ t.term | slugify }}">{{ t.term }}</dt>
<dd>{{ t.def }}{% if t.see %} <a href="{{ t.see }}">More →</a>{% endif %}</dd>
{% endfor %}</dl>
