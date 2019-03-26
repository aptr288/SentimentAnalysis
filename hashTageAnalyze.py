

import sys
import jsonpickle
import os
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
                     wait_on_rate_limit_notify=True,retry_count=100,retry_delay=10)

    return api
api = get_auth()
searchQuery = '#wall'  # this is what we're searching for
maxTweets = 10000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'tweets.txt' # We'll store the
# tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# file = "5_twitterBBC.csv"
# f = open(file, "w")
# Headers = "tweet_user, tweet_text,  replies,  retweets\n"
# f.write(Headers)
# url = "https://twitter.com/realDonaldTrump/status/1092787440560078849"
# html = urlopen(url)
# soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())
# # Gets the tweet
# tweets = soup.find_all("li", attrs={"class":"js-stream-item"})

# # Writes tweet fetched in file
# for tweet in tweets:
#     try:
#         if tweet.find('p',{"class":'tweet-text'}):
#             tweet_user = tweet.find('span',{"class":'username'}).text.strip()
#             tweet_text = tweet.find('p',{"class":'tweet-text'}).text.encode('utf8').strip()
#             replies = tweet.find('span',{"class":"ProfileTweet-actionCount"}).text.strip()
#             retweets = tweet.find('span', {"class" : "ProfileTweet-action--retweet"}).text.strip()
#             # String interpolation technique
#             f.write(f'{tweet_user},/^{tweet_text}$/,{replies},{retweets}\n')
#     except: AttributeError
# f.close()

