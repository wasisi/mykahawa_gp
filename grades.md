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
      </div>
    </div>
  </div>
</article>

<section>
<h2>Example 1: Setting data inline</h2>
  <div id="example1"></div>
  <pre class="prettyprint">
  <script src="/data/table.js" type="text/javascript"></script>
  </pre>
</section>

<section>
  <h2>Example 2: Setting data from external source</h2>
    <div id="example2"></div>
    <pre class="prettyprint">
      <code> 
        $.ajax({
          url:'data.json',
          dataType: 'json', 
          success: function(json) { 
              example2 = $('#example2').columns({
                  data:json, 
             }); 
          }
        }); 
      </code>
    </pre>
</section>
