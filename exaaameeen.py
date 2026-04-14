import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df[['gender', 'race/ethnicity']].head())
print(df[['gender', 'race/ethnicity']].shape)
print(df[['gender', 'race/ethnicity']].tail(10))
