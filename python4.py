import numpy as np
import pandas as pd
ip=np.array([10,20,30,40])
s=pd.Series(ip)
print(s)

s=np.array([10,20,20,9,4,4,6,5,7,7,9,9,9,])
i=pd.Index(s)
print(i.value_counts())

p=np.array
k=pd.Series(4[66,32,46,84,46])
print(k)

#data frames
import pandas as pd
data=pd.DataFrame([["chattu","harsha"],[17,19]],columns=["names","age"])
print(data)

#data frames using dictinory
import pandas as pd
dat={"names":['x','y','z'],
     "age":[10,13,33]}

p=pd.DataFrame(dat)
print(p)



#data frames and series using csv file
import pandas as pd

Data = pd.read_csv("C:/Users/SPTINT-17/Desktop/data/iris.csv")

s=pd.Series(Data["Species"])
print(s)

df=pd.DataFrame(Data['Species'],Data['PetalWidthCm'])
print(df)
