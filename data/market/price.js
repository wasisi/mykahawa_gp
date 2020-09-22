var seriesOptions = [],
    seriesCounter = 0,
    names = ['MIN', 'AVE', 'MAX'];

/**
 * Create the chart when all data is loaded
 * @returns {undefined}
 */
function createChart() {

    Highcharts.stockChart('container_price', {

        rangeSelector: {
            selected: 4
        },

        title: {
            text: 'Price fluctuation comparison (USD/50Kg bag)'
        },

        yAxis: {
            labels: {
                formatter: function () {
                    return (this.value > 0 ? ' + ' : '') + this.value + '%';
                }
            },
            plotLines: [{
                value: 0,
                width: 2,
                color: 'silver'
            }]
        },

        plotOptions: {
            series: {
                compare: 'percent',
                showInNavigator: true
            }
        },

        tooltip: {
            pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
            valueDecimals: 2,
            split: true
        },

        credits: {
            text: 'https://www.mykahawa.org. Powered by Highcharts',
            href: 'https://www.mykahawa.org'
        },

        series: seriesOptions
    });
}

function success(data) {
    var name = this.url.match(/(min|ave|max)/)[0].toUpperCase();
    var i = names.indexOf(name);
    seriesOptions[i] = {
        name: name,
        data: data
    };

    // As we're loading the data asynchronously, we don't know what order it
    // will arrive. So we keep a counter and create the chart when all the data is loaded.
    seriesCounter += 1;

    if (seriesCounter === names.length) {
        createChart();
    }
}

Highcharts.getJSON(
    '/data/market/price_min.json',
    success
);
Highcharts.getJSON(
    '/data/market/price_ave.json',
    success
);
Highcharts.getJSON(
    '/data/market/price_max.json',
    success
);