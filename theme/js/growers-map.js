/* Coffee growers map: Leaflet + OpenStreetMap tiles, no API key needed.
 * Expects: <div id="growers-map" data-src="/data/growers/growers_map.geojson">
 * Optional controls: #map-search, input[name="map-type"], #map-reset, #map-status
 */
(function () {
  'use strict';
  var el = document.getElementById('growers-map');
  if (!el || !window.L) return;

  var COLORS = {
    'Cooperative society': '#b5302e',
    'Factory': '#4b8030',
    'Estate': '#6b3f22',
    'Small estate': '#c27c00',
    'Other': '#5f5750'
  };
  // Kenya's coffee-growing areas (from the data extent, padded a little).
  var COFFEE_AREAS = L.latLngBounds([-4.6, 33.9], [1.9, 40.5]);

  var map = L.map(el, { scrollWheelZoom: false, zoomSnap: 0.5 });
  map.fitBounds(COFFEE_AREAS);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  // Only capture the scroll wheel once the user has interacted with the map.
  map.on('click focus', function () { map.scrollWheelZoom.enable(); });
  map.on('mouseout blur', function () { map.scrollWheelZoom.disable(); });

  var cluster = L.markerClusterGroup({ showCoverageOnHover: false, maxClusterRadius: 45, chunkedLoading: true });
  map.addLayer(cluster);

  var status = document.getElementById('map-status');
  var search = document.getElementById('map-search');
  var typeBoxes = Array.prototype.slice.call(document.querySelectorAll('input[name="map-type"]'));
  var reset = document.getElementById('map-reset');
  var all = [];

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function icon(type) {
    var c = COLORS[type] || COLORS.Other;
    return L.divIcon({
      className: '',
      html: '<span class="mk-dot" style="background:' + c + ';width:14px;height:14px"></span>',
      iconSize: [14, 14],
      iconAnchor: [7, 7],
      popupAnchor: [0, -6]
    });
  }

  function popup(p) {
    return '<strong>' + esc(p.name) + '</strong><br>' +
      esc(p.type) + (p.code ? ' &middot; Growers code ' + esc(p.code) : '') + '<br>' +
      '<span style="color:#5f5750">' +
      (p.verified ? 'Location verified' : 'Approximate location (nearby school, ward or town)') +
      '</span>';
  }

  function say(msg) { if (status) status.textContent = msg; }

  function apply(fit) {
    var q = search ? search.value.trim().toLowerCase() : '';
    var types = typeBoxes.filter(function (b) { return b.checked; }).map(function (b) { return b.value; });
    var shown = all.filter(function (m) {
      var p = m.feature.properties;
      if (types.length && types.indexOf(p.type) === -1) return false;
      if (q && (p.name + ' ' + p.code).toLowerCase().indexOf(q) === -1) return false;
      return true;
    });
    cluster.clearLayers();
    cluster.addLayers(shown);
    say(shown.length + ' of ' + all.length + ' mapped growers shown');
    if (fit && q && shown.length) {
      if (shown.length === 1) {
        cluster.zoomToShowLayer(shown[0], function () { shown[0].openPopup(); });
      } else {
        map.fitBounds(L.featureGroup(shown).getBounds().pad(0.2));
      }
    }
    return shown;
  }

  fetch(el.getAttribute('data-src'))
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (gj) {
      gj.features.forEach(function (f) {
        var c = f.geometry.coordinates;
        var m = L.marker([c[1], c[0]], { icon: icon(f.properties.type), title: f.properties.name, alt: f.properties.name });
        m.feature = f;
        m.bindPopup(popup(f.properties));
        all.push(m);
      });
      apply(false);
    })
    .catch(function () { say('Sorry, the map data could not be loaded.'); });

  var timer;
  if (search) search.addEventListener('input', function () {
    clearTimeout(timer);
    timer = setTimeout(function () { apply(true); }, 250);
  });
  typeBoxes.forEach(function (b) { b.addEventListener('change', function () { apply(false); }); });
  if (reset) reset.addEventListener('click', function () {
    if (search) search.value = '';
    typeBoxes.forEach(function (b) { b.checked = true; });
    apply(false);
    map.closePopup();
    map.fitBounds(COFFEE_AREAS);
  });

  // Let other scripts (the growers table) jump to a grower on the map.
  window.mkGrowersMap = {
    show: function (id) {
      var hit = all.filter(function (m) { return m.feature.properties.id === id; })[0];
      if (!hit) return false;
      if (search) search.value = '';
      typeBoxes.forEach(function (b) { b.checked = true; });
      apply(false);
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      cluster.zoomToShowLayer(hit, function () { hit.openPopup(); });
      return true;
    }
  };
})();
