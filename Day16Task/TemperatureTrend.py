#4. Temperature Trend Line Plot 
#Scenario: 
#Daily temperatures: 
#temps = np.array([28, 30, 32, 31, 29]) 
#Task: 
#● Convert into Pandas Series 
#● Plot a line graph 
#● Add title and grid



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
temps = np.array([28, 30, 32, 31, 29])
temp_series=pd.Series(temps)
plt.plot(temp_series,marker='o',linestyle='-',color='b')
plt.title("Daily Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature(c)")
plt.grid(True)
plt.show()
        
