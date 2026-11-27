#10. Data Cleaning + Visualization 
#Scenario: 
#data = np.array([100, np.nan, 200, 150, np.nan, 300]) 
#Task: 
#1. Convert to Pandas Series 
#2. Replace NaN with mean 
#3. Plot: 
#○ Line graph of cleaned data 
#○ Bar chart of values > average


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = np.array([100, np.nan, 200, 150, np.nan, 300]) 
series=pd.Series(data)
mean_val=series.mean()
cleaned=series.fillna(mean_val)
print("cleaned series",cleaned)
print(f"Average (mean) : {mean_val}")
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(12,5))
ax1.plot(cleaned.index,cleaned.values,marker='o',color='blue',linestyle='-')
ax1.set_xlabel("Index")
ax1.set_ylabel("Value")
ax1.set_title("Line Graph of cleaned Data")
ax1.grid(True)
above_avg=cleaned[cleaned>mean_val]
ax2.bar(above_avg.index.astype(str),above_avg.values,color='green')
ax2.set_xlabel("Index")
ax2.set_ylabel("Value")
ax2.set_title("Values greater than Average")
plt.tight_layout()
plt.show()



