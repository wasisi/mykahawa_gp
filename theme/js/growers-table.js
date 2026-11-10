/* Searchable growers directory.
 * Expects: <table id="growers-table" data-src="/data/growers/growers.json"> with an empty <tbody>,
 * plus #growers-q (text), #growers-type, #growers-county (selects), #growers-count, #growers-more.
 * URL parameters ?q=, ?type= and ?county= pre-fill the filters (used by the homepage search).
 */
(function () {
  'use strict';
  var table = document.getElementById('growers-table');
  if (!table) return;

  var PAGE = 50;
  var tbody = table.querySelector('tbody');
  var q = document.getElementById('growers-q');
  var type = document.getElementById('growers-type');
  var county = document.getElementById('growers-county');
  var count = document.getElementById('growers-count');
  var more = document.getElementById('growers-more');
  var rows = [], matches = [], shown = 0;

  var params = new URLSearchParams(location.search);
  if (params.get('q')) {
    // A search for a county name (e.g. ?q=nyeri) shows the growers in that county.
    var wanted = params.get('q').trim().toLowerCase();
    var match = Array.prototype.filter.call(county.options, function (o) { return o.value && o.value.toLowerCase() === wanted; })[0];
    if (match) county.value = match.value; else q.value = params.get('q');
  }
  if (params.get('type')) type.value = params.get('type');
  if (params.get('county')) county.value = params.get('county');

  function cell(tr, text, cls) {
    var td = document.createElement('td');
    if (cls) td.className = cls;
    td.textContent = text || '';
    tr.appendChild(td);
    return td;
  }

  function render(reset) {
    if (reset) { tbody.textContent = ''; shown = 0; }
    var frag = document.createDocumentFragment();
    matches.slice(shown, shown + PAGE).forEach(function (g) {
      var tr = document.createElement('tr');
      var name = cell(tr, '');
      var link = document.createElement('a');
      link.href = g.u;
      link.textContent = g.n;
      name.appendChild(link);
      if (g.a) {
        var aff = document.createElement('div');
        aff.className = 'small text-muted';
        aff.textContent = g.a;
        name.appendChild(aff);
      }
      cell(tr, g.t);
      cell(tr, g.k);
      cell(tr, g.c);
      var mapCell = cell(tr, '');
      if (g.m && window.mkGrowersMap) {
        var b = document.createElement('button');
        b.type = 'button';
        b.className = 'btn btn-sm btn-outline-secondary';
        b.textContent = 'Show on map';
        b.setAttribute('aria-label', 'Show ' + g.n + ' on the map');
        b.addEventListener('click', function () { window.mkGrowersMap.show(g.i); });
        mapCell.appendChild(b);
      }
      frag.appendChild(tr);
    });
    tbody.appendChild(frag);
    shown = Math.min(shown + PAGE, matches.length);
    count.textContent = matches.length
      ? 'Showing ' + shown + ' of ' + matches.length + ' growers'
      : 'No growers match your search.';
    more.hidden = shown >= matches.length;
  }

  function filter() {
    var text = q.value.trim().toLowerCase();
    var t = type.value, k = county.value;
    matches = rows.filter(function (g) {
      if (t && g.t !== t) return false;
      if (k && g.k !== k) return false;
      if (text && (g.n + ' ' + g.c + ' ' + g.a + ' ' + g.k).toLowerCase().indexOf(text) === -1) return false;
      return true;
    });
    render(true);
  }

  fetch(table.getAttribute('data-src'))
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (data) { rows = data; filter(); })
    .catch(function () { count.textContent = 'Sorry, the growers list could not be loaded.'; });

  var timer;
  q.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(filter, 200); });
  type.addEventListener('change', filter);
  county.addEventListener('change', filter);
  more.addEventListener('click', function () { render(false); });
})();
