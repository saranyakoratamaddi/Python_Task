#9. Multi-Department Data Aggregation 
#A company collects employee counts from two branches. 
#Branch A: 
#[[10, 20], 
#[30, 40]]
#Branch B: 
#[[5, 15], 
#[25, 35]] 
#Scenario: 
#● Combine the two matrices. 
#● Calculate the total employees across all departments. 
#● Print the combined matrix and total.






import numpy as np
branch1=np.array([[10, 20],[30, 40]])
branch2=np.array([[5, 15],[25, 35]])
print("Branch A",branch1)
print("Branch B",branch2)
combined=branch1+branch2
print("Combined matrix",combined)
totalemp=np.sum(combined)
print("Total Employees:",totalemp)
