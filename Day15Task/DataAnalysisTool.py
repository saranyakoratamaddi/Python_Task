#6. Data Analysis Tool (NumPy + Pandas) 
#Analyze student marks. 
#Task: 
#● Generate marks using NumPy 
#● Convert into Pandas DataFrame 
#● Use conditions to filter passing students 
#● Calculate mean using math/NumPy 
#● Use loop to print results





import numpy as np
import pandas as pd
std_name=['Ram','Krishna','Rahul','Ramya']
marks=np.random.randint(25,100,size=len(std_name))
df=pd.DataFrame({'Student':std_name,'Marks':marks})
print("All Student Marks")
print(df,"\n")
pass_std=df[df['Marks']>=40]
avg=np.mean(df['Marks'])
passing_avg=np.mean(pass_std['Marks'])
print("Passing students(marks>=40)")
for index,row in pass_std.iterrows():
    print(f"Students:{row['Student']}| Marks;{row['Marks']}")
print("class average marks:{avg:.2f}")
print("Passing students avg :",passing_avg)
    
