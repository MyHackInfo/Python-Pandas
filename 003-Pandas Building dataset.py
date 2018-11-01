import quandl
import pandas as pd
api_key=open('apikeys.txt','r').read()

df=quandl.get('FMAC/HPI_AK', authtoken=api_key)
print(df.head())


