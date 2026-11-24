#4. Find Maximum Value 
#arr = np.array([12, 45, 22, 67, 34]) 
#Task: 
#● Convert to Pandas Series 
#● Find the maximum value




import numpy as np
import pandas as pd
arr = np.array([12, 45, 22, 67, 34])
s=pd.Series(arr)
max_val=s.max()
print("Panda Series")
print(s)
print("Maximum Value",max_val)
