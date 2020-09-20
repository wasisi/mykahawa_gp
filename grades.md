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
		<div id="coffeegradestable"></div>
      </div>
    </div>
  </div>
</article>

<link href="https://unpkg.com/tabulator-tables@4.8.1/dist/css/tabulator.min.css" rel="stylesheet">
<script type="text/javascript" src="https://unpkg.com/tabulator-tables@4.8.1/dist/js/tabulator.min.js"></script>
<script type="text/javascript" src="/data/grades/coffeegrades.json"></script>

<script type="text/javascript">					
				var local_data = coffeegrades_data;  <!-- name inside json file -->	
				var table = new Tabulator("#coffeegradestable", {
					height:"311px",								
					columns:[
					{title:"#", formatter:"rownum", align:"center", width:40},
					{title:"Grade",   field:"grade"},
					{title:"Grade name",   field:"grade_name"},
					{title:"Size", field:"size"},
					],					
				});					
</script>