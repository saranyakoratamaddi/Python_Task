#2. Monthly Sales Analysis
#Scenario:
#sales = np.array([100, 150, 200, 180, 220, 300])
#months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
#Task:
#● Create DataFrame
#● Plot:
#○ Line graph → sales trend
#○ Bar chart → month-wise comparison
#○ Pie chart → contribution of each month
#○ Histogram → frequency of sales values
#○ Scatter plot → month index vs sales



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df = pd.DataFrame({"Months": months, "Sales": sales})
print(df)
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
plt.bar(months, sales)
plt.title("Month Wise Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
plt.pie(sales, labels=months, autopct="%1.1f%%")
plt.title("Monthly Sales Contribution")
plt.show()
plt.hist(sales, bins=5)
plt.title("Sales Distrubution")
plt.xlabel("Sales")
plt.ylabel("Count")
plt.show()
plt.scatter(range(len(sales)), sales)
plt.title("Index vs Slaes")
plt.xlabel("Index")
plt.ylabel("Sales")
plt.show()
