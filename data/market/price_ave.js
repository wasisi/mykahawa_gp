Highcharts.getJSON('/data/market/price_ave.json', function (data) {
    // Create the chart
    Highcharts.stockChart('container', {


        rangeSelector: {
            selected: 1
        },

        title: {
            text: 'Average prices: 27 January 2015 to 15 September 2020'
        },

        credits: {
            text: 'https://www.mykahawa.org. Powered by Highcharts',
            href: 'https://www.mykahawa.org'
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