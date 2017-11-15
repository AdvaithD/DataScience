# A python script that uses twitter to undestand how people are feeling about a given topic
# Why twitter? Its a huge source of sentiment, lots of users, and lots of opinions.

# Sentiment Analysis
# Tokenization: Splitting text into several words or sentences
# Note: Need to register for Twitter's API

import tweepy
from textblob import TextBlob

consumer_key= 'sMq1Yi1aJBt6yPAmlYpVls66G'
consumer_secret= 'J3HnAJ8giDwMzawwbk0MfLM5YrsEuX8UJTUQBG8vrG2lbIyjRh'

access_token='2510050405-EsawvnmcpmpBF7PRJ3u33OUzaZq3EbTFQJWOrHx'
access_token_secret='ky7T9inecZCsF4ElfrnCgH4ihITwWi0q0UqHmJvopY2kR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

public_tweets = api.search('Trump')


# looping through the tweets
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
