#1. Monthly Sales Line Graph 
#Scenario: 
#A shop records monthly sales: 
#sales = np.array([100, 150, 200, 250, 300]) 
#months = ["Jan", "Feb", "Mar", "Apr", "May"] 
#Task: 
#● Convert data into a Pandas DataFrame 
#● Plot a line graph 
#● Label X-axis as months and Y-axis as sales






import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
sales = np.array([100, 150, 200, 250, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May"]
df=pd.DataFrame({"Months":months,"Sales":sales})
plt.plot(df["Months"],df["Sales"],marker="o")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()
