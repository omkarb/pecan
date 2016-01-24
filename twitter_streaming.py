# Import the necessary methods from tweepy library
from tweepy import StreamListener
from tweepy import TweepError
from tweepy import OAuthHandler
from tweepy import Stream

# Libraries to actually collect tweet data
import multiprocessing
import api_key
import threading
from decimal import Decimal, ROUND_DOWN

# Sentiment Analysis lib
import indicoio

# Allows for verification certificate
import urllib3
import certifi
import warnings
warnings.filterwarnings("ignore")

https = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED', # Force certificate check.
    ca_certs=certifi.where(),  # Path to the Certifi bundle.
)

# You're ready to make verified HTTPS requests.
try:
    r = https.request('GET', 'https://api.twitter.com')
except urllib3.exceptions.SSLError as e:
    print()

# User credentials to access Twitter API
access_token = api_key.token
access_token_secret = api_key.token_secret
consumer_key = api_key.consumer_key
consumer_secret = api_key.consumer_secret

# key_term = 'nba'
indicoio.config.api_key = api_key.indico_key
tweets_data = []
sentiments = []
sent = indicoio.sentiment_hq

# def newTerm(str):
#     key_term = str

sentiment_value = 0

# This is a basic listener that just prints received tweets to stdout. ft. Drake
class StdOutListener(StreamListener):

    def on_status(self, status):
        global sentiment_value
        body = status.text
        s = indicoio.sentiment_hq(body)
        s = Decimal(s).quantize(Decimal('.0001'), rounding=ROUND_DOWN)
        sentiments.append(s)
        sentiment_value = (sum(sentiments) / len(sentiments))

    def on_error(self, status_code):
        print("Error:", status_code)


# Connect to Twitter Stream
def twitter_connection():
    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except TweepError as err:
        message = "Error: " + err
        return message


def main(query):
    auth = twitter_connection()
    l = StdOutListener()
    stream = Stream(auth, l)
    # This line filters Twitter Streams to capture data by the desired keywords
    stream.filter(track=[query])


def timed_process(query):
    t = threading.Thread(target=main, args=(query,))
    t.start()
    t.join(5)
    print(sentiment_value)
    return sentiment_value
