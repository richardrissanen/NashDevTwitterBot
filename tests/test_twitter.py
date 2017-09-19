import unittest
import nashDevTwitterBot.twitter as twitter
from datetime import datetime, timezone, timedelta, date

class TestTwitter(unittest.TestCase):

  def setUp(self):
    self.start_datetime = datetime(2017, 9, 14, 16, 30, 28, 125303)

  def tearDown(self):
    self.start_datetime = None

  def test_create_message(self):
    message = twitter.create_message(self.start_datetime, 'Event title', 'Emma', 'http://cal.nashvl.org/events')
    self.assertEqual(message, '04:30PM Event title at Emma http://cal.nashvl.org/events' )
