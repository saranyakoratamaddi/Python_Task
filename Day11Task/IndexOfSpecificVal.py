#10. Find Indexes of Specific Value 
#A quality check system stores product defect codes: 
#[2, 4, 1, 4, 3, 4, 5] 
#Task: 
#● Find the indexes where value = 4 using NumPy searching.




import numpy as np
defectcode=np.array([2, 4, 1, 4, 3, 4, 5])
index=np.where(defectcode==4)[0]
print("Indexes where value is 4:",index)
