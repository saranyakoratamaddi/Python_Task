#1. Student Performance Dashboard
#Scenario: A school records marks of students in one subject:
#marks = np.array([45, 67, 89, 56, 72, 91, 38])
#students = ["A", "B", "C", "D", "E", "F", "G"]
#Task:
#● Convert to Pandas DataFrame
#● Plot:
#○ Line graph → trend of marks
#○ Bar chart → student vs marks
#○ Pie chart → Pass (>50) vs Fail
#○ Histogram → distribution of marks
#○ Scatter plot → index vs marks



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students= ["A","B","C","D","E","F","G"]
df= pd.DataFrame({"Students": students,"Marks": marks})
print(df)
plt.plot(students, marks, marker='o')
plt.title("Students Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
plt.bar(students, marks)
plt.title("Students vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
pass_count = sum(marks > 50)
fail_count = sum(marks <= 50)
plt.pie([pass_count, fail_count],label=["Pass", "Fail"], autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()
plt.hist(marks, bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Count")
plt.show()
plt.scatter(range(len(marks)), marks)
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.show()
