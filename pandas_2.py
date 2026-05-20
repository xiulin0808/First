import pandas as pd
data1 ={
   "name": ["Apple","Banana","Orange","Mango","Grape","Guava"],
    "age":[30,20,25,60,45,35],
    "score":[100,150,80,60,90,54]
}
df1=pd.DataFrame(data1)
print(df1)
data2=[
    ["Apple",30,100],
    ["Banana",20 ,150],
    ["Orange", 25 ,80 ],
    ["Mango  ",60 , 60 ],
    ["Grape", 45 , 90 ],
    ["Guava ", 35 , 54 ]
]
df2=pd.DataFrame(data2,columns=["name","age","score"])
print(df2)

print(df1.info())
s=(df1.describe().round(2))
print(df1.describe().round(2))
s.to_csv("0520_stock2.csv")
