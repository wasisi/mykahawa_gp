$.getJSON('/countyprice/?format=json', function(jsonfile){


var labels = jsonfile.map(function(e) {
   return e.county_name;
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

var ctx = document.getElementById('countyprices').getContext('2d');
var config = {
   type: 'bar',
   data: {
      labels: labels,
      datasets: [
      {
         label: 'Min',
         data: min,
         backgroundColor: 'rgba(186,228,179,1)'
      },
      {
         label: 'Ave',
         data: ave,
         backgroundColor: 'rgba(116,196,118,1)'
      },
      {
         label: 'Max',
         data: max,
         backgroundColor: 'rgba(35,139,69,1)'
      },
      ]
   },
   options: {
            responsive: true,
            title: {
               display: true,
               text: 'Minimum, Average and Maximum Price (USD $ per 50 Kg bag) per county during the last 365 days'
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
                     labelString: 'Price (USD $)'
                  }
               }]
            }
         }
};

var chart = new Chart(ctx, config);})