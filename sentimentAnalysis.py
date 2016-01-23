import indicoio

indicoio.config.api_key = '5ca05133a5b0124405885e67117e9515'


def returnSentiment(str):
    # List to hold sentiment Values from top tweets
    sentimentValues = []

    # Take the given term, and create a twitter search for it

    twitterURL = "https://twitter.com/search?src=typd&q=" + str

    return


print(indicoio.sentiment_hq('indico is so easy to use!'))

# 0.07062467665597527
