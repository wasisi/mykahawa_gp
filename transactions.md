---
layout: base
title: Transactions
redirect_from: "/analytics/dashboard/"
redirect_from: "/transactions/list/"
comments: true
---
<header>
  <div class="container">
    <div class="header-content">
      <h1>Transactions</h1>
    </div>
  </div>
</header>

<script src="https://code.highcharts.com/stock/highstock.js"></script>
<script src="https://code.highcharts.com/stock/modules/data.js"></script>
<script src="https://code.highcharts.com/stock/modules/exporting.js"></script>
<script src="https://code.highcharts.com/stock/modules/export-data.js"></script>

<article>
  <div class="container">
    <div class="row">
      <div class="col-md-8 mx-auto">
        <p class="lead">
          The coffee season which is known as the crop year runs from 1st October to 30th September of the following year. This season covers cultural practices, processing and marketing of coffee. Picking of coffee normally happens in December and April. Farmers are required by the Coffee Act to deliver their coffee to co-operative factories for primary processing. The co-operatives subsequently deliver pulped beans to millers for milling and the millers deliver coffee to registered marketing agents. However, some smallholder farmers who are far from cooperative societies use hand pulpers to process their coffee in their farms. Marketing is done through the Nairobi Coffee Exchange by registered marketing agents who are responsible for cleaning, classification and warehousing. 
        </p>  
        <a href="/data/transactions/coffeetransactions.csv">
          <button>Download transactions from 27 January 2015 to 15 September 2020</button>
        </a>
      </div>
      <div>
            
          </div>
    </div>
  </div>
  <div id="container" style="height: 400px; min-width: 310px">
    <script src="/data/market/price_ave.js" type="text/javascript"></script>
  </div>
  <h2>Price comparison</h2>
  <p>Comparison of the price variation from the previous sale</p>
  <div id="container_price" style="height: 400px; min-width: 310px">
    <script src="/data/market/price.js" type="text/javascript"></script>
  </div> 
  <h2>Value of coffee sold</h2>
  <p>Value of coffee sales by date</p>
  <div id="container_value" style="height: 400px; min-width: 310px">
    <script src="/data/market/value.js" type="text/javascript"></script>
  </div> 
  <h2>Weight of coffee sold</h2>
  <p>Weight of coffee sales by date</p>
  <div id="container_weight" style="height: 400px; min-width: 310px">
    <script src="/data/market/weight.js" type="text/javascript"></script>
  </div>    

  <p>The charts above have been developed using data provided by the Nairobi Coffee Exchange. Aggregations have been made which may cause some slight deviations from the numbers provided by the Nairobi Coffee Exchange. Whenever there are deviations, the numbers from the Nairobi Coffee Exchange will prevail.</p>

</article>

{% include disqus_comments.html %}