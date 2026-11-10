---
layout: base
title: Subscribe to MyKahawa
permalink: node/subscribe.html
hero: true
heading: "Subscribe"
description: "Get MyKahawa updates on Kenyan coffee prices, market reports and directory changes by email."
lead: "Get updates on Kenyan coffee prices, new market reports and directory changes, and be matched with potential partners."
---
{%- comment -%}
The old Mailchimp list no longer exists (its signup URL returns 404).
Until a new mailing list service is chosen, sign-ups arrive by email.
{%- endcomment -%}
<div class="container mk-section mk-prose">
  <form id="subscribe-form" class="mk-chart-card" novalidate>
    <div class="form-group">
      <label for="sub-name">Your name</label>
      <input type="text" id="sub-name" class="form-control" autocomplete="name">
    </div>
    <div class="form-group">
      <label for="sub-org">Organisation, company or cooperative <span class="text-muted">(optional)</span></label>
      <input type="text" id="sub-org" class="form-control" autocomplete="organization">
    </div>
    <div class="form-group">
      <label for="sub-role">I am a…</label>
      <select id="sub-role" class="form-control">
        <option>Coffee farmer or cooperative</option>
        <option>Estate owner or manager</option>
        <option>Exporter, dealer or roaster</option>
        <option>Miller, marketing agent or warehouseman</option>
        <option>Researcher or development organisation</option>
        <option>Government or regulator</option>
        <option>Other</option>
      </select>
    </div>
    <button type="submit" class="btn mk-btn-accent">Subscribe by email</button>
    <p class="mk-note mt-3 mb-0">This opens your email app with a message to <a href="mailto:wasisi.coffee@gmail.com?subject=Subscribe%20to%20MyKahawa">wasisi.coffee@gmail.com</a>. Just press send. We only use your email to send MyKahawa updates; see our <a href="/node/privacy.html">privacy policy</a>.</p>
  </form>
</div>

<script>
  document.getElementById('subscribe-form').addEventListener('submit', function (e) {
    e.preventDefault();
    var v = function (id) { return document.getElementById(id).value.trim(); };
    var body = 'Please subscribe me to MyKahawa updates.\n\n' +
      'Name: ' + v('sub-name') + '\n' +
      'Organisation: ' + v('sub-org') + '\n' +
      'I am a: ' + v('sub-role') + '\n';
    location.href = 'mailto:wasisi.coffee@gmail.com?subject=' + encodeURIComponent('Subscribe to MyKahawa') +
      '&body=' + encodeURIComponent(body);
  });
</script>
