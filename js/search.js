ByLawSearch = function() {
  var self = this;

  var $form = $('form#search');
  var $results = $('#search-results');
  var $waiting = $('#search-waiting');
  var template = $('#search-result-tmpl').html();
  var $submit = $form.find('button[type=submit]');
  Mustache.parse(template);
  var places = {};
  REGIONS.forEach(function(p) {
    places[p.code] = p;
  });

  self.search = function() {
    var q = $form.find('input[name=q]').val();
    var region_code = $form.find('input[name=region]').val();
    var params = {};

    $submit.find('.fas').removeClass('d-none');

    $results.hide();
    $waiting.show();

    params = {
      q: q,
      country: 'za',
    };
    
    if (region_code) {
      params.frbr_uri__startswith = '/' + region_code + '/';
    }

    $.getJSON('https://srbeugae08.execute-api.eu-west-1.amazonaws.com/default/searchOpenBylaws', params, function(response, textStatus, jqXHR) {
      var hits = [];
      $submit.find('.fas').addClass('d-none');
      console.log(response);

      response.q = q;
      response.results.forEach(function(result) {
        result.region = places['un-' + result.locality];

        // only keep those with a region
        if (result.region) {
          hits.push(result);

          result.url = (result.region.microsite ? ('https://' + result.region.bucket) : '') +
            result.frbr_uri.slice(4) + "/" + result.language + "/";

          result.snippet = result._snippet
            .replace(/^\s*[;:",.()-]+/, '')  // trim leading punctuation
            .replace(/<b>/g, "<mark>")
            .replace(/<\/b>/g, "</mark>")
            .trim();
        }
      });

      response.hits = {hits: hits};
      response.no_region = region_code === "";
      response.regions = [];
      for (var code in places) {
        var region = places[code];
        region.active = code == region_code;
        response.regions.push(region);
      }

      $results
        .empty()
        .append(Mustache.render(template, response))
        .show();

      $waiting.hide();
    });
  };

  self.submitSearch = function(e) {
    if (window.history.pushState) {
      e.preventDefault();

      // don't reload the whole window
      window.history.pushState(null, null, '?' + $form.serialize());
      self.search();
    }
  };

  self.getParamValue = function(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
  };

  // search term from uri
  self.searchFromUri = function() {
    var q = self.getParamValue('q');
    if (q) {
      $form.find('input[name=q]').val(q);
      $form.find('input[name=region]').val(self.getParamValue('region'));
      $form.submit();
    }
  };

  // handle clicks on a city
  $results.on('click', '.list-group-item', function(e) {
    e.preventDefault();
    $form.find('[name=region]').val($(this).data('code'));
    $form.submit();
  });

  $form.on('submit', self.submitSearch);
  window.onpopstate = self.searchFromUri;

  return self;
};

$(function() {
  var search = new ByLawSearch();
  // kick off a search
  search.searchFromUri();
}); 
