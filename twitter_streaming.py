# Import the necessary methods from tweepy library
from tweepy import StreamListener
from tweepy import TweepError
from tweepy import OAuthHandler
from tweepy import Stream

# Libraries to actually collect tweet data
import pandas as pd
import twitter_api_data

# Sentiment Analysis lib
import indicoio

# User credentials to access Twitter API
api_key = twitter_api_data.indico_key
access_token = twitter_api_data.access_token
access_token_secret = twitter_api_data.access_token_secret
consumer_key = twitter_api_data.consumer_key
consumer_secret = twitter_api_data.consumer_secret

key_term = 'nba'
indicoio.config.api_key = api_key
tweets_data = []
sent = indicoio.sentiment_hq

def newTerm(str):
    key_term = str


# This is a basic listener that just prints received tweets to stdout. ft. Drake
class StdOutListener(StreamListener):
    def on_status(self, status):
        body = status.text
        count = 10

        if count > 0:
            print(indicoio.sentiment_hq(body))
            count -= 1
        else:
            return

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

if __name__ == '__main__':
    auth = twitter_connection()
    l = StdOutListener()
    stream = Stream(auth, l)
    # This line filters Twitter Streams to capture data by the desired keywords
    stream.filter(track=[key_term])


# Create an empty pandas dataFrame
tweets = pd.DataFrame()
# Add the actual tweets to this dataframe, in its own column
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)


# print(tweets['text'])