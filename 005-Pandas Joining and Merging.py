import pandas as pd

df1=pd.DataFrame({'Name':['narsi','jeetu','bob'],
                  'Age':[21,20,25]})


df2=pd.DataFrame({'Name':['chris','mark','bob'],
                  'Age':[25,20,23]})


##df1.set_index('Age',inplace=True)
##df2.set_index('Age',inplace=True)
##joins= df1.join(df2,lsuffix='_df1',rsuffix='_df2')
##print(joins)

##merge=pd.merge(df1,df2,on='Age',how='outer')
##merge.set_index('Age',inplace=True)
##print(merge)
