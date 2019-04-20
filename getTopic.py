from collections import defaultdict
import os
import pandas as pd
cwd = os.getcwd()
path = str(cwd) + "\\files\\RepliesWithTopicCopy.csv"
df = pd.read_csv(path, header=None,low_memory=False)


tweetReplyDict = defaultdict(list)
count = 0

for index, row in df.iterrows():
    if(index == 0):
        continue
    # print(row[0])

    if(row[4] == "1"):
        row_list = []

        row_list.append(row[0])
        row_list.append(row[1])
        row_list.append(row[2])
        row_list.append(row[3])
        if (row[3][0] == '-'):
            row_list.append("S" + row[3])
        else:
            row_list.append("S+" + row[3])

        count += 1
        row_list.append('T1')
        tweetReplyDict[count] = row_list

    if (row[5] == "1"):
        row_list = []

        row_list.append(row[0])
        row_list.append(row[1])
        row_list.append(row[2])
        row_list.append(row[3])
        if (row[3][0] == '-'):
            row_list.append("S" + row[3])
        else:
            row_list.append("S+" + row[3])

        count += 1
        row_list.append('T2')
        tweetReplyDict[count] = row_list

    if (row[6] == "1"):
        row_list = []

        row_list.append(row[0])
        row_list.append(row[1])
        row_list.append(row[2])
        row_list.append(row[3])
        if (row[3][0] == '-'):
            row_list.append("S" + row[3])
        else:
            row_list.append("S+" + row[3])

        count += 1
        row_list.append('T3')
        tweetReplyDict[count] = row_list

    if (row[7] == "1"):
        row_list = []

        row_list.append(row[0])
        row_list.append(row[1])
        row_list.append(row[2])
        row_list.append(row[3])
        if (row[3][0] == '-'):
            row_list.append("S" + row[3])
        else:
            row_list.append("S+" + row[3])

        count += 1
        row_list.append('T4')
        tweetReplyDict[count] = row_list

    if (row[8] == "1"):
        row_list = []

        row_list.append(row[0])
        row_list.append(row[1])
        row_list.append(row[2])
        row_list.append(row[3])
        if (row[3][0] == '-'):
            row_list.append("S" + row[3])
        else:
            row_list.append("S+" + row[3])

        count += 1
        row_list.append('T5')
        tweetReplyDict[count] = row_list

    if (row[9] == "1"):
        row_list = []

        row_list.append(row[0])
        row_list.append(row[1])
        row_list.append(row[2])
        row_list.append(row[3])
        if (row[3][0] == '-'):
            row_list.append("S" + row[3])
        else:
            row_list.append("S+" + row[3])

        count += 1
        row_list.append('T6')
        tweetReplyDict[count] = row_list

    print(index)

df_clean = pd.DataFrame.from_dict(tweetReplyDict,orient='index')

df_clean.to_csv('files\\RepliesFormatted.csv',header=False)