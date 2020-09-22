# mykahawa.org
Building up on the Kenya Coffee Directory that was published by the Kenya Coffee Traders Association in 2012 to provide an updated list of Kenya coffee producers and buyers based on transactions reported by the Nairobi Coffee Auction weekly. The website links coffee transactions at the auction to their respective producers and buyers. This will allow farmers and coffee buyers, who depend on intermediaries at the auction, to be able to follow the auction remotely and engage in dialogue to negotiate better deals for themselves.

## What you can find in this repository
You can view and/or download the following lists:
1. Growers: List of cooperatives, estates and factories 
2. Dealers: Companies that have been licensed to purchase coffee at the Nairobi Coffee Exchage
3. Transactions: records of coffee sales at the Nairobi Coffee Exchange from 27 January 2015 to 29 September 2020.
4. General information about coffee in Kenya 

## Local development

This repo is the mykahawa.org website, based on Jekyll. There are two major steps to building this website`jekyll build` builds the website as a regular Jekyll website.

1. Clone this repo
2. Tell git to fetch only the master branch, and not the `gh-pages` branch, which is built automatically and is very big. Edit `.git/config` and change the `fetch` line of the `[remote "origin"]` section to look like this: `fetch = +refs/heads/master:refs/remotes/origin/master`
3. Install Jekyll: `bundle install`
4. Build the website: `bundle exec jekyll server --watch --incremental`
