---
layout: base
title: Growers
redirect_from: "/directory/producers/"
comments: true
---
<header>
  <div class="container">
    <div class="header-content">
      <h1>Growers</h1>
    </div>
  </div>
</header>

<article>
  <div class="container">
    <div class="row">
      <div class="col-md-8 mx-auto">
        <p class="lead">
          Kenya’s coffee is grown in the highlands between 1400 and 2000 metres above sea level. The main growing areas are around Mt. Kenya, Nakuru and Machakos. Most of Kenya’s coffee is grown on small farms organized into cooperatives and plantation/large estates. According to the Coffee Act (2001), the distinction between small and large farms is determined by the size and ownership of pulping stations. In Kenya, it is estimated that 60% of coffee is produced by smallholder farmers.
        </p>
        {% include ko-fi.html %}
        <h2>Coffee growers</h2>
          <div>
          <a href="/data/growers/coffeegrowers.csv">
            <button>Download CSV</button>
          </a>  
          </div>  
          <div id="coffeegrowerstable"></div>
          <h2>Map showing some coffee growers</h2>
          <p>The map below is mainly for illustrative purposes. Many of the points have been developed using proxy data like schools, county wards, villages, towns and sublocations. Some points have been verified from field visits. Details about location accuracy are available from the <a href="/data/growers/coffeegrowers.csv">growers list download</a>. </p>
          <p>If you wish to contribute to this map and our list of growers e.g. by adding or correcting information,  please send an email to  <a href="mailto:info@mahwa.org?subject=Add%2Fedit%20coffee%20grower%20location">info@mykahawa.org</a>. Remember to add the following details in your email if you have the information: A description of the farm, Grower CBK code, grower name, longitude, latitude and website. If you can't get the longitude and latitude you can send a screenshot or location from https://www.google.com/maps.</p>
          <div id='map' style='width: 700px; height: 525px;'></div><br />
          <button id="fit">Fit map to Kenya</button>
      </div>
    </div>
  </div>

  {% include disqus_comments.html %}
</article>

<link href="https://unpkg.com/tabulator-tables@4.8.1/dist/css/tabulator.min.css" rel="stylesheet">
<script type="text/javascript" src="https://unpkg.com/tabulator-tables@4.8.1/dist/js/tabulator.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/promise-polyfill@8/dist/polyfill.min.js"></script>
<script type="text/javascript" src="/data/growers/coffeegrowers.json"></script>

<script type="text/javascript">	
	var local_data = coffeegrowers_data;  <!-- name inside json file -->
	var table = new Tabulator("#coffeegrowerstable", {
    height:"500px",
		data: local_data,
		ajaxProgressiveLoad:"scroll",
		layout:"fitColumns",
    virtualDomHoz:true,
		columns:[
		{title:"#", formatter:"rownum", align:"center", width:80},
		{title:"Ref",   field:"title"},
		{title:"Grower name",   field:"producer_name"},
    {title:"Category",   field:"actor"},
		],
	});
</script>
 

<script>
	mapboxgl.accessToken = 'pk.eyJ1IjoibXlrYWhhd2EiLCJhIjoiY2tmbXV4bHJ0MDUxZTJybXBsd2JzaDZoeiJ9.8M1YZahCfMJkuGixC3XmVg';
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v11',
center: [38,1],
zoom: 6
});
 
map.on('load', function () {
map.addSource('places', {
'type': 'geojson',
'data': 'data/growers/coffeegrowers_location.geojson'
});
// Add a layer showing the places.
map.addLayer({
'id': 'places',
'type': 'symbol',
'source': 'places',
'layout': {
'text-field': ['get', 'producer_name'],
'text-variable-anchor': ['top', 'bottom', 'left', 'right'],
'text-radial-offset': 0.5,
'text-justify': 'auto',
//if you want to make icon-image generic replace farm with {icon} and add Maki icon name in properties e.g. "icon": "farm"
'icon-image': 'farm-15',
'icon-allow-overlap': true
}
});
 
// When a click event occurs on a feature in the places layer, open a popup at the
// location of the feature, with description HTML from its properties.
map.on('click', 'places', function (e) {
var coordinates = e.features[0].geometry.coordinates.slice();
var description = e.features[0].properties.cbk_growers_code;
 
// Ensure that if the map is zoomed out such that multiple
// copies of the feature are visible, the popup appears
// over the copy being pointed to.
while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
}
 
new mapboxgl.Popup()
.setLngLat(coordinates)
.setHTML(description)
.addTo(map);
});
 
// Change the cursor to a pointer when the mouse is over the places layer.
map.on('mouseenter', 'places', function () {
map.getCanvas().style.cursor = 'pointer';
});
 
// Change it back to a pointer when it leaves.
map.on('mouseleave', 'places', function () {
map.getCanvas().style.cursor = '';
});
});

// Fit to Kenya
document.getElementById('fit').addEventListener('click', function () {
      map.fitBounds([
          [32.958984, -5.353521],
          [43.50585, 5.615985]
      ]);
   });

// Geocoder
var geocoder = new MapboxGeocoder({ // Initialize the geocoder
  accessToken: mapboxgl.accessToken, // Set the access token
  mapboxgl: mapboxgl, // Set the mapbox-gl instance
  marker: false, // Do not use the default marker style
  placeholder: 'Search in Kenya', //Remind users of search limit
  bbox: [32.958984, -5.353521, 43.50585, 5.615985], // Boundary for Berkeley
});

// Add the geocoder to the map
map.addControl(geocoder);

</script>