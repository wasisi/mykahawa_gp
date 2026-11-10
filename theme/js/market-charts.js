/* Nairobi Coffee Exchange charts (Chart.js, MIT licence).
 * Data: /data/market/sales.json and /data/market/grade_prices.json, built by scripts/build_data.py.
 * Each chart has a table with the same numbers on the page, for screen readers and exact values.
 */
(function () {
  'use strict';
  if (!window.Chart) return;

  var INK = '#2a2522', MUTED = '#5f5750', GRID = '#ece6df', GREEN = '#4b8030';
  // Categorical slots, fixed order (validated: CVD and normal-vision separation pass on adjacent pairs).
  var GRADE_COLORS = { AA: '#2a78d6', AB: '#eb6834', PB: '#1baf7a', C: '#eda100' };

  Chart.defaults.font.family = "'Source Sans 3', 'Source Sans Pro', Arial, sans-serif";
  Chart.defaults.font.size = 13;
  Chart.defaults.color = MUTED;
  Chart.defaults.maintainAspectRatio = false;
  Chart.defaults.plugins.tooltip.backgroundColor = '#fff';
  Chart.defaults.plugins.tooltip.titleColor = INK;
  Chart.defaults.plugins.tooltip.bodyColor = INK;
  Chart.defaults.plugins.tooltip.borderColor = '#d8d0c7';
  Chart.defaults.plugins.tooltip.borderWidth = 1;
  Chart.defaults.plugins.tooltip.padding = 10;
  Chart.defaults.plugins.tooltip.boxPadding = 4;

  var usd = function (v) { return 'US$' + Math.round(v).toLocaleString('en'); };
  var axis = function (title, extra) {
    var a = { grid: { color: GRID, drawTicks: false }, border: { display: false }, ticks: { padding: 6 },
              title: { display: !!title, text: title, color: MUTED } };
    for (var k in extra) a[k] = extra[k];
    return a;
  };

  // Direct labels at the end of each line, so identity never relies on colour alone.
  var endLabels = {
    id: 'endLabels',
    afterDatasetsDraw: function (chart) {
      if (!chart.options.plugins.endLabels) return;
      var ctx = chart.ctx;
      ctx.save();
      ctx.font = '600 13px ' + Chart.defaults.font.family;
      ctx.fillStyle = INK;
      ctx.textBaseline = 'middle';
      var labels = [];
      chart.data.datasets.forEach(function (ds, i) {
        var meta = chart.getDatasetMeta(i);
        if (meta.hidden) return;
        for (var j = meta.data.length - 1; j >= 0; j--) {
          if (ds.data[j] != null) { labels.push({ text: ds.label, x: meta.data[j].x + 8, y: meta.data[j].y }); break; }
        }
      });
      // Nudge labels apart so lines ending close together stay readable.
      labels.sort(function (a, b) { return a.y - b.y; });
      for (var k = 1; k < labels.length; k++) {
        if (labels[k].y - labels[k - 1].y < 15) labels[k].y = labels[k - 1].y + 15;
      }
      labels.forEach(function (l) { ctx.fillText(l.text, l.x, l.y); });
      ctx.restore();
    }
  };

  function el(id) { return document.getElementById(id); }

  fetch('/data/market/sales.json').then(function (r) { return r.json(); }).then(function (sales) {
    // 1. Average price at each auction
    if (el('chart-price')) new Chart(el('chart-price'), {
      type: 'line',
      data: {
        labels: sales.map(function (s) { return s.date; }),
        datasets: [{ label: 'Average price', data: sales.map(function (s) { return s.price; }),
                     borderColor: GREEN, backgroundColor: GREEN, borderWidth: 2,
                     pointRadius: 0, pointHoverRadius: 5, tension: 0.2 }]
      },
      options: {
        interaction: { mode: 'index', intersect: false },
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: {
            title: function (it) { var s = sales[it[0].dataIndex]; return 'Sale of ' + new Date(s.date).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }); },
            label: function (it) { var s = sales[it.dataIndex]; return [usd(s.price) + ' per 50 kg bag', s.lots.toLocaleString('en') + ' lots, ' + Math.round(s.tonnes).toLocaleString('en') + ' tonnes']; }
          } }
        },
        scales: {
          x: axis('', { grid: { display: false }, ticks: { maxTicksLimit: 8, callback: function (v) { return this.getLabelForValue(v).slice(0, 7); } } }),
          y: axis('US$ per 50 kg bag', { beginAtZero: true })
        }
      }
    });

    // 2. Volume and value by season (two charts - never two y-axes on one)
    var seasons = {}, order = [];
    sales.forEach(function (s) {
      if (!seasons[s.season]) { seasons[s.season] = { t: 0, v: 0 }; order.push(s.season); }
      seasons[s.season].t += s.tonnes; seasons[s.season].v += s.usd;
    });
    var bar = function (id, values, label, fmt) {
      if (!el(id)) return;
      new Chart(el(id), {
        type: 'bar',
        data: { labels: order, datasets: [{ label: label, data: values, backgroundColor: GREEN,
                hoverBackgroundColor: '#3a6425', borderRadius: { topLeft: 4, topRight: 4 }, borderSkipped: 'bottom',
                maxBarThickness: 48 }] },
        options: {
          plugins: { legend: { display: false }, tooltip: { callbacks: { label: function (it) { return fmt(it.raw); } } } },
          scales: { x: axis('Season (Oct–Sep)', { grid: { display: false } }), y: axis(label, { beginAtZero: true }) }
        }
      });
    };
    bar('chart-volume', order.map(function (k) { return Math.round(seasons[k].t); }), 'Tonnes sold',
        function (v) { return v.toLocaleString('en') + ' tonnes'; });
    bar('chart-value', order.map(function (k) { return Math.round(seasons[k].v / 1e5) / 10; }), 'Value (US$ million)',
        function (v) { return 'US$' + v + ' million'; });
  });

  // 3. Average price by grade and season
  if (el('chart-grades')) fetch('/data/market/grade_prices.json').then(function (r) { return r.json(); }).then(function (gp) {
    // Fixed order AA, AB, PB, C so colours and legend never depend on the data order.
    var grades = Object.keys(GRADE_COLORS).map(function (code) {
      return gp.grades.filter(function (g) { return g.grade === code; })[0];
    }).filter(Boolean);
    new Chart(el('chart-grades'), {
      type: 'line',
      plugins: [endLabels],
      data: {
        labels: gp.seasons,
        datasets: grades.map(function (g) {
          var c = GRADE_COLORS[g.grade];
          return { label: g.grade, data: g.prices, borderColor: c, backgroundColor: c, borderWidth: 2,
                   pointRadius: 4, pointHoverRadius: 6, pointBorderColor: '#fff', pointBorderWidth: 2, tension: 0.2 };
        })
      },
      options: {
        layout: { padding: { right: 36 } },
        interaction: { mode: 'index', intersect: false },
        plugins: {
          endLabels: true,
          legend: { position: 'top', align: 'start', labels: { usePointStyle: true, pointStyle: 'circle', boxWidth: 8, color: INK } },
          tooltip: { itemSort: function (a, b) { return b.raw - a.raw; },
                     callbacks: { label: function (it) { return ' ' + it.dataset.label + ': ' + usd(it.raw); } } }
        },
        scales: { x: axis('Season (Oct–Sep)', { grid: { display: false } }), y: axis('US$ per 50 kg bag', { beginAtZero: true }) }
      }
    });
  });
})();
