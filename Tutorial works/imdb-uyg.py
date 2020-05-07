import pandas as pd 

df = pd.read_csv("datasets/imdb.csv")
results = df
results = df.columns #show colmuns

results = df.head(5)    #first n rows
results = df.head(10)

results = df.tail(5)    #last n rows
results = df.tail(10)

results = df["Movie_Title"] # recors of the selected column
results = df["Movie_Title"][:5] # records of the selected column till nth record

results = df[["Movie_Title","Rating"]].head(5)
results = df[["Movie_Title","Rating"]].tail(7)

results = df[5:10][["Movie_Title","Rating"]].head()
results = df[df["Rating"] >= 8][["Movie_Title","Rating"]].head(50)
results = df[(df["YR_Released"]>= 2014) & (2015> df["YR_Released"])]
results = df[(df["Num_Reviews"] > 100000) | (( 8 <= df["Rating"]) & (df["Rating"] <= 9 ))]







print(results)




