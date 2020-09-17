$.getJSON('countygradeweight/?format=json', function(jsonfile){


var labels = jsonfile.map(function(e) {
   return e.grade;
});
var sum = jsonfile.map(function(e) {
   return e.grade_weight;
});

var ctx = document.getElementById('countygradeweight').getContext('2d');
var config = {
   type: 'bar',
   data: {
      labels: labels,
      datasets: [
      {
         label: 'Weight',
         data: sum,
         backgroundColor: 'rgba(35,139,69,1)'
      },
      ]
   },
   options: {
            responsive: true,
            title: {
               display: true,
               text: 'Weight offered (Kg) per Grade during the last 365 days'
            },
            tooltips: {
               mode: 'index',
               intersect: false,
            },
            hover: {
               mode: 'nearest',
               intersect: true
            },
            scales: {
               xAxes: [{
                  display: true,
                  scaleLabel: {
                     display: true,
                     labelString: 'Grade'
                  }
               }],
               yAxes: [{
                  display: true,
                  scaleLabel: {
                     display: true,
                     labelString: 'Weight (Kg)'
                  }
               }]
            }
         }
};

var chart = new Chart(ctx, config);})
