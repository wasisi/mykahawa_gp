$.getJSON('/topproducerweight/?format=json', function(jsonfile){


var labels = jsonfile.map(function(e) {
   return e.producer_name;
});
var sum = jsonfile.map(function(e) {
   return e.sum_weight;
});

var ctx = document.getElementById('topproducerweight').getContext('2d');
var config = {
   type: 'bar',
   data: {
      labels: labels,
      datasets: [
      {
         label: 'Sum',
         data: sum,
         backgroundColor: 'rgba(186,228,179,1)'
      },
      ]
   },
   options: {
            responsive: true,
            title: {
               display: true,
               text: 'Top 10 coffee growers during the last 365 days'
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
                     labelString: 'Coffee Grower'
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