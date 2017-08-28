from datetime import datetime
from config import App
from libs import Twitter, Events, Timer

# Grabs config
url_key = App.config('parser', 'url_key')
start_key = App.config('parser', 'start_key')
title_key = App.config('parser', 'title_key')

# Fetches and parses Feed
event_listings = Events.get()

# CDT
current_time = Timer.current_time()
end_of_day = Timer.end_of_day()

# Iterates over events compares start time to eod and current time and posts the events to twitter
for event in event_listings:
  start_time_string = event[start_key]
  start_time_string = Timer.sanitize(start_time_string)
  start_datetime = Timer.get_datetime(start_time_string)

  if start_datetime > current_time and start_datetime < end_of_day:
    title = event[title_key]
    url = event[url_key]

    message = Twitter.create_message(start_datetime, title, url)

    Twitter.post(message)
