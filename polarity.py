import re
import urllib.request

from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv("Reactions.csv", header=None)
# df_clean = pd.DataFrame().reindex_like(df)

#Cleans the tweets by removing user name and irrelavent non alphabetic data
def clean_tweet(tweet):
    if tweet.startswith("https://t.co/"):
        soup = BeautifulSoup(urllib.request.urlopen(tweet),features="lxml")
        tweet = soup.title.string
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


# returns compound sentiment of tweet rounding off to 1, 0 -1
def analize_sentiment_decision(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    # analysis = TextBlob(tweet)
    # if analysis.sentiment.polarity > 0:
    #     return 1
    # elif analysis.sentiment.polarity == 0:
    #     return 0
    # else:
    #     return -1

    analyser = SentimentIntensityAnalyzer()

    score = analyser.polarity_scores(tweet)
    # print(score['compound'])
    if(score['compound'] >= 0.05):
        return 1
    elif(score['compound'] > -0.05 and score['compound'] < 0.05):
        return 0
    else:
        return -1

#returns compound sentiment of tweet as is
def analize_sentiment_compound(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    # analysis = TextBlob(tweet)
    # if analysis.sentiment.polarity > 0:
    #     return 1
    # elif analysis.sentiment.polarity == 0:
    #     return 0
    # else:
    #     return -1

    analyser = SentimentIntensityAnalyzer()

    score = analyser.polarity_scores(tweet)
    return score['compound']

tweetReplyDict = defaultdict(list)


for index, row in df.iterrows():
    row_list = 0
    key = ''
    for indexRow,elements in enumerate(row):

        if indexRow == 0:
            key = clean_tweet(elements)
            continue

        if(pd.isnull(elements)):
            continue
        else:
            cleaned_element = clean_tweet(elements)
            # print(cleaned_element)
            row_list += analize_sentiment_decision(cleaned_element)

    tweetReplyDict[key] = row_list

print(tweetReplyDict)
