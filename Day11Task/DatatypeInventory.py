#6. Check Data Type of Inventory Values 
#A warehouse stores product quantities: 
#[10, 20, 30, 40] 
#Task: 
#● Convert it into a NumPy array. 
#● Print the data type (dtype) of the array.




import numpy as np
quantity=[10, 20, 30, 40]
quantityarr=np.array([10, 20, 30, 40])
print("Data Type of the Inventory is:",quantityarr.dtype)
