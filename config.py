import os

class App:
  __config = {
    'events_url': 'http://cal.nashvl.org/events.atom',
    'parser': {
      'listings_key': 'entries',
      'url_key': 'link',
      'title_key': 'title',
      'start_key': 'start_time',
    },
    'time': {
      'timezone_offset': -5,
      'end_of_day_offset': +15, # this assumes the script runs at 9am
    },
    'twitter': {
      'consumer_key': os.environ['CONSUMER_KEY'],
      'consumer_secret': os.environ['CONSUMER_SECRET'],
      'access_token': os.environ['ACCESS_TOKEN'],
      'access_token_secret': os.environ['ACCESS_TOKEN_SECRET'],
    },
  }

  @staticmethod
  def config(key, key2=False):
    if key2:
      return App.__config[key][key2]
    else:
      return App.__config[key]
