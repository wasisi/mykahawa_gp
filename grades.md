---
layout: base
title: Grades
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
          Guide on the classification of coffee by grade
        </p>
        <h2>Coffee grades</h2>
		<div id="example-table"></div>
      </div>
    </div>
  </div>
</article>

<link href="https://unpkg.com/tabulator-tables@4.8.1/dist/css/tabulator.min.css" rel="stylesheet">
<script type="text/javascript" src="https://unpkg.com/tabulator-tables@4.8.1/dist/js/tabulator.min.js"></script>
<script type="text/javascript" src="/data/user_data.json"></script>

<script type="text/javascript">					
				var local_data = esp_data;  <!-- name inside json file -->	
				var table = new Tabulator("#example-table", {
					data: local_data,
					pagination:"local",
					paginationSize:10,
					layout:"fitColumns",
					placeholder:"No Data Available",								
					columns:[
					{title:"#", formatter:"rownum", align:"center", width:40},
					{title:"Name",   field:"name"},
					{title:"Card ID",   field:"card"},
					{title:"Access", field:"access", sorter:"number"},
					{title:"Del",  width:60 , formatter:"buttonCross", align:"center"},
					{title:"Edit", width:60 , formatter:"buttonTick", align:"center" },
					],					
				});					
</script>