# Twitter streaming code attributable to Adil Moujahid

# Import the necessary methods from tweepy library
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Libraries to actually collect tweet data
import json
import pandas as pd
import twitter_api_data

# Variables that contains the user credentials to access Twitter API
access_token = twitter_api_data.access_token
access_token_secret = twitter_api_data.access_token_secret
consumer_key = twitter_api_data.consumer_key
consumer_secret = twitter_api_data.consumer_secret

key_term = 'nba'

def newTerm(str):
    key_term = str

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        return True

if __name__ == '__main__':
    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the desired keywords
    stream.filter(track=[key_term])

# Read the tweet data into an array
tweets_data_path = '../data/twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)


print(tweets['text'])