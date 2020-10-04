$.getJSON('/marketvalue/?format=json', function(jsonfile){


var labels = jsonfile.map(function(e) {
   return e.isodate;
});
var value = jsonfile.map(function(e) {
   return e.sale_value;
});

var ctx = document.getElementById('marketvalue').getContext('2d');
var config = {
   type: 'line',
   data: {
      labels: labels,
      datasets: [{
         label: 'Value',
         data: value,
         backgroundColor: 'rgba(35,139,69,1)'
      },
      ]
   },
   options: {
            responsive: true,
            title: {
               display: true,
               text: 'Value (USD $) per Sale during the last 365 days'
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
                     labelString: 'Date of Sale'
                  }
               }],
               yAxes: [{
                  display: true,
                  scaleLabel: {
                     display: true,
                     labelString: 'Value (USD $)'
                  }
               }]
            }
         }
};

var chart = new Chart(ctx, config);})
