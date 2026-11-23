#1. Sales Threshold Filtering 
#You are given monthly sales: 
#sales = np.array([12000, 18000, 9000, 22000, 15000, 30000]) 
#Task: 
#● Filter all sales values greater than the average sales 
#● Return the filtered array.


import numpy as np
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])
print(sales)
avg=np.mean(sales)
print("Average sales:",avg)
filtered_sales=sales[sales>avg]
print("Sales values greater than average sales:",filtered_sales)
