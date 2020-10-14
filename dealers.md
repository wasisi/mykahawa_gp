---
layout: base
title: Dealers
redirect_from: "/directory/dealers/"
comments: true
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
          Coffee dealers are persons registered by the county governments or the Agriculture and Food Authority to deal with coffee in Kenya. The coffee dealer license is issued by the <a href="https://coffee.agricultureauthority.go.ke/index.php/sectors/stakeholders" target="_blank">Agriculture and Food Authority (AFA)</a>. The list below includes 157 dealers as follows: 84 Coffee Dealers, 15 Coffee Millers, 11 Commercial Marketing Agents, 22 Grower Marketers, 14 Private Coffee Warehousemen, 7 Commercial Coffee Warehousemen and 4 Management Agents. Information on how to register for a license is available on <a href="https://www.wikiprocedure.com/index.php/Kenya_-_Obtain_Coffee_Dealers_License" target="_blank">WikiProcedure</a>  
        </p>
        <h2>Coffee dealers</h2>
          <div>
          <a class="btn btn-primary" href="/data/dealers/coffeedealers.csv" role="button">Download list of coffee dealers</a>
          <br><br>
          </div>         
          <div id="coffeedealerstable"></div>
      </div>
    </div>
  </div>

{% include disqus_comments.html %}
  
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
    {title:"Category", field:"category"},
		{title:"Dealer", field:"title"},
		{title:"Website", field:"website"},
		],
	});
</script>