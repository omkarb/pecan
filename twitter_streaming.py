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
    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)


if __name__ == '__main__':
    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    print("Connected to Twitter")
    stream = Stream(auth, l)
    # This line filters Twitter Streams to capture data by the desired keywords
    stream.filter(track=[key_term])


# Read the tweet data into an array
tweets_data_path = '../data/twitter_data.txt'


# Takes the data from the .txt file and moves it into an array
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

# Create an empty pandas dataFrame
tweets = pd.DataFrame()
# Add the actual tweets to this dataframe, in its own column
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)


print("Debug")
print(tweets['text'])
