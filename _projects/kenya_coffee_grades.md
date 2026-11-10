---
title: "Kenya coffee grades explained: AA, AB, PB, C, E, TT, T and prices"
heading: Kenya coffee grades
description: "The official Kenya coffee grades (E, AA, AB, PB, C, TT, T, MH, ML, HE, SB, UG) with screen sizes from the Coffee Regulations, how grading works, and the average auction price of each grade."
redirect_from:
  - "/coffee/grades/"
  - "/grades.html"
---
{% assign m = site.data.market %}
{% assign std = site.data.grade_standards %}

Kenyan coffee is sold by **grade**. After milling, clean coffee is sorted by bean size, shape and density into the Kenya Standard grades set out in the Fifth Schedule of the Crops (Coffee) (General) Regulations, 2019. The [Coffee Act, 2026](/projects/kenya-coffee-laws.html) requires millers to follow the prescribed standard grades, and new grading regulations may update this list. The grade is the first thing buyers look at in an auction catalogue, and it has a big effect on price: between {{ m.first_sale | date: "%Y" }} and {{ m.last_sale | date: "%Y" }}, AA sold for about {% assign aa = m.grades | where: "grade", "AA" | first %}{% assign t = m.grades | where: "grade", "T" | first %}**US${{ aa.price | round }}** per 50 kg bag at the Nairobi Coffee Exchange, while T fetched about **US${{ t.price | round }}**.

## How Kenyan coffee is graded

Grading happens at the dry mill, after parchment coffee has been hulled. The Nairobi Coffee Exchange describes four factors:

1. **Bean size (screen size).** Beans are shaken through a stack of perforated screens. The screen a bean is retained on gives its size grade. Larger screens generally mean higher grades.
2. **Density.** Heavier, denser beans are preferred for premium grades. Light beans are blown out by air into the TT grade.
3. **Defects.** Fewer broken, discoloured or damaged beans means a better grade.
4. **Cup quality.** Liquorers taste every lot. A coffee's cup quality can raise or lower its value beyond what its size grade suggests.

The Regulations require that, where a grade is specified, **at least 95% of the beans must fall within that grade**. Millers must follow these Kenya standards as well as regional and international standards, and specialty coffee is graded under protocols such as those of the Specialty Coffee Association.

## The Kenya Standard grades

<div class="mk-table-wrap mb-3">
<table class="mk-table">
<caption>Main Kenya coffee grades: screen size, description and average auction price, {{ m.first_sale | date: "%Y" }}–{{ m.last_sale | date: "%Y" }}</caption>
<thead><tr><th scope="col">Grade</th><th scope="col">Screen size</th><th scope="col">What it is</th><th scope="col" class="num">Avg price<br><span class="font-weight-normal">US$/50 kg</span></th><th scope="col" class="num">Share of volume</th></tr></thead>
<tbody>
{% for g in std.main %}{% assign p = m.grades | where: "grade", g.grade | first %}
<tr>
<th scope="row">{{ g.grade }}<div class="small font-weight-normal">{{ g.name }}</div></th>
<td>{{ g.screen }}</td>
<td>{{ g.standard }} <span class="small text-muted d-block mt-1">{{ g.notes }}</span></td>
<td class="num">{% if p %}{{ p.price | round }}{% else %}–{% endif %}</td>
<td class="num">{% if p %}{{ p.tonnes | times: 100.0 | divided_by: m.tonnes | round: 1 }}%{% else %}–{% endif %}</td>
</tr>
{% endfor %}
</tbody>
</table>
</div>

## Other Kenyan grades

<div class="mk-table-wrap mb-3">
<table class="mk-table">
<caption>Miscellaneous Kenya coffee grades</caption>
<thead><tr><th scope="col">Grade</th><th scope="col">Name</th><th scope="col">Description</th><th scope="col" class="num">Avg price<br><span class="font-weight-normal">US$/50 kg</span></th></tr></thead>
<tbody>
{% for g in std.miscellaneous %}{% assign p = m.grades | where: "grade", g.grade | first %}
<tr>
<th scope="row">{{ g.grade }}</th>
<td>{{ g.name }}</td>
<td>{{ g.standard }}</td>
<td class="num">{% if p %}{{ p.price | round }}{% else %}–{% endif %}</td>
</tr>
{% endfor %}
</tbody>
</table>
</div>

**Mbuni (MH, ML)** is coffee that was dried in the cherry instead of being pulped and washed. It is graded separately from washed (parchment) coffee and usually sells for much less. **UG1** (US${% assign u = m.grades | where: "grade", "UG1" | first %}{{ u.price | round }}) and **UG2** (US${% assign u = m.grades | where: "grade", "UG2" | first %}{{ u.price | round }}) are ungraded lots of different quality.

## Grade is not everything

Two AA lots can sell for very different prices. Cup quality, the reputation of the factory or estate, certification and the lot size all matter. See how prices for each grade [changed season by season](/transactions.html#grades), and look up the grade-by-grade prices of any [cooperative, factory or estate](/growers.html).

<p class="mk-note">Sources: Crops (Coffee) (General) Regulations, 2019, Fifth Schedule (as revised to 31 December 2022); Nairobi Coffee Exchange, <a href="https://www.nairobicoffeeexchange.co.ke/kenya-coffee-origin/coffee-grades" rel="noopener">Understanding Kenya Coffee Grades</a>. Prices: volume-weighted averages of Nairobi Coffee Exchange auction lots, {{ m.first_sale | date: "%B %Y" }} to {{ m.last_sale | date: "%B %Y" }}, compiled by MyKahawa.</p>
