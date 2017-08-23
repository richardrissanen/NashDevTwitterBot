class App:
  __config = {
    "events_url": "http://cal.nashvl.org/events.atom",
    "listings_key": "entries",
    "url_key": "link",
    "title_key": "title",
    "start_key": "start_time",
  }

  @staticmethod
  def config(key):
      return App.__config[key]
