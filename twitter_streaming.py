# Twitter streaming code attributable to Adil Moujahid

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "4837759413-IV38kwcsAvn6BLTzFd6dEeAmR3ekrpjgsvXRMl9"
access_token_secret = "z7q4rpWi0q2FlBx5jFiOoBqNSXdY2uCr1hkYwHuMtWGCd"
consumer_key = "WA6bPuRDmKX59h7bSkV4ecPxl"
consumer_secret = "C16BN5ibCnlZcYStqJBaVb48u9DZXS7f2oPNk9S7jj1vEjjVOI"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])