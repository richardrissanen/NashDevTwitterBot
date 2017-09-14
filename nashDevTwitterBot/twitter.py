from config import App
import tweepy

__consumer_key = App.config('twitter', 'consumer_key')
__consumer_secret = App.config('twitter', 'consumer_secret')
__access_token = App.config('twitter', 'access_token')
__access_token_secret = App.config('twitter', 'access_token_secret')

def create_message(start_datetime, title, location, url):
  return start_datetime.strftime('%I:%M%p') + ' ' + title + ' at ' + location + ' ' + url

def post(message):
  auth = tweepy.OAuthHandler(Twitter.__consumer_key, Twitter.__consumer_secret)
  auth.set_access_token(Twitter.__access_token, Twitter.__access_token_secret)

  api = tweepy.API(auth)

  api.update_status(message)
