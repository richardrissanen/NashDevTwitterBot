import feedparser
from datetime import datetime, timezone, timedelta, date

from config import App

# Grabs config
events_url = App.config('events_url')

listings_key = App.config('parser', 'listings_key')
url_key = App.config('parser', 'url_key')
start_key = App.config('parser', 'start_key')
title_key = App.config('parser', 'title_key')

timezone_offset = App.config('time', 'timezone_offset')
end_of_day_offset = App.config('time', 'end_of_day_offset')

delta = timedelta(hours=timezone_offset)
tz = timezone(delta)
current_time = datetime.now(tz)
end_of_day = datetime.now(tz) + timedelta(hours=end_of_day_offset)

# Parses Feed
parsed_feed = feedparser.parse(events_url)
event_listings = parsed_feed[listings_key]

# Prints Title, Url and start of events for the current day
for event in event_listings:
  start = event[start_key].replace('T', '').replace('-05:00', '-0500').replace('-06:00', '-0600') # -06:00 was bad data
  start_time = datetime.strptime(start, "%Y-%m-%d%H:%M:%S%z")

  if start_time > current_time and start_time < end_of_day:
    print(event[title_key])
    print(event[url_key])
    print(start_time)
    print(current_time)
