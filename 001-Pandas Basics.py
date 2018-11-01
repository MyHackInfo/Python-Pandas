import pandas as pd
import numpy as np

game={'Name':['Gta','Taken','COD','Ops','Car race','Bike race','Pubg'],
       'Level':[20,10,22,25,5,3,8],
       'Rating':[10,6,9,10,6,3,11]}

# 1-store data frame value in variable
df=pd.DataFrame(game)

# 2-Show the result of datafarame
#print(df.head())                   # show only start 5 result
#print(df.tail())                   # show only last 5 result
#print(df.tail(2))                  # puts value need last.
#print(df.sort_values(['Rating']))  # show on base sort_values().
df1=df['Level'].value_counts()      # we can count column value_counts().
print(df1.plot(kind='bar'))

print(df)
#print(df['Name'])
#print(df[['Name','Rating']])

# 3-Change index value on data base.
#print(df.set_index('Name'))
#df.set_index('Rating',inplace=True)
#print(df)

# 4-DataFrame data convert
#print(df.Name.tolist())                    # Single convert
#print(np.array(df[['Name','Level']]))       # Multi convert
