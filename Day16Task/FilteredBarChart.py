#7. Filtered Bar Chart 
#Scenario: 
#marks = np.array([45, 80, 60, 30, 90]) 
#names = ["A", "B", "C", "D", "E"] 
#Task: 
#● Convert to DataFrame 
#● Filter students with marks > 50 
#● Plot bar chart only for filtered students



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
marks = np.array([45, 80, 60, 30, 90]) 
names = ["A", "B", "C", "D", "E"]
df=pd.DataFrame({'Name':names,'Marks':marks})
filtered_df=df[df['Marks']>50]
plt.bar(filtered_df['Name'],filtered_df['Marks'],color='skyblue')
plt.xlabel('student name')
plt.ylabel('Marks')
plt.title('Student with marks > 50')
plt.show()

