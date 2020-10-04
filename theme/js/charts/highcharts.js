Highcharts.getJSON('https://demo-live-data.highcharts.com/aapl-c.json', function (data) {
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