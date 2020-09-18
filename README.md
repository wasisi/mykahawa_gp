# mykahawa.org


This repo is the mykahawa.org website, based on Jekyll. There are two major steps to building this website`jekyll build` builds the website as a regular Jekyll website.

## Local development

1. Clone this repo
2. Tell git to fetch only the master branch, and not the `gh-pages` branch, which is built automatically and is very big. Edit `.git/config` and change the `fetch` line of the `[remote "origin"]` section to look like this: `fetch = +refs/heads/master:refs/remotes/origin/master`
3. Install Python dependencies: `pip install -r requirements.txt`
4. Install Jekyll: `bundle install`
5. Build the website: `bundle exec jekyll server --watch --incremental`
