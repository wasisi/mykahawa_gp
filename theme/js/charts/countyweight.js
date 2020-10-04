$.getJSON('/countyweight/?format=json', function(jsonfile){


var labels = jsonfile.map(function(e) {
   return e.county_name;
});
var sum = jsonfile.map(function(e) {
   return e.county_weight;
});

var ctx = document.getElementById('countyweight').getContext('2d');
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
               text: 'Weight offered (Tonnes) per county during the last 365 days'
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
                     labelString: 'County'
                  }
               }],
               yAxes: [{
                  display: true,
                  scaleLabel: {
                     display: true,
                     labelString: 'Weight (Tonnes)'
                  }
               }]
            }
         }
};

var chart = new Chart(ctx, config);})
