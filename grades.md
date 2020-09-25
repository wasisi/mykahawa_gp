---
layout: base
title: Grades
comments: true
---
<header>
  <div class="container">
    <div class="header-content">
      <h1>Grades</h1>
    </div>
  </div>
</header>

<article> 
  <div class="container">
    <div class="row">
      <div class="col-md-8 mx-auto">
        <p class="lead">
          Kenya’s coffee is marketed internationally as Kenya Arabica grade AB which is classified as E, AA, AB, PB, C, TT and T. The grade is determined by size and density and liquor quality. The main processing methods employed are wet and dry processing. Wet processing results in higher quality parchment coffee than mbuni produced from dry processing. Between 2004 and 2009 there was an average of 91% of coffee that underwent wet processing. 
         </p>
         <p> 
          Quality is determined by the combination of the physical appearance of the green bean and the roasted coffee and more importantly the cup quality after tasting
        </p>
        <p>Coffee characteristics and processes that affect quality:</p>
        <ul>
          <li>Presence or absence of extraneous material like stones or twigs: Drying and cleaning  </li>
          <li>Wrinkled beans: Drying</li>
          <li>Cracking/shrunken and boat shaped beans: Drying</li>
          <li>Nipped or deformed coffee: Pulping</li>
          <li>Overall cup quality (aroma, thickness of the brew, taste, flavour and acidity): Picking, storage, washing, soaking, cleaning, pulping, and fermentation</li>
          <li>Fruity cup: Pulping</li>
          <li>Mustiness or foxy beans: Fermentation</li>
          <li>Foxy beans: Bagging</li>
          <li>Mould (Ochratoxin A): Drying, diseases, and pests</li>
        </ul>
        {% include ko-fi.html %}
        <h2>Coffee grades</h2>
          <div>
          <a href="/data/grades/coffeegrades.csv">
            <button>Download CSV</button>
          </a>  
          </div> 		      
          <div id="coffeegradestable"></div>
      </div>
    </div>
  </div>
   {% include disqus_comments.html %}
</article>

<link href="https://unpkg.com/tabulator-tables@4.8.1/dist/css/tabulator.min.css" rel="stylesheet">
<script type="text/javascript" src="https://unpkg.com/tabulator-tables@4.8.1/dist/js/tabulator.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/promise-polyfill@8/dist/polyfill.min.js"></script>
<script type="text/javascript" src="/data/grades/coffeegrades.json"></script>

<script type="text/javascript">	
	var local_data = coffeegrades_data;  <!-- name inside json file -->
	var table = new Tabulator("#coffeegradestable", {
		data: local_data,
		ajaxProgressiveLoad:"load",
		layout:"fitColumns",
		columns:[
		{title:"#", formatter:"rownum", align:"center", width:40},
		{title:"Grade",   field:"grade"},
		{title:"Grade name",   field:"grade_name"},
		{title:"Size", field:"size"},
		],
	});
</script>