---
layout: base
title: Growers
redirect_from: "/directory/producers/"
comments: true
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
          Kenya’s coffee is grown in the highlands between 1400 and 2000 metres above sea level. The main growing areas are around Mt. Kenya, Nakuru and Machakos. Most of Kenya’s coffee is grown on small farms organized into cooperatives and plantation/large estates. According to the Coffee Act (2001), the distinction between small and large farms is determined by the size and ownership of pulping stations. In Kenya, it is estimated that 60% of coffee is produced by smallholder farmers.
        </p>
        <h2>Coffee growers</h2>
          <div>
          <a href="/data/growers/coffeegrowers.csv">
            <button>Download CSV</button>
          </a>  
          </div>  
          <div id="coffeegrowerstable"></div>
      </div>
    </div>
  </div>

  {% include disqus_comments.html %}
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
    {title:"Disambiguation",   field:"disambiguation"},
		],
	});

</script>