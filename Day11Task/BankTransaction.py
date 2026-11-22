 #1. Bank Transaction Storage 
#A bank stores the transaction amounts of a customer in a list: 
#[1200, 500, 800, 1500] 
#Scenario: 
#● Convert the list into a NumPy array. 
#● Print the type of the object. 
#● Verify that it is a NumPy ndarray.





import numpy as np
trnsc=[1200, 500, 800, 1500]
trnscarr=np.array(trnsc)
print("Type of object:",type(trnscarr))
print("Is Numpy ndarray:",isinstance(trnscarr,np.ndarray))



