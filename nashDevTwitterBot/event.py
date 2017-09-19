from config import App
import nashDevTwitterBot.timer as timer
import feedparser
import re

class Event:

  __url = App.config('events_url')
  __content_key = App.config('parser', 'content_key')
  __content_value = App.config('parser', 'content_value')
  __listings_key = App.config('parser', 'listings_key')
  __start_key = App.config('parser', 'start_key')
  __title_key = App.config('parser', 'title_key')
  __url_key = App.config('parser', 'url_key')


  def __init__(self, start, title, url, location):
    self.start = start
    self.title = title
    self.url = url
    self.location = location

  @classmethod
  def get_all(self):
    parsed_feed = feedparser.parse(Event.__url)
    listings = parsed_feed[Event.__listings_key]

    events_array = []

    for listing in listings:
      start_time_string = listing[Event.__start_key]
      start_time_string = timer.sanitize(start_time_string)
      start_datetime = timer.get_datetime(start_time_string)

      title = listing[Event.__title_key]
      url = listing[Event.__url_key]

      content = listing[Event.__content_key][0][Event.__content_value]
      location = self._parse_location(content)

      new_event = Event(start_datetime, title, url, location)

      events_array.append(new_event)

    return events_array

  @staticmethod
  def _parse_location(content):
    r = re.compile('fn org\\\'>.*')
    match = r.search(content)

    location = ''

    if match:
      matched_string = match.group()
      prefix = re.compile('fn org\\\'>')
      postfix = re.compile('</span>')
      new_content = prefix.sub("", matched_string)
      location = postfix.sub("", new_content)

    return location
