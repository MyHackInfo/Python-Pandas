import pandas as pd

df1=pd.DataFrame({'Name':['narsi','jeetu','bob'],
                  'Age':[21,20,25]})


df2=pd.DataFrame({'Name':['chris','mark','bob'],
                  'Age':[24,22,23]})

# concatenating dataframe
#con=pd.concat([df1,df2])
#print(con)


# Appending dataframe
app=df1.append(df2)
print(app)
