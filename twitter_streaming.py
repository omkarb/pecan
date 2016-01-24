# Import the necessary methods from tweepy library
from functools import reduce
from tweepy import StreamListener
from tweepy import TweepError
from tweepy import OAuthHandler
from tweepy import Stream

# Libraries to actually collect tweet data
import multiprocessing
import twitter_api_data
import time
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
api_key = twitter_api_data.indico_key
access_token = twitter_api_data.access_token
access_token_secret = twitter_api_data.access_token_secret
consumer_key = twitter_api_data.consumer_key
consumer_secret = twitter_api_data.consumer_secret

key_term = 'nba'
indicoio.config.api_key = api_key
tweets_data = []
sentiments = []
sent = indicoio.sentiment_hq

# def newTerm(str):
#     key_term = str


# This is a basic listener that just prints received tweets to stdout. ft. Drake
class StdOutListener(StreamListener):



    def on_status(self, status):
        body = status.text
        s = indicoio.sentiment_hq(body)
        s = Decimal(s).quantize(Decimal('.0001'), rounding=ROUND_DOWN)
        sentiments.append(s)
        print(sum(sentiments) / len(sentiments))



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


def main(key_term):
    auth = twitter_connection()
    l = StdOutListener()
    stream = Stream(auth, l)
    # This line filters Twitter Streams to capture data by the desired keywords
    stream.filter(track=[key_term])



if __name__ == '__main__':
    p = multiprocessing.Process(target=main, name="main")
    p.start()
    time.sleep(10)
    p.terminate()
    p.join()
