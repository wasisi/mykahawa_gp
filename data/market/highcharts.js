Highcharts.getJSON('/data/market/price_ave.json', function (data) {
    // Create the chart
    Highcharts.stockChart('container', {


        rangeSelector: {
            selected: 1
        },

        title: {
            text: 'Nairobi Coffee Exchange'
        },

        series: [{
            name: 'Average Price',
            data: data,
            tooltip: {
                valueDecimals: 2
            }
        }]
    });
});