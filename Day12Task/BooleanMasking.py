#11. Boolean Masking for Salary Analysis 
#Scenario: 
#Employee salaries: 
#[25000, 40000, 15000, 50000, 30000] 
#Task: 
#● Filter salaries above 30000. 
#● Count how many employees satisfy this condition.





import numpy as np
salary=np.array([25000, 40000, 15000, 50000, 30000])
print(salary)
high=salary>30000
filtered=salary[high]
count=np.sum(high)
print("Filtered salaries above 30000",filtered)
print("Number of employees",count)
