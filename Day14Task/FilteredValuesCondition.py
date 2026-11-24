#5. Filter Values Using Condition 
#arr = np.array([10, 25, 30, 15, 40]) 
#Task: 
#● Convert to Pandas Series 
#● Filter values greater than 20




import numpy as np
import pandas as pd
arr = np.array([10, 25, 30, 15, 40])
df=pd.Series(arr)
filtered=df[df>20]
print("Filtered Values greater than 20:",df)
