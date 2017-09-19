from config import App
from datetime import datetime, timezone, timedelta, date

__timezone_offset = App.config('time', 'timezone_offset')
__end_of_day_offset = App.config('time', 'end_of_day_offset')

def current_time():
  tz = __timezone()
  return datetime.now(tz)

def end_of_day():
  tz = __timezone()
  return datetime.now(tz) + timedelta(hours=__end_of_day_offset)

def get_datetime(start_time_string):
  return datetime.strptime(start_time_string, "%Y-%m-%d%H:%M:%S%z")

def sanitize(start_time_string):
  return start_time_string.replace('T', '').replace('-05:00', '-0500').replace('-06:00', '-0600') # -06:00 == bad data

def __timezone():
  delta = timedelta(hours=__timezone_offset)
  return timezone(delta)
