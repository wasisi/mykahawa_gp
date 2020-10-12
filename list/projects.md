---
title: Kenya Coffee
narrow: true
permalink: kenya-coffee.html
show_profile: true

---

Coffee was introduced in Kenya in the 1890s by French and Scotties Missionaries who were experimenting on the suitability of different sites types of coffee that came to be known as “French Mission Coffee”. This followed from the breeding of various varieties of coffee to cope with diseases, pests and drought. These varieties include Scott Laboratory (SL) 28 and 34, Blue Mountain, Kent (K) variety K7, and K20,and Ruiru 11. 

{% for project in site.projects %}
- [{{ project.title }}]({{ site.baseurl }}{{ project.url }})
{% endfor %}
