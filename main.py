from libs import Twitter, Event, Timer

# Fetches and parses Feed
events = Event.get_all()

# CDT
current_time = Timer.current_time()
end_of_day = Timer.end_of_day()

# Iterates over events, compares start time to eod and current time, and posts the events to twitter
for event in events:
  event_start = event.start

  if event_start > current_time and event_start < end_of_day:
    message = Twitter.create_message(event_start, event.title, event.location, event.url)
    Twitter.post(message)
