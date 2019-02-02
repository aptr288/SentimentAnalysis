import sys

import tweepy
from tweepy import OAuthHandler
import json


consumer_key = 'HfWdzYAvtsGhMtKS70AZX6HNG'
consumer_secret = 'ignb3qWxcgIcc4nBrFbVlAdtUN86RfR0BvHCCxPDQIHQKCQiEp'
access_token = '619712240-erIcJPx36P6l9KF6ByKXyN3Edf0G8Klidtw9TZcb'
access_secret = '9tgeN58dB1Vc9pvKXhLwtiYFI0xSt1GbxJ2o5T7THrqBK'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# for friend in tweepy.Cursor(api.search).items():
#     print(json.dumps(friend._json))

# for friend in tweepy.Cursor(api.friends).items():
#     # Process the friend here
#     print(json.dumps(friend._json))


# bluthquotes_tweets = api.user_timeline(screen_name = 'ayushmannk', count = 15)
#
# for status in bluthquotes_tweets:
#     print(status)

replies=[]
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

for full_tweets in tweepy.Cursor(api.user_timeline,screen_name='virendersehwag',timeout=999999).items(10):
  for tweet in tweepy.Cursor(api.search,q='to:virendersehwag', since_id=1091797327688450049, result_type='recent',timeout=999999).items(1000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
      if (tweet.in_reply_to_status_id_str==full_tweets.id_str):
        replies.append(tweet.text)
  print("Tweet :",full_tweets.text.translate(non_bmp_map))
  for elements in replies:
       print("Replies :",elements) 
