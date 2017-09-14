from config import App

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
      start_time_string = Timer.sanitize(start_time_string)
      start_datetime = Timer.get_datetime(start_time_string)

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

###

from datetime import datetime, timezone, timedelta, date

class Timer:

  __timezone_offset = App.config('time', 'timezone_offset')
  __end_of_day_offset = App.config('time', 'end_of_day_offset')

  @staticmethod
  def current_time():
      tz = Timer.__timezone()
      return datetime.now(tz)

  @staticmethod
  def end_of_day():
    tz = Timer.__timezone()
    return datetime.now(tz) + timedelta(hours=Timer.__end_of_day_offset)

  @staticmethod
  def get_datetime(start_time_string):
    return datetime.strptime(start_time_string, "%Y-%m-%d%H:%M:%S%z")

  @staticmethod
  def sanitize(start_time_string):
    return start_time_string.replace('T', '').replace('-05:00', '-0500').replace('-06:00', '-0600') # -06:00 == bad data

  @staticmethod
  def __timezone():
    delta = timedelta(hours=Timer.__timezone_offset)
    return timezone(delta)

###

import tweepy

class Twitter:

  __consumer_key = App.config('twitter', 'consumer_key')
  __consumer_secret = App.config('twitter', 'consumer_secret')
  __access_token = App.config('twitter', 'access_token')
  __access_token_secret = App.config('twitter', 'access_token_secret')

  @staticmethod
  def create_message(start_datetime, title, location, url):
    return start_datetime.strftime('%I:%M%p') + ' ' + title + ' at ' + location + ' ' + url

  @staticmethod
  def post(message):
    auth = tweepy.OAuthHandler(Twitter.__consumer_key, Twitter.__consumer_secret)
    auth.set_access_token(Twitter.__access_token, Twitter.__access_token_secret)

    api = tweepy.API(auth)

    api.update_status(message)
