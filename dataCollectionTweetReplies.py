import sys
import json
import matplotlib
import json
import re
import seaborn as sns
import tweepy  # To consume Twitter's API
import pandas as pd  # To handle data
import numpy as np  # For number computing
import tweepy
# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
from collections import defaultdict
from tweepy import OAuthHandler
from retrying import retry


# Provides user authentication through access tokens and secret keys to get data from Twitter
def get_auth():
    consumer_key = 'qcq2FiLTgjsOiAz7SZSa8NT8Q'
    consumer_secret = 'b4fOmhWboQZkMYFYiWImVxkZUk6AeuK0mRshCrPyNHVnT6sdqL'
    access_token = '619712240-QfErMlhFzeEtK7Ru1cmERKns9WFPDuIXUlHMjEJW'
    access_secret = 'aBouYO4ournJvwuSd4yeSiXHgCrOTaENwY5uURCcp9GX0'

    # auth = OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_secret)
    # api = tweepy.API(auth)
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True, retry_count=100, retry_delay=10)

    return api


api = get_auth()
tweetReplyDict = defaultdict(list)


# retry with interverls to tackle issue like 429 exception
# @retry(wait_exponential_multiplier=100, wait_exponential_max=1000)
# previously retry method is used if time is out but with authentication detail of APP auth it automatically
# wait for some time
def get_replies(TweetId, UserId):
    replies = []
    tweet = api.get_status(TweetId, tweet_mode='extended')
    tweetContent = tweet.full_text
    print(tweetContent)
    # max id helps scrapping so that it provides upper bound for searching and helps scrapp replies in between.
    for searchreply in tweepy.Cursor(api.search, q='to:' + UserId, max_id=1107408129619382277, since_id=TweetId,
                                     tweet_mode='extended').items(10000):
        if (searchreply, 'in_reply_to_status_id_str'):
            if (searchreply.in_reply_to_status_id_str == tweet.id_str):
                replies.append(searchreply.full_text)

    tweetReplyDict[tweetContent] = replies
    return tweetReplyDict


# tweet id for which we want our replies to be scrapped
reply = get_replies(1107385751577088000, 'realDonaldTrump')

print("------------")
dt = pd.DataFrame.from_dict(reply, orient='index')
print(dt)

# saves replies for tweet only if it can scrap more than 450 replies so that minimum number of
# replies are present for each tweet to know how people are reacting to each tweet
if not (dt.empty):
    if (len(dt.columns) > 450):
        with open('data.json', mode='a+') as fp:
            json.dump(reply, fp)
            dt.to_csv("Reactions.csv", mode='a', header=False)
