from config import App

import feedparser

class Events:

  __url = App.config('events_url')
  __listings_key = App.config('parser', 'listings_key')

  @staticmethod
  def get():
    parsed_feed = feedparser.parse(Events.__url)
    return parsed_feed[Events.__listings_key]

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
  def create_message(start_datetime, title, url):
    return start_datetime.strftime('%I:%M%p') + ' ' + title + ' ' + url

  @staticmethod
  def post(message):
    auth = tweepy.OAuthHandler(Twitter.__consumer_key, Twitter.__consumer_secret)
    auth.set_access_token(Twitter.__access_token, Twitter.__access_token_secret)

    api = tweepy.API(auth)

    api.update_status(message)
