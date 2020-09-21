---
layout: base
title: Growers
---
<header>
  <div class="container">
    <div class="header-content">
      <h1>Growers</h1>
    </div>
  </div>
</header>

<article>
  <div class="container">
    <div class="row">
      <div class="col-md-8 mx-auto">
        <p class="lead">
          These are the guys grow all coffee
        </p>
        <h2>Coffee growers</h2>
          <div id="coffeegrowerstable"></div>
      </div>
    </div>
  </div>
</article>

<link href="https://unpkg.com/tabulator-tables@4.8.1/dist/css/tabulator.min.css" rel="stylesheet">
<script type="text/javascript" src="https://unpkg.com/tabulator-tables@4.8.1/dist/js/tabulator.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/promise-polyfill@8/dist/polyfill.min.js"></script>
<script type="text/javascript" src="/data/growers/coffeegrowers.json"></script>

<script type="text/javascript">	
	var local_data = coffeegrowers_data;  <!-- name inside json file -->
	var table = new Tabulator("#coffeegrowerstable", {
		data: local_data,
		ajaxProgressiveLoad:"load",
		layout:"fitColumns",
		columns:[
		{title:"#", formatter:"rownum", align:"center", width:80},
		{title:"Ref",   field:"title"},
		{title:"Grower name",   field:"producer_name"},
    {title:"Category",   field:"actor"},
		],
	});
</script>