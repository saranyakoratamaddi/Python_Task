#4. Temperature Monitoring System
#Scenario:
#temps = np.array([28, 30, 32, 35, 33, 31, 29])
#days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#Task:
#● Create DataFrame
#● Plot:
#○ Line graph → daily temperature trend
#○ Bar chart → day-wise temperature
#○ Pie chart → proportion of high (>30) vs low temps
#○ Histogram → temperature frequency
#○ Scatter plot → day index vs temperature



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
df = pd.DataFrame({"Days": days,"Temperature": temps})
print(df)
plt.plot(days, temps, marker='o')
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()
plt.bar(days, temps)
plt.title("Day Wise Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()
high = sum(temps > 30)
low = sum(temps <= 30)
plt.pie([high, low],labels=["High", "Low"], autopct="%1.1f%%")
plt.title("High vs Low Temperature")
plt.show()
plt.hist(temps, bins=5)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Count")
plt.show()
plt.scatter(range(len(temps)), temps)
plt.title("Day Index vs Temperature")
plt.xlabel("Index")
plt.ylabel("Temperature")
plt.show()
