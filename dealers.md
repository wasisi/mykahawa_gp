---
layout: base
title: Dealers
redirect_from: "/directory/dealers/"
comments: false
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
          Coffee dealers/traders are persons licensed to buy coffee at the Nairobi Coffee Exchange or to import coffee. The coffee dealer license is issued by the Agriculture and Food Authority. Find out more here: <a href="https://www.wikiprocedure.com/index.php/Kenya_-_Obtain_Coffee_Dealers_License" target="_blank">WikiProcedure</a>  
        </p>
        <h2>Coffee dealers</h2>
          <div>
          <a href="/data/dealers/coffeedealers.csv">
            <button>Download CSV</button>
          </a>  
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
		{title:"Dealer", field:"title"},
		{title:"Website", field:"website"},
		],
	});
</script>