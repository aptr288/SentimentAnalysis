import re
import urllib.request
import os
from bs4 import BeautifulSoup
import pandas as pd
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

cwd = os.getcwd()
path = str(cwd) + "\\files\\Reactions.csv"
df = pd.read_csv(path, header=None)

def clean_tweet(tweet):
    if tweet.startswith("https://t.co/"):
        soup = BeautifulSoup(urllib.request.urlopen(tweet), features="lxml")
        tweet = soup.title.string
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def analize_sentiment(tweet):
    analyser = SentimentIntensityAnalyzer()

    score = analyser.polarity_scores(tweet)
    scoreExact = score['compound']
    if(scoreExact < -0.9 and scoreExact >= -1 ):
        y = -0.9
    elif (scoreExact < -0.8 and scoreExact >= -0.9):
        y = -0.8
    elif (scoreExact < -0.7 and scoreExact >= -0.8):
        y = -0.7
    elif (scoreExact < -0.6 and scoreExact >= -0.7):
        y = -0.6
    elif (scoreExact < -0.5 and scoreExact >= -0.6):
        y = -0.5
    elif (scoreExact < -0.4 and scoreExact >= -0.5):
        y = -0.4
    elif (scoreExact < -0.3 and scoreExact >= -0.4):
        y = -0.3
    elif (scoreExact < -0.2 and scoreExact >= -0.3):
        y = -0.2
    elif (scoreExact < -0.1 and scoreExact >= -0.2):
        y = -0.1
    elif (scoreExact < 0 and scoreExact >= -0.1):
        y = 0
    elif (scoreExact < 0.1 and scoreExact >= 0):
        y = 0.1
    elif (scoreExact < 0.2 and scoreExact >= 0.1):
        y = 0.2
    elif (scoreExact < 0.3 and scoreExact >= 0.2):
        y = 0.3
    elif (scoreExact < 0.4 and scoreExact >= 0.3):
        y = 0.4
    elif (scoreExact < 0.5 and scoreExact >= 0.4):
        y = 0.5
    elif (scoreExact < 0.6 and scoreExact >= 0.5):
        y = 0.6
    elif (scoreExact < 0.7 and scoreExact >= 0.6):
        y = 0.7
    elif (scoreExact < 0.8 and scoreExact >= 0.7):
        y = 0.8
    elif (scoreExact < 0.9 and scoreExact >= 0.8):
        y = 0.9
    elif(scoreExact < 1 and scoreExact >= 0.9 ):
        y = 1
    return scoreExact, y


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

                sentiment, sentimentRoundedOff = analize_sentiment(cleaned_element)
                row_list.append(sentimentRoundedOff)
                print(count)
                tweetReplyDict[count] = row_list

df_clean = pd.DataFrame.from_dict(tweetReplyDict,orient='index')

df_clean.to_csv('files\\Replies.csv',header=False)