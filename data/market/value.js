Highcharts.getJSON('/data/market/value.json', function (data) {
    // Create the chart
    Highcharts.stockChart('container_value', {


        rangeSelector: {
            selected: 1
        },

        title: {
            text: 'Value of coffee sold since 27 January 2015 in USD'
        },

        credits: {
            text: 'https://www.mykahawa.org. Powered by Highcharts',
            href: 'https://www.mykahawa.org'
        },
        
        series: [{
            name: 'Value (USD)',
            data: data,
            tooltip: {
                valueDecimals: 0
            }
        }]
    });
});