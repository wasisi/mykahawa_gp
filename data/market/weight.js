Highcharts.getJSON('/data/market/weight.json', function (data) {
    // Create the chart
    Highcharts.stockChart('container_weight', {


        rangeSelector: {
            selected: 1
        },

        title: {
            text: 'Weight of coffee sold since 27 January 2015 in kilogrammes (Kg)'
        },

        credits: {
            text: 'https://www.mykahawa.org. Powered by Highcharts',
            href: 'https://www.mykahawa.org'
        },
        
        series: [{
            name: 'Weight (Kg)',
            data: data,
            tooltip: {
                valueDecimals: 0
            }
        }]
    });
});