#5. Store Sales Comparison 
#Tw stores record daily sales for 3 days. 
#Scenario: 
#Store A = [200, 250, 300] 
#Store B = [180, 270, 310] 
#Task: 
#● Store them in NumPy arrays. 
#● Find the daily difference in sales between the two stores. 
#● Print the resulting array.






import numpy as np
arr1=np.array([200, 250, 300])
arr2=np.array([180, 270, 310])
print("Store A Daily sales:",arr1)
print("Store B daily sales:",arr2)
result=arr1-arr2
print("Diffence between two stores:",result)

