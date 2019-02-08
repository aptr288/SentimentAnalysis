'''
TODO: Using emoticons
TODO: Focusing on single tweet
TODO:

'''
import sys
# General:
import matplotlib
import tweepy  # To consume Twitter's API
import pandas as pd  # To handle data
import numpy as np  # For number computing

# For plotting and visualization:
#from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
# matplotlib inline

import tweepy
from tweepy import OAuthHandler
import json

from textblob import TextBlob
import re

# consumer_key = 'qcq2FiLTgjsOiAz7SZSa8NT8Q'
# consumer_secret = 'b4fOmhWboQZkMYFYiWImVxkZUk6AeuK0mRshCrPyNHVnT6sdqL'
# access_token = '619712240-QfErMlhFzeEtK7Ru1cmERKns9WFPDuIXUlHMjEJW'
# access_secret = 'aBouYO4ournJvwuSd4yeSiXHgCrOTaENwY5uURCcp9GX0'
#
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
#
# api = tweepy.API(auth)
#
# tweets = api.user_timeline(screen_name="realDonaldTrump", count=200)
# print("Number of tweets extracted: {}.\n".format(len(tweets)))
#
# # We print the most recent 5 tweets:
# print("5 recent tweets:\n")
# for tweet in tweets[:5]:
#     print(tweet.text.encode('utf-8'))
#
#
# # We create a pandas dataframe as follows:
# data = pd.DataFrame(data=[tweet.text.encode('utf-8') for tweet in tweets], columns=['Tweets'])
# # We display the first 10 elements of the dataframe:
# # display(data.head(10))
#
#
# # print(tweets[0].id)
# # print(tweets[0].created_at)
# # print(tweets[0].source)
# # print(tweets[0].favorite_count)
# # print(tweets[0].retweet_count)
# # print(tweets[0].geo)
# # print(tweets[0].coordinates)
# # print(tweets[0].entities)
#
# data['len']  = np.array([len(tweet.text) for tweet in tweets])
# data['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
# data['Retweets'] = np.array([tweet.retweet_count for tweet in tweets])
#
#
# def clean_tweet(tweet):
#     '''
#     Utility function to clean the text in a tweet by removing
#     links and special characters using regex.
#     '''
#     return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
#
# def analize_sentiment(tweet):
#     '''
#     Utility function to classify the polarity of a tweet
#     using textblob.
#     '''
#     analysis = TextBlob(clean_tweet(tweet))
#     if analysis.sentiment.polarity > 0:
#         return 1
#     elif analysis.sentiment.polarity == 0:
#         return 0
#     else:
#         return -1
#
# # We create a column with the result of the analysis:
# data['Senti Analysis'] = np.array([ analize_sentiment(tweet) for tweet in data['Tweets'] ])
#
# # We display the updated dataframe with the new column:
# display(data.head(10))
#
# data.to_csv("AnalysisFile.csv")


from retrying import retry


# retry with interverls to tackle issue like 429 exception

@retry(wait_exponential_multiplier=100, wait_exponential_max=10000)
def get_replies(TweetId):
    tweetRepdict = {}
    consumer_key = 'qcq2FiLTgjsOiAz7SZSa8NT8Q'
    consumer_secret = 'b4fOmhWboQZkMYFYiWImVxkZUk6AeuK0mRshCrPyNHVnT6sdqL'
    access_token = '619712240-QfErMlhFzeEtK7Ru1cmERKns9WFPDuIXUlHMjEJW'
    access_secret = 'aBouYO4ournJvwuSd4yeSiXHgCrOTaENwY5uURCcp9GX0'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    replies = []
    repliesToParticularTweet = []
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

    for full_tweets in tweepy.Cursor(api.user_timeline, screen_name='realDonaldTrump', timeout=999999).items(10):
        for tweet in tweepy.Cursor(api.search, q='to:realDonaldTrump', since_id=TweetId,
                                   result_type='recent', timeout=999999).items(100):
            if hasattr(tweet, 'in_reply_to_status_id_str'):

                if (tweet.in_reply_to_status_id_str == full_tweets.id_str):
                    replies.append(tweet.text)
                if (tweet.id == TweetId):
                    repliesToParticularTweet.append(tweet.text)
        tweetText = full_tweets.text.translate(non_bmp_map)
        print("Tweet :", tweetText)
        for elements in replies:
            print(elements)
        tweetRepdict[tweetText] = replies
    return tweetRepdict


repliy = get_replies(1092991438579732482)
print("----------------------------")
data = pd.DataFrame()
for key, value in repliy.items():

    data['Tweet'] = key
    data['Reaction'] = ""
    print(key, value)
print("----------------------------")

data.to_csv('CommentFile.csv')

# for friend in tweepy.Cursor(api.search).items():
#     print(json.dumps(friend._json))

# for friend in tweepy.Cursor(api.friends).items():
#     # Process the friend here
#     print(json.dumps(friend._json))


# bluthquotes_tweets = api.user_timeline(screen_name = 'ayushmannk', count = 15)
#
# for status in bluthquotes_tweets:
#     print(status)
