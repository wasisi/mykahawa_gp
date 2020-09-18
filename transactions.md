---
layout: base
title: Dealers
---
<header>
  <div class="container">
    <div class="header-content">
      <h1>Transactions</h1>
    </div>
  </div>
</header>

<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
<script src="https://code.highcharts.com/stock/highstock.js"></script>
<script src="https://code.highcharts.com/stock/modules/data.js"></script>
<script src="https://code.highcharts.com/stock/modules/exporting.js"></script>
<script src="https://code.highcharts.com/stock/modules/export-data.js"></script>

<div id="container" style="height: 400px; min-width: 310px">
<script src="/data/market/highcharts.js" type="text/javascript"></script>
</div>

<article>
  <div class="container">
    <div class="row">
      <div class="col-md-8 mx-auto">
        <p class="lead">
          This is what happens at the Nairobi Coffee Exchange
        </p>
      </div>
    </div>
  </div>
  <div class="row">
  <p>test</p>
  <canvas id="marketprices">
   <script src="/data/market/marketprice.js" type="text/javascript"></script>
  </canvas>
</div>
</article>
