import indicoio
import twitter_streaming

indicoio.config.api_key = '5ca05133a5b0124405885e67117e9515'


def returnSentiment(str):
    # List to hold sentiment Values from top tweets
    sentimentValues = []
    twitter_streaming.newTerm(str)
    tweets = twitter_streaming.tweets['text']

    for text in tweets:
        sentimentValues.append(indicoio.sentiment_hq(text))

    sentiment = sum(sentimentValues) / len(sentimentValues)

    return str(sentiment)

# print(indicoio.sentiment_hq('indico is so easy to use!'))

# 0.07062467665597527
