import pandas as pd
data=pd.read_csv("data.csv")
#print(data)
#print(type(data))
player=data["Player"]
print(player)
print(type(player))
l=["Player","Run"]
player=data[l]
print(player)
print(type(player))
data["newcol"]="New Data"
print(data)
data["newcol"]=data["Run"]**2
data.to_csv("newdata.csv",index=False)
print(data)
del data["newcol"]
print(data)
#print(data[(data["Run"]<=5000) |  ( (data["Run"]<=15000))])