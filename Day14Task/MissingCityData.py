#2. Missing City Data (NaN Handling) 
#A dataset contains city populations: 
#cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000} 
#Scenario: 
#You want data for: 
#["Delhi", "Chennai", "Bangalore"] 
#Task: 
#● Create a Series with the above index 
#● Identify which cities have missing values (NaN)




import pandas as pd
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}
target=["Delhi", "Chennai", "Bangalore"]
city_series=pd.Series(cities,index=target)
print("City Series")
print(city_series)
missing_cities=city_series[city_series.isna()].index.tolist()
print("Cities with missing values:",missing_cities)
