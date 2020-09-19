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
    <code>
        $('#example1').columns({
          data: [
            {'Emp. Number': 00001, 'First Name':'John', 'Last Name':'Smith' },
            {'Emp. Number': 00002, 'First Name':'Jane', 'Last Name':'Doe' },
            {'Emp. Number': 00003, 'First Name':'Ted', 'Last Name':'Johnson' },
            {'Emp. Number': 00004, 'First Name':'Betty', 'Last Name':'Smith' },
            {'Emp. Number': 00005, 'First Name':'Susan', 'Last Name':'Wilson' },
            {'Emp. Number': 00006, 'First Name':'John', 'Last Name':'Doe' },
            {'Emp. Number': 00007, 'First Name':'Bill', 'Last Name':'Watson' },
            {'Emp. Number': 00008, 'First Name':'Walter', 'Last Name':'Wright' }
          ]
        });
      </code>
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
