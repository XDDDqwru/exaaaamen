import pandas as pd
df = pd.read_csv('StudentsPerformance.csv') 

print(df[['gender', 'math score', 'lunch']].head(12))
print(df[['gender', 'math score', 'lunch']].shape)
print(df[['gender', 'math score', 'lunch']].tail(8))
print(df.dtypes)
