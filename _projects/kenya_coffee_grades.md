---
title: Kenya coffee grades
redirect_from: "/coffee/grades/"
redirect_from: "/grades.html"
---

## Introduction

Kenya’s coffee is marketed internationally as Kenya Arabica grade AB which is classified as E, AA, AB, PB, C, TT and T. The grade is determined by size and density and liquor quality. The main processing methods employed are wet and dry processing. Wet processing results in higher quality parchment coffee than mbuni produced from dry processing. Between 2004 and 2009 there was an average of 91% of coffee that underwent wet processing.[Download CSV](/data/grades/coffeegrades.csv).


<a href="/data/grades/coffeegrades.csv">
<button>Download CSV</button>
      
<div id="coffeegradestable"></div>

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

