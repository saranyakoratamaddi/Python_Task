#6. Row Selection & Deletion 
#A DataFrame: 
#df = pd.DataFrame({ 
#"A": [10, 20, 30], 
#"B": [5, 15, 25] 
#}, index=["x", "y", "z"]) 
#Task: 
#● Select row with index "y
#● Delete row "x" 
#● Print updated DataFrame





import pandas as pd
df = pd.DataFrame({ 
"A": [10, 20, 30], 
"B": [5, 15, 25] 
}, index=["x", "y", "z"])
print("The original Data Frame:")
print(df)
row_y=df.loc["y"]
print("selected row Y:")
print(row_y)
df=df.drop(["x"])
print("Updated Data Frame")
print(df)
