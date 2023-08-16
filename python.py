import pandas as pd
Data = pd.read_csv("C:/Users/SPTINT-17/Desktop/data/iris.csv")
print(Data)
print(Data.head(5))
print(Data.tail(2))
print(Data["Species"])
print(Data.info())
print(Data.dtypes)
print(Data.count())
