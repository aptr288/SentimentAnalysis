import re
import urllib.request

from bs4 import BeautifulSoup
from textblob import TextBlob
import pandas as pd
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv("Reactions.csv", header=None)


# df_clean = pd.DataFrame().reindex_like(df)

def clean_tweet(tweet):
    if tweet.startswith("https://t.co/"):
        soup = BeautifulSoup(urllib.request.urlopen(tweet), features="lxml")
        tweet = soup.title.string
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def analize_sentiment(tweet):
    analyser = SentimentIntensityAnalyzer()

    score = analyser.polarity_scores(tweet)
    return score['compound']


tweetReplyDict = defaultdict(list)
count = 0

for index, row in df.iterrows():
    key = ''
    for indexRow, elements in enumerate(row):
        row_list = []
        if indexRow == 0:
            key = clean_tweet(elements)
            continue

        if(pd.isnull(elements)):
            continue
        else:
            cleaned_element = clean_tweet(elements)
            # print(cleaned_element)

            if(cleaned_element != ''):
                count += 1
                row_list.append(key)
                row_list.append(cleaned_element)

                sentiment = analize_sentiment(cleaned_element)
                row_list.append(sentiment)
                print(count)
                tweetReplyDict[count] = row_list

df_clean = pd.DataFrame.from_dict(tweetReplyDict,orient='index')

df_clean.to_csv('Replies.csv',header=False)