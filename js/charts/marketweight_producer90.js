$.getJSON('marketweight90/?format=json', function(jsonfile){


var labels = jsonfile.map(function(e) {
   return e.isodate;
});
var value = jsonfile.map(function(e) {
   return e.sale_weight;
});

var ctx = document.getElementById('producermarketweight90').getContext('2d');
var config = {
   type: 'line',
   data: {
      labels: labels,
      datasets: [{
         label: 'Weight',
         data: value,
         backgroundColor: 'rgba(35,139,69,1)'
      },
      ]
   },
   options: {
            responsive: true,
            title: {
               display: true,
               text: ''
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
                     labelString: 'Weight offered (Kg)'
                  }
               }]
            }
         }
};

var chart = new Chart(ctx, config);})
