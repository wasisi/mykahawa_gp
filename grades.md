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
        <div id="example-table"></div>
      </div>
    </div>
  </div>
</article>

<link href="https://unpkg.com/tabulator-tables@4.8.1/dist/css/tabulator.min.css" rel="stylesheet">
<script type="text/javascript" src="https://unpkg.com/tabulator-tables@4.8.1/dist/js/tabulator.min.js"></script>

<script>
var table = new Tabulator("#coffeegradestablee", {
    ajaxURL:"/data/grades/coffeegrades.json", //ajax URL
});
</script> 


<script type="text/javascript">

	//sample data to be used in all tabulators
	var tabledata = [
	{id:1, name:"Oli Bob \n steve", age:"12", gender:"male", height:1, col:"red", dob:"", cheese:1, lucky_no:5},
	{id:2, name:"Mary May", age:"1", gender:"female", height:2, col:"blue", dob:"14/05/1982", cheese:true, lucky_no:10},
	{id:3, name:"Christine Lobowski", age:"42", height:0, col:"green", dob:"22/05/1982", cheese:"true", lucky_no:12},
	{id:4, name:"Brendon Philips", age:"125", gender:"male", height:1, col:"orange", dob:"01/08/1980", lucky_no:18},
	{id:5, name:"Margret Marmajuke", age:"16", gender:"female", height:5, col:"yellow", dob:"31/01/1999", lucky_no:33},
	{id:6, name:"Frank Harbours", age:"38", gender:"male", height:4, col:"red", dob:"", cheese:1, lucky_no:2},
	{id:7, name:"Jamie Newhart", age:"23", gender:"male", height:3, col:"green", dob:"14/05/1985", cheese:true, lucky_no:63},
	{id:8, name:"Gemma Jane", age:"60", height:0, col:"red", dob:"22/05/1982", cheese:"true", lucky_no:72},
	{id:9, name:"Emily Sykes", age:"42", gender:"female", height:1, col:"maroon", dob:"11/11/1970", lucky_no:44},
	{id:10, name:"James Newman", age:"73", gender:"male", height:5, col:"red", dob:"22/03/1998", lucky_no:9},
	];

</script>
<section>
	<header>Fit To Data <span> - for full documentation visit <a href="http://olifolkerd.github.io/tabulator/docs/#fittodata">http://olifolkerd.github.io/tabulator/docs/#fittodata</a></span></header>
	<p>
		Tables will automatically resize to fit the data
	</p>
	<div id="example-table-fittodata"></div>
  <script type="text/javascript">
  $("#example-table-fittodata").tabulator({
			height:"320px",
			columns:[
			{title:"Name", field:"name", width:200},
			{title:"Age", field:"age", width:60, align:"right", sorter:"number"},
			{title:"Gender", field:"gender"},
			{title:"Height", field:"height", align:"center", width:80},
			{title:"Favourite Color", field:"col"},
			{title:"Date Of Birth", field:"dob", align:"center", sorter:"date"},
			{title:"Likes Cheese", field:"cheese", align:"center"},
			],
    });
    $("#example-table-fittodata").tabulator("setData", tabledata);
    $(window).resize(function(){
			$("#example-table-fittodata").tabulator("redraw");
		});
</script>
</section>