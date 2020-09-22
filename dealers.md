---
layout: base
title: Dealers
---
<header>
  <div class="container">
    <div class="header-content">
      <h1>Dealers</h1>
    </div>
  </div>
</header>

<article>
  <div class="container">
    <div class="row">
      <div class="col-md-8 mx-auto">
        <p class="lead">
          These are the guys who buy all the coffee
        </p>
        <h2>Coffee dealers</h2>
          <div id="coffeedealerstable"></div>
      </div>
    </div>
  </div>
</article>

<link href="https://unpkg.com/tabulator-tables@4.8.1/dist/css/tabulator.min.css" rel="stylesheet">
<script type="text/javascript" src="https://unpkg.com/tabulator-tables@4.8.1/dist/js/tabulator.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/promise-polyfill@8/dist/polyfill.min.js"></script>
<script type="text/javascript" src="/data/dealers/coffeedealers.json"></script>

<script type="text/javascript">	
	var local_data = coffeedealers_data;  <!-- name inside json file -->
	var table = new Tabulator("#coffeedealerstable", {
		data: local_data,
		ajaxProgressiveLoad:"load",
		layout:"fitColumns",
		columns:[
		{title:"#", formatter:"rownum", align:"center", width:40},
		{title:"Dealer", field:"title"},
		{title:"Website", field:"website"},
		],
	});
</script>