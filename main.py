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

# Prints Title, Url and start of events for the current day
for event in event_listings:
  start = event[start_key].replace('T', '').replace('-05:00', '-0500').replace('-06:00', '-0600') # -06:00 was bad data
  start_time = datetime.strptime(start, "%Y-%m-%d%H:%M:%S%z")

  if start_time > current_time and start_time < end_of_day:
    title = event[title_key]
    url = event[url_key]

    message = start_time.strftime('%I:%M%p') + ' ' + title + ' ' + url

    Twitter.post(message)
