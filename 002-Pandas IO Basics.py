import pandas as pd
df=pd.read_csv('nuclear.csv')
print(df)

df.set_index('date',inplace=True)
df.to_csv('nuclear2.csv')

df=pd.read_csv('nuclear2.csv')
print(df.head())

df=pd.read_csv('nuclear2.csv', index_col=0)
print(df.head())

df.to_html('nuclearofhtml.html')
