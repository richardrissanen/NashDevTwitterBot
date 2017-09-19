import unittest
from nashDevTwitterBot.event import Event

class TestEvent(unittest.TestCase):

  def test_init(self):
    meetup = Event('04:30pm', 'Event Title', 'http://cal.nashvl.org/events', 'Emma')
    self.assertEqual(meetup.start, '04:30pm')
    self.assertEqual(meetup.title, 'Event Title')
    self.assertEqual(meetup.url, 'http://cal.nashvl.org/events')
    self.assertEqual(meetup.location, 'Emma')
