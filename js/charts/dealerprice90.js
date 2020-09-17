$.getJSON('/dealerprice90/?format=json', function(jsonfile){


var labels = jsonfile.map(function(e) {
   return e.title;
});
var min = jsonfile.map(function(e) {
   return e.min_price;
});
var ave = jsonfile.map(function(e) {
   return e.ave_price;
});
var max = jsonfile.map(function(e) {
   return e.max_price;
});

var ctx = document.getElementById('dealerprices90').getContext('2d');
var config = {
   type: 'bar',
   data: {
      labels: labels,
      datasets: [
      {
         label: 'Ave',
         data: ave,
         backgroundColor: 'rgba(116,196,118,1)'
      }
      ]
   },
   options: {
            responsive: true,
            title: {
               display: true,
               text: 'Average Price (USD $ per 50 Kg bag) per Dealer during the last 90 days'
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
                     labelString: 'Dealer'
                  }
               }],
               yAxes: [{
                  display: true,
                  scaleLabel: {
                     display: true,
                     labelString: 'Price (USD $)'
                  }
               }]
            }
         }
};

var chart = new Chart(ctx, config);})