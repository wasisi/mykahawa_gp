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

<script>
var table = new Tabulator("#example-table", {
    height:"311px",
    columns:[
    {title:"Name", field:"name"},
    {title:"Progress", field:"progress", sorter:"number"},
    {title:"Gender", field:"gender"},
    {title:"Rating", field:"rating"},
    {title:"Favourite Color", field:"col"},
    {title:"Date Of Birth", field:"dob", hozAlign:"center"},
    ],
});
</script>