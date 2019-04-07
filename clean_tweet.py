import re
import pandas as pd
from collections import defaultdict

df = pd.read_csv("sample.csv", header=None)
# df_clean = pd.DataFrame().reindex_like(df)

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

tweetReplyDict = defaultdict(list)


for index, row in df.iterrows():
    row_list = []
    for elements in row:
        print(elements)
        if(pd.isnull(elements)):
            continue
        else:
            cleaned_element = clean_tweet(elements)
            # print(cleaned_element)
            row_list.append(cleaned_element)

    tweetReplyDict[index] = row_list

df_clean = pd.DataFrame.from_dict(tweetReplyDict,orient='index')

print(df_clean)

df_clean.to_csv('Cleaned_Reactions.csv',mode='a',header=False)