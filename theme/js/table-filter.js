/* Filter the rows of a static table as the user types.
 * <input data-filter-table="table-id" data-filter-count="count-id">
 */
(function () {
  'use strict';
  document.querySelectorAll('input[data-filter-table]').forEach(function (input) {
    var table = document.getElementById(input.getAttribute('data-filter-table'));
    var count = document.getElementById(input.getAttribute('data-filter-count'));
    if (!table) return;
    var rows = Array.prototype.slice.call(table.tBodies[0].rows);
    var noun = input.getAttribute('data-filter-noun') || 'rows';
    function run() {
      var q = input.value.trim().toLowerCase(), n = 0;
      rows.forEach(function (tr) {
        var hit = !q || tr.textContent.toLowerCase().indexOf(q) !== -1;
        tr.hidden = !hit;
        if (hit) n++;
      });
      if (count) count.textContent = q ? n + ' of ' + rows.length + ' ' + noun + ' match' : rows.length + ' ' + noun;
    }
    input.addEventListener('input', run);
    run();
  });
})();
