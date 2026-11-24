#10. Row Filtering + Aggregation 
#A dataset: 
#arr = np.array([ 
#[100, 200], 
#[150, 250], 
#[80, 120], 
#[300, 400] ]) 
#Task: 
#● Convert to DataFrame with columns "Sales", "Profit" 
#● Filter rows where Sales > 100 
#● Find average Profit of filtered rows




import pandas as pd
import numpy as np
arr = np.array([ [100, 200], [150, 250], [80, 120], [300, 400] ])
df=pd.DataFrame(arr,columns=["Sales", "Profit"])
filtered=df[df["Sales"]>100]
avg=filtered["Profit"].mean()
print("Filtered DataFrame:",filtered)
print("Average profit of filtered rows:",avg)
