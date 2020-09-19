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

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="/plugins/gotopage.js"></script>
<script src="/plugins/ajaxpaging.js"></script>
<script src="/js/vendor/jquery.columns.min.js"></script>
<script>
  //Coffee grades
  $.ajax({
      url:'/data/grades/coffeegrades.json',
      dataType: 'json', 
      success: function(json) { 
          coffeegradestable = $('#coffeegradestable').columns({
              data:json
          }); 
      }
  }); 
</script> 