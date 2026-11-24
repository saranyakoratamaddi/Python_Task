#8. Complex DataFrame Transformation 
#A DataFrame: 
#df = pd.DataFrame({ 
#"Name": ["A", "B", "C", "D"], 
#"Marks": [50, 80, 30, 90] }) 
#● Students scoring below 50 failed 
#Task: 
#1. Create a column Status ("Pass"/"Fail") 
#2. Filter only passed students 
#3. Calculate average marks of passed students




import numpy as np
import pandas as pd
df = pd.DataFrame({ 
"Name": ["A", "B", "C", "D"], 
"Marks": [50, 80, 30, 90] }) 
df["Status"]=np.where(df["Marks"]>=50,"Pass","Fail")
passed=df[df["Status"]=="Pass"]
avg=passed["Marks"].mean()
print("Data Frame")
print(df)
print("Passed Students:",passed)
print("Average marks of passed students:",avg)
    
