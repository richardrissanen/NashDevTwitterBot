import unittest
from config import App
import nashDevTwitterBot.timer as timer
from datetime import datetime, timezone, timedelta, date

class TestTimer(unittest.TestCase):

    def setUp(self):
      self.timezone_offset = App.config('time', 'timezone_offset')
      self.eod_offset = App.config('time', 'end_of_day_offset')
      self.start_time_string = '2017-09-1608:00:00-0500'
      self.string_to_sanitize = '2017-09-16T08:00:00-05:00'

    def tearDown(self):
      self.timezone_offset = None
      self.eod_offset = None
      self.start_time_string = None
      self.string_to_sanitize = None

    def test_current_time(self):
      now = datetime.now(timezone(timedelta(hours=self.timezone_offset)))
      current_time = timer.current_time()
      delta = current_time - now

      self.assertEqual(delta < timedelta(0,0,10000) and delta > timedelta(0,0,0), True)

    def test_end_of_day(self):
      eod = datetime.now(timezone(timedelta(hours=self.timezone_offset))) + timedelta(hours=self.eod_offset)
      timer_eod = timer.end_of_day()
      delta = timer_eod - eod

      self.assertEqual(delta < timedelta(0,0,10000) and delta > timedelta(0,0,0), True)

    def test_get_datetime(self):
      timer_datetime = timer.get_datetime(self.start_time_string)
      self.assertEqual(timer_datetime, datetime(2017, 9, 16, 8, 0, tzinfo=timezone(timedelta(-1, 68400))))

    def test_sanitize_string(self):
      self.assertEqual(timer.sanitize(self.string_to_sanitize), self.start_time_string)
