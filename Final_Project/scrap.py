import tweepy
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
from credentials import *

# API's setup:
# Twitter App access keys for @user
consumer_key = 'MiOGqZIoA779scx9DP7pSeYzM'
consumer_secret = 'e9IurOqeoTPwZyLoChvQXCTo363CYt76Ijjy2EQjtT1F4GiznG'
access_token = '1118579811402825733-7P03ASm89v3EchFleWogbhvcl2U9Wr'
access_token_secret = '6uIksmLCHb1CxeAIBW75hT4I7DQ6jjUGmQkujuR2Wf2Xi'

# get the manipulate right
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# use the user_timeline function to get tweets
last_id = ''
tweets_summary = []
while True:
    try:
        if last_id == '':
            tweets = api.user_timeline(screen_name='realDonaldTrump', count=200)
            last_id = tweets[-1].id
        else:
            tweets = api.user_timeline(screen_name='realDonaldTrump', count=200, max_id=last_id)
            last_id = tweets[-1].id

        tweets_summary.extend(tweets)

    except Exception:
        print("finished")
        break


print("Number of tweets extracted:{}.\n".format(len(tweets_summary)))
# check the things we get
# for tweet in tweets_summary:
#     print(tweet.text)

# create a pandas dataframe as follows:
data = pd.DataFrame(data=[tweet.text for tweet in  tweets_summary], columns=['Tweets'])
data['length'] = np.array([len(tweet.text) for tweet in tweets_summary])
data['ID'] = np.array([tweet.id for tweet in tweets_summary])
data['Date'] = np.array([tweet.created_at for tweet in tweets_summary])
data['Source'] = np.array([tweet.source for tweet in tweets_summary])
data['Likes'] = np.array([tweet.favorite_count for tweet in tweets_summary])
data['RTs'] = np.array([tweet.retweet_count for tweet in tweets_summary])

data.to_csv('tweets.csv')

