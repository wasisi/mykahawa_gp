---
title: "Kenya coffee grades: AA, AB, PB, C, E, TT, T explained"
heading: Kenya coffee grades
description: "Kenyan coffee grades explained (AA, AB, PB, C, E, TT, T, MH, ML and more): bean size, screen and the average auction price of each grade at the Nairobi Coffee Exchange."
redirect_from:
  - "/coffee/grades/"
  - "/grades.html"
---

## Introduction

Kenya’s coffee is marketed internationally as Kenya Arabica grade AB which is classified as E, AA, AB, PB, C, TT and T. The grade is determined by size and density and liquor quality. The main processing methods employed are wet and dry processing. Wet processing results in higher quality parchment coffee than mbuni produced from dry processing. Between 2004 and 2009 there was an average of 91% of coffee that underwent wet processing.

## Grades and auction prices

{% assign order = "E,AA,AB,PB,C,TT,T,HE,SB,MH,ML,UG,UG1,UG2" | split: "," %}
{% assign gd = site.data.directory.grades %}
{% assign mg = site.data.market.grades %}

<div class="mk-table-wrap mb-3">
<table class="mk-table">
<caption>Kenyan coffee grades with average Nairobi Coffee Exchange price, {{ site.data.market.first_sale | date: "%Y" }}–{{ site.data.market.last_sale | date: "%Y" }}</caption>
<thead><tr><th scope="col">Grade</th><th scope="col">Name and description</th><th scope="col" class="num">Avg price<br><span class="font-weight-normal">US$/50 kg</span></th><th scope="col" class="num">Tonnes sold</th></tr></thead>
<tbody>
{% for code in order %}{% assign g = gd | where: "grade", code | first %}{% assign p = mg | where: "grade", code | first %}{% if g %}
<tr>
<th scope="row">{{ g.grade }}</th>
<td><strong>{{ g.grade_name }}</strong>{% if g.description != "" %}<br><span class="small">{{ g.description }}</span>{% endif %}</td>
<td class="num">{% if p %}{{ p.price | round }}{% else %}–{% endif %}</td>
<td class="num">{% if p %}{% include num.html n=p.tonnes %}{% else %}–{% endif %}</td>
</tr>
{% endif %}{% endfor %}
</tbody>
</table>
</div>

Prices are volume-weighted averages of all lots sold at the Nairobi Coffee Exchange auction from {{ site.data.market.first_sale | date: "%B %Y" }} to {{ site.data.market.last_sale | date: "%B %Y" }}. See how [grade prices changed season by season](/transactions.html#grades).

