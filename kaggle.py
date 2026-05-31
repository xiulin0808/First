import numpy as np
import csv

products = []
stock = []
price = []
sales = []

# 讀取 CSV
with open("Data_1.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        products.append(row["Product_Name"])

        stock.append(float(row["Stock_Quantity"]))

        price.append(
            float(
                row["Unit_Price"]
                .replace("$", "")
                .replace(",", "")
            )
        )

        sales.append(float(row["Sales_Volume"]))

# 轉成 NumPy 陣列
products = np.array(products)
stock = np.array(stock)
price = np.array(price)
sales = np.array(sales)

# (1) 每個商品的總庫存價值
inventory_value = stock * price

print("=== 每個商品的總庫存價值 ===")
for i in range(len(products)):
    print(products[i], ":", inventory_value[i])

# (2) 找出最暢銷商品
best_index = np.argmax(sales)

print("\n=== 最暢銷商品 ===")
print("商品名稱：", products[best_index])
print("銷售量：", sales[best_index])

# (3) 計算 9 折後收入
revenue_90 = sales * price * 0.9

total_revenue_90 = np.sum(revenue_90)

print("\n=== 9折後總收入 ===")
print(total_revenue_90)