import tweepy
import numpy as np
import pandas as pd


consumer_key = 'MiOGqZIoA779scx9DP7pSeYzM'
consumer_secret = 'e9IurOqeoTPwZyLoChvQXCTo363CYt76Ijjy2EQjtT1F4GiznG'
access_token = '1118579811402825733-7P03ASm89v3EchFleWogbhvcl2U9Wr'
access_token_secret = '6uIksmLCHb1CxeAIBW75hT4I7DQ6jjUGmQkujuR2Wf2Xi'

# API's setup


def twitter_setup():
    """
    Utility function to setup the Twitter's API
    :return: API with authentication
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


public_tweets = twitter_setup().user_timeline('realDonaldTrump', count=200)

data = pd.DataFrame(data=[tweet.text for tweet in public_tweets], columns=['Tweets'])
data['length'] = np.array([len(tweet.text) for tweet in public_tweets])
data['Date'] = np.array([tweet.created_at for tweet in public_tweets])
data['Source'] = np.array([tweet.source for tweet in public_tweets])
data['Likes'] = np.array([tweet.favorite_count for tweet in public_tweets])
data['RTs'] = np.array([tweet.retweet_count for tweet in public_tweets])

print(data.head())

data.to_csv('tweets.csv')

