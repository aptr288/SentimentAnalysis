import re

from textblob import TextBlob
import pandas as pd
from collections import defaultdict

df = pd.read_csv("sample.csv", header=None)
# df_clean = pd.DataFrame().reindex_like(df)

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analize_sentiment(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

tweetReplyDict = defaultdict(list)


for index, row in df.iterrows():
    row_list = 0
    key = ''
    for index,elements in enumerate(row):

        if(index == 0):
            key = elements
            continue

        if(pd.isnull(elements)):
            continue
        else:
            cleaned_element = clean_tweet(elements)
            # print(cleaned_element)
            row_list += analize_sentiment(cleaned_element)

    tweetReplyDict[key] = row_list

print(tweetReplyDict)