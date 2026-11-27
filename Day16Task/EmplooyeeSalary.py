#3. Employee Salary Insights
#Scenario:
#salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
#departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
#Task:
#● Convert into DataFrame
#● Plot:
#○ Line graph → salary trend
#○ Bar chart → department-wise salary comparison
#○ Pie chart → department distribution
#○ Histogram → salary distribution
#○ Scatter plot → index vs salary


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
df=pd.DataFrame({"Departments": departments,"Salary": salaries})
plt.plot(range(len(salaries)), salaries, marker='o')
plt.title("Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.show()
df.groupby("Department")["Salary"].mean().plot(kind="bar")
plt.title("Department Wise Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()
df["Department"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Department Distribution")
plt.ylabel("")
plt.show()
plt.hist(salaries, bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")
plt.show()
plt.scatter(range(len(salaries)), salaries)
plt.title("Index vs Salary")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.show()
