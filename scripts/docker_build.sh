#!/bin/bash
# Build the site with the same Jekyll version as GitHub Pages, using Docker (no local Ruby needed).
# Output goes to .out/ (gitignored). Usage: scripts/docker_build.sh
set -e
cd "$(dirname "$0")/.."
docker run --rm -v "$PWD":/site -v mykahawa_gems:/usr/local/bundle -w /site ruby:3.3 bash -c "
  bundle install --quiet && bundle exec jekyll build -d /tmp/out 2>&1 &&
  rm -rf /site/.jekyll-cache && mkdir -p /site/.out && find /site/.out -mindepth 1 -delete && cp -r /tmp/out/. /site/.out/ &&
  chown -R $(id -u):$(id -g) /site/.out /site/Gemfile.lock"
