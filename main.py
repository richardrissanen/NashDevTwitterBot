from nashDevTwitterBot.event import Event
import nashDevTwitterBot.timer as timer
import nashDevTwitterBot.twitter as twitter

# Fetches and parses Feed
events = Event.get_all()

# CDT
current_time = timer.current_time()
end_of_day = timer.end_of_day()

# Iterates over events, compares start time to eod and current time, and posts the events to twitter
for event in events:
  event_start = event.start

  if event_start > current_time and event_start < end_of_day:
    message = twitter.create_message(event_start, event.title, event.location, event.url)
    twitter.post(message)
