'''
TODO: Using emoticons
TODO: Focusing on single tweet
TODO:

'''
import sys
# General:
from collections import defaultdict

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
                     wait_on_rate_limit_notify=True)

    return api

tweetReplyDict = defaultdict(list)
# retry with interverls to tackle issue like 429 exception
#@retry(wait_exponential_multiplier=100, wait_exponential_max=1000)
def get_replies(TweetId,UserId):

    api = get_auth()
    replies = []
    # repliesToParticularTweet = []
    # non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    tweet = api.get_status(TweetId)
    tweetContent = tweet.text
    print(tweetContent)

    for searchreply in tweepy.Cursor(api.search, q='to:'+UserId, since_id=TweetId).items(10000):
        if (searchreply, 'in_reply_to_status_id_str'):
            if (searchreply.in_reply_to_status_id_str == tweet.id_str):
                replies.append(searchreply.text)

    tweetReplyDict[tweetContent] = replies
    return tweetReplyDict

reply = get_replies(1092787440560078849, 'realDonaldTrump')
#reply = get_replies(1093697713395269632,'rajcheerfull')
print("------------")
dt = pd.DataFrame.from_dict(reply, orient='index')
print(dt)
dt.to_csv("Reactions.csv", mode='a', header=False)
    # for full_tweets in tweepy.Cursor(api.user_timeline, screen_name='rajcheerfull', timeout=999999).items(10):
    #     print(full_tweets.text)
        # for tweet in tweepy.Cursor(api.search, q='to:rajcheerfull', since_id=TweetId,
        #                            result_type='recent', timeout=999999).items(1000):
        #     if hasattr(tweet, 'in_reply_to_status_id_str'):
        #
        #         if (tweet.in_reply_to_status_id_str == full_tweets.id_str):
        #             replies.append(tweet.text)
        #         if (tweet.id == TweetId):
        #             repliesToParticularTweet.append(tweet.text)
        # tweetText = full_tweets.text.translate(non_bmp_map)
    #     print("Tweet :", tweetText)
    #     #for elements in replies:
    #
    #         #print(elements)
    #     tweetRepdict[tweetText] = replies
    # return tweetRepdict



