import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df[['math score', 'reading score', 'writing score']])

print(df[ 'writing score'].dtype)

print(df[ 'writing score'].count())

print(df.info())

print(df.shape)

print(df.tail())
