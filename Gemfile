source "https://rubygems.org"

# Match the Jekyll version and plugins that GitHub Pages uses to build the site.
# Local preview:  bundle install && bundle exec jekyll serve
gem "github-pages", group: :jekyll_plugins

group :jekyll_plugins do
  gem "jekyll-redirect-from"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
end

# Needed by `jekyll serve` on Ruby 3+
gem "webrick", "~> 1.8"

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]
gem "wdm", "~> 0.1.0" if Gem.win_platform?
