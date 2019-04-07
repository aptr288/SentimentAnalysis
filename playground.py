# <<<<<<< HEAD
import pandas as pd
import math

df = pd.read_csv("Reactions.csv")
# df_clean = pd.DataFrame().reindex_like(df)

#print(df)

row_list = []

for index, row in df.iterrows():

    for elements in row:
        if(pd.isnull(elements)):
            continue
        else:
            print(elements)

    # if(row.isna):
    #     continue
    # else:
    #     print(index, row)
def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analize_sentiment(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

#
#
#
# =======
# def intersect(nums1, nums2):
#     intersectList = []
#     for i in nums1:
#         for j in nums2:
#             print("present element")
#             print(i)
#             print("Updated List")
#             print(nums2)
#             if (i == j):
#                 intersectList.append(i)
#                 nums2.remove(j)
#                 break
#         print("Intersection List")
#         print(intersectList)
#     return intersectList
#
# a = [4,9,5,4]
# b = [9,4,9,8,4]
#
# c = intersect(a,b)
# print(c)
# >>>>>>> 61dc7efc2864351b01dea4d1952a48913ed84f0c
