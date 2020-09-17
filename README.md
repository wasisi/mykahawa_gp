# akn.ipbes.net

[![Build Status](https://travis-ci.com/ipbes/akn.ipbes.net.svg?branch=master)](https://travis-ci.com/github/ipbes/akn.ipbes.net)

This repo is the akn.ipbes.net website, based on Jekyll. There are two major steps to building this website:

1. `bin/update.py` is a Python script which pulls by-law information from Laws.Africa and sets up the appropriate Jekyll site structure.
2. `jekyll build` builds the website as a regular Jekyll website.

In production, these two steps are performed by Travis-CI, and the resulting site is force pushed to the `gh-pages` branch as a static website.

## But where is the content?

This repo looks a bit empty, there are no places and by-laws. This saves us from having a repo tracking every change to every by-law. Instead, this repo is fleshed out by Travis-CI during the build phase.

## Local development

1. Clone this repo
2. Tell git to fetch only the master branch, and not the `gh-pages` branch, which is built automatically and is very big. Edit `.git/config` and change the `fetch` line of the `[remote "origin"]` section to look like this: `fetch = +refs/heads/master:refs/remotes/origin/master`
2. Install Python dependencies: `pip install -r requirements.txt`
3. Install Jekyll: `bundle install`
4. Get your Indigo API token from [indigo.akn4undocs.ipbes.net/accounts/profile/api/](https://indigo.akn4undocs.ipbes.net/accounts/profile/api/)
5. `export INDIGO_API_AUTH_TOKEN=your-token`
6. Pull in by-law content for just one region: `bin/update.py --quick un-ipbes`
7. Build the website: `bundle exec jekyll server --watch --incremental`

## Adding a new municipality

1. Add the municipality name, code and by-laws website URL to `_data/places.json`
2. Add the municipality logo and placard images to `img/municipalities/`, using the naming format `<code>-logo.png` and `<code>-placard.jpg`. Note that the two files have different extensions.
3. Push to master
