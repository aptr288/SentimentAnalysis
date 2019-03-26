'''
TODO: Using emoticons
TODO: Focusing on single tweet
TODO:

'''
import sys
# General:
from collections import defaultdict
import json
import matplotlib
import tweepy  # To consume Twitter's API
import pandas as pd  # To handle data
import numpy as np  # For number computing

# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
# matplotlib inline

import tweepy
from tweepy import OAuthHandler
import json

from textblob import TextBlob
import re

from retrying import retry
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
                     wait_on_rate_limit_notify=True,retry_count=100,retry_delay=10)

    return api
api = get_auth()
tweetReplyDict = defaultdict(list)
# retry with interverls to tackle issue like 429 exception
#@retry(wait_exponential_multiplier=100, wait_exponential_max=1000)
def get_replies(TweetId,UserId):


    replies = []
    # repliesToParticularTweet = []
    # non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    tweet = api.get_status(TweetId, tweet_mode='extended')
    tweetContent = tweet.full_text
    print(tweetContent)
     #, max_id = '1094633257377787904', since = '2019-02-09'
    for searchreply in tweepy.Cursor(api.search, q='to:'+UserId,max_id = 1107408129619382277, since_id=TweetId, tweet_mode='extended').items(10000):
        if (searchreply, 'in_reply_to_status_id_str'):
            if (searchreply.in_reply_to_status_id_str == tweet.id_str):
                replies.append(searchreply.full_text)

    tweetReplyDict[tweetContent] = replies
    return tweetReplyDict

reply = get_replies(1107385751577088000, 'realDonaldTrump')

print("------------")
dt = pd.DataFrame.from_dict(reply, orient='index')
print(dt)

if not (dt.empty ):
    if(len(dt.columns)>450):
        with open('data.json', mode='a+') as fp:
            json.dump(reply, fp)
            dt.to_csv("Reactions.csv", mode='a', header=False)







