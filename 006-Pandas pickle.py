import pandas as pd
import pickle

df1=pd.DataFrame({'Name':['narsi','jeetu','bob'],
                  'Age':[21,20,25]})


df2=pd.DataFrame({'Name':['chris','mark','bob'],
                  'Age':[25,20,23]})



merge=pd.merge(df1,df2,on='Age',how='outer')
merge.set_index('Age',inplace=True)
get=merge

# Write data in pickle file
pickle_get=open('mergepickle.pickle','wb')
pickle.dump(get,pickle_get)
pickle_get.close()

# Read data form pickle file
pickle_tak=open('mergepickle.pickle','rb')
get_from_pickle=pickle.load(pickle_tak)

print(get_from_pickle)
print(get)

get_from_pickle.to_pickle('mergepickle.pickle')

data_pickle=pd.read_pickle('mergepickle.pickle')
print(data_pickle)
