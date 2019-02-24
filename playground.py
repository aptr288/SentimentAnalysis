print("aaaaaaaaaaaaa")
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
# def get_auth():
#
#     consumer_key = 'qcq2FiLTgjsOiAz7SZSa8NT8Q'
#     consumer_secret = 'b4fOmhWboQZkMYFYiWImVxkZUk6AeuK0mRshCrPyNHVnT6sdqL'
#     access_token = '619712240-QfErMlhFzeEtK7Ru1cmERKns9WFPDuIXUlHMjEJW'
#     access_secret = 'aBouYO4ournJvwuSd4yeSiXHgCrOTaENwY5uURCcp9GX0'
#
#     # auth = OAuthHandler(consumer_key, consumer_secret)
#     # auth.set_access_token(access_token, access_secret)
#     # api = tweepy.API(auth)
#     auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
#
#     api = tweepy.API(auth, wait_on_rate_limit=True,
#                      wait_on_rate_limit_notify=True,retry_count=100,retry_delay=10)
#
#     return api
# api = get_auth()
#
# tweet = api.get_status(1095523879689293825, tweet_mode='extended')
# tweetContent = tweet.full_text
print("tweetContent")