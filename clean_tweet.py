import re
import pandas as pd
from collections import defaultdict
import urllib.request
from bs4 import BeautifulSoup

# url = "BS162NF8HC"
# response = requests.get("https://t.co/" + urllib.parse.quote(url))
# c = response.content

# link = "https://t.co/BS162NF8HC"
# f = requests.head(link)
# print(f.content)
# soup = BeautifulSoup(f.content)
#
# sample = soup.find("title")
# #
# print(soup.prettify())
# print(sample.contents[0])
# print(response.content)

df = pd.read_csv("sample.csv", header=None)
# df_clean = pd.DataFrame().reindex_like(df)

def clean_tweet(tweet):
    if tweet.startswith("https://t.co/"):
        soup = BeautifulSoup(urllib.request.urlopen(tweet),features="lxml")
        tweet = soup.title.string
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

tweetReplyDict = defaultdict(list)


for index, row in df.iterrows():
    row_list = []
    key = ''
    for indexRow, elements in enumerate(row):
        if indexRow == 0:
            key = clean_tweet(elements)
            continue

        if(pd.isnull(elements)):
            continue
        else:
            cleaned_element = clean_tweet(elements)
            # print(cleaned_element)
            row_list.append(cleaned_element)

    tweetReplyDict[key] = row_list

df_clean = pd.DataFrame.from_dict(tweetReplyDict,orient='index')

print(df_clean)

df_clean.to_csv('Cleaned_Reactions.csv',header=False)