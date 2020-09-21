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
          <div>
            <button id="download-csv">Download CSV</button>
          </div>  
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
    height:"500px",
		data: local_data,
		ajaxProgressiveLoad:"scroll",
		layout:"fitColumns",
    virtualDomHoz:true,
		columns:[
		{title:"#", formatter:"rownum", align:"center", width:80},
		{title:"Ref",   field:"title"},
		{title:"Grower name",   field:"producer_name"},
    {title:"Category",   field:"actor"},
    {title:"Latitude",   field:"lat"},
    {title:"Longitude",   field:"lon"},
    {title:"Location accuracy",   field:"location_accuracy"},
    {title:"Location source",   field:"location_source"},
    {title:"Location notes",   field:"location_notes"},
    {title:"Location verified?",   field:"location_verified"},
    {title:"Disambiguation",   field:"disambiguation"},
    {title:"Notes",   field:"notes"},
		],
	});

  //trigger download of data.csv file
document.getElementById("download-csv").addEventListener("click", function(){
    table.download("csv", "data.csv");
});

</script>