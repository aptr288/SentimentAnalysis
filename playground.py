import pandas as pd

df = pd.read_csv("Reactions.csv")

print(df)

for row in df.itertuples():
    for element in row:
        if(pd.isna(element)):
            continue
        else:
            element
            break