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
print("字典模式前5筆",df1.head())
print("字典模式後五筆",df1.tail())
print("列表模式前5筆",df2.head())
print("列表模式後五筆",df2.tail())
print(df2.info())