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


<script type="text/javascript">
//create Tabulator on DOM element with id "example-table"
var table = new Tabulator("#example-table", {
 	height:205, // set height of table (in CSS or here), this enables the Virtual DOM and improves render speed dramatically (can be any valid css height value)
 	layout:"fitColumns", //fit columns to width of table (optional)
 	columns:[ //Define Table Columns
	 	{title:"Name", field:"name", width:150},
	 	{title:"Age", field:"age", align:"left", formatter:"progress"},
	 	{title:"Favourite Color", field:"col"},
	 	{title:"Date Of Birth", field:"dob", sorter:"date", align:"center"},
 	],
 	rowClick:function(e, row){ //trigger an alert message when the row is clicked
 		alert("Row " + row.getData().id + " Clicked!!!!");
 	},
});
</script>

<script type="text/javascript">
//define some sample data
var tabledata = '/data/grades/coffeegrades.json'
[
	{id:1, name:"Oli Bob", age:"12", col:"red", dob:""},
	{id:2, name:"Mary May", age:"1", col:"blue", dob:"14/05/1982"},
	{id:3, name:"Christine Lobowski", age:"42", col:"green", dob:"22/05/1982"},
	{id:4, name:"Brendon Philips", age:"125", col:"orange", dob:"01/08/1980"},
	{id:5, name:"Margret Marmajuke", age:"16", col:"yellow", dob:"31/01/1999"},
];

//load sample data into the table
table.setData(tabledata);
</script>