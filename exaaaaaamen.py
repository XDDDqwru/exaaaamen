import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df[ 'reading score'])


print(df[ 'reading score'].count())
print(df[ 'reading score'].sum())
