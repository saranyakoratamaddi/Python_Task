#6. Multi-Line Graph for Sales Comparison 
#Scenario: 
#data = { 
#"Month": ["Jan", "Feb", "Mar"], 
#"Store_A": [100, 150, 200], 
#"Store_B": [90, 140, 210] 
#} 
#Task: 
#● Create DataFrame 
#● Plot two line graphs on same plot 
#● Add legend





import matplotlib.pyplot as plt
import pandas as pd
data = { "Month": ["Jan", "Feb", "Mar"], "Store_A": [100, 150, 200], "Store_B": [90, 140, 210] }
df=pd.DataFrame(data)
plt.plot(df["Month"],df["Store_A"],marker="o",label="Store_A")
plt.plot(df["Month"],df["Store_B"],marker="s",label="Store_B")
plt.title("Sales Comparision Graph")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()
