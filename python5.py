import pandas as pd
data = {"days":[1,2,3,4,5,6,7,8,9,10],
       "steps":[4335,9552,7332,7862,4504,5335,7552,8332,6504,8965]}
k=pd.DataFrame(data)
k['steps']=k['steps'] + 1000
print(k)


hs= k[k['steps'] > 7000]['days']
print("the days walk more then 7000",hs)
