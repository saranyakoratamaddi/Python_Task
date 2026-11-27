#9. Combined Visualization Dashboard 
#Scenario: 
#sales = np.array([100, 200, 150, 300]) 
#products = ["A", "B", "C", "D"] 
#Task: 
#● Create DataFrame 
#● Plot: 
#○ Line graph (trend) 
#○ Bar chart (comparison) 
#○ Pie chart (distribution) 
#● Show all in single figure (subplots)




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sales = np.array([100, 200, 150, 300]) 
products = ["A", "B", "C", "D"] 
df=pd.DataFrame({"Products":products,"Sales":sales})
print("Sales Data")
print(df)
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.plot(products,sales,marker='o')
plt.title('Sales')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.grid(True)
plt.subplot(1,3,2)
plt.bar(products,sales)
plt.title('Product comaparision')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.subplot(1,3,3)
plt.pie(sales,labels=products,autopct='%1.1f%%')
plt.title('Sales Distribution')
plt.tight_layout()
plt.show()

