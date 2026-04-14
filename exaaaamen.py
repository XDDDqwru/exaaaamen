import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')     
print(df[['math score', 'reading score', 'writing score']].head(10))
print(df[['math score', 'reading score', 'writing score']].shape)
print("Cantidad:", df['reading score'].count())
print("Suma total:", df['reading score'].sum())