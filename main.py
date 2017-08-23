import feedparser

from config import App

# Grabs config
events_url = App.config('events_url')
listings_key = App.config('listings_key')
url_key = App.config('url_key')
title_key = App.config('title_key')
start_key = App.config('start_key')

# Parses Feed
parsed_feed = feedparser.parse(events_url)
prased_links = parsed_feed[listings_key]

# Prints Title, Url and start of first event
print(prased_links[0][title_key])
print(prased_links[0][url_key])
print(prased_links[0][start_key])
