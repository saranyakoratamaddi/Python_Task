#�
#�
#Scenario 1: Basic Data Loading & Cleaning 
#You are given a CSV file containing railway gauge data. 
#�
#�
#Tasks: 
#1. Load the dataset into a Pandas DataFrame. 
#2. Display the first 5 rows and column names. 
#3. Check for missing values and replace them with 0. 
#4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.




import pandas as pd
df=pd.read_csv('railway_gauges.csv')#Loading the dataset into pandas DataFrame
print("Column Names:",df.columns.tolist())
print("\nFirst 5 Rows")
print(df.head())#Gives data of first 5
print("Missing Values before Replacing")
print(df.isnull().sum())
df.fillna(0,inplace=True)
gauge_col=['Year','Broad Gauge','Metre Gauge','Narrow Gauge','Total']#coverting guage names into numeric types
for col in gauge_col:
    df[col]=pd.to_numeric(df[col],errors='coerce').fillna(0)
print("Data Type of all Colums:")
print(df[gauge_col].dtypes)

#�
#�
#Scenario 2: Simple Visualization 
#You want a quick understanding of total railway track growth. 
#�
#�
#Tasks: 
#1. Extract Year and Total columns. 
#2. Plot a line graph showing Total tracks over years. 
#3. Add: 
#○ Title 
#○ X and Y labels 
#4. Identify whether the trend is increasing or decreasing.


import matplotlib.pyplot as plt
years=df['Year']#Extracting Year and tOtal from dataframe
total_tracks=df['Total']
plt.figure(figsize=(10,6))
plt.plot(years,total_tracks,marker='o',linestyle='-',color='blue')
plt.title("Total Railway Track Growth ")
plt.xlabel("Year")
plt.ylabel("Total Railway Tracks")
plt.grid(True)
#Display the Railway Tracks
if total_tracks.iloc[-1]>total_tracks.iloc[0]:
    print("Trend:The Total Railway Track Length is generally increasing over the year")
elif total_tracks.iloc[-1]<total_tacks.iloc[0]:
    print("Trend:The Total Railway Track Length is generally decreasing over the year")
else:
    print("Trend:The Total Railway Track Length is remained constant over the year")


#�
#�
#Scenario 3: Filtering + Bar Chart 
#You are asked to analyze modern railway expansion. 
#�
#�
#Tasks: 
#1. Filter the dataset for years after 2000. 
#2. Select Broad Gauge, Metre Gauge, and Narrow Gauge. 
#3. Plot a grouped bar chart comparing all three gauges. 
#4. Add legend and proper labels. 
#5. Identify which gauge dominates in recent years. 
#�
#�

import pandas as pd
import matplotlib.pyplot as plt
filtered_df=df[df['Year']>2000]#Filter the data set for years after 2000
gauges=['Broad Gauge','Metre Gauge','Narrow Gauge']#Selecting gauges
if not filtered_df.empty:
    df_plot=filtered_df.set_index('Year')[gauges]
    ax=df.plot(kind="bar",figsize=(12,6),width=0.8)
    plt.title("Modern Railway Expansion")
    plt.xlabel('Year',fontsize=12)
    plt.ylabel('Track Length',fontsize=12)
    plt.xticks(rotation=70)
    plt.legend(title='Gauge Type')
    plt.tight_layout()
    latest_year_data=filtered_df.iloc[-1][gauges]
    dominate=latest_year_data.idmax()
    print("Latest Year",filtered_df['Year'].iloc[-1])
    print("Dominant Gauge",dominate)
else:
    print("No data found")

#�
#�
#Scenario 4: Feature Engineering + Pie Chart 
#You want to analyze the contribution of each gauge type. 
#�
#�
#Tasks: 
#1. Calculate total sum of each gauge across all years. 
#2. Create a new structure (Series/DataFrame) for totals. 
#3. Plot a pie chart showing percentage contribution. 
#4. Add percentage labels (autopct). 
#5. Interpret which gauge contributes the most.

gauge_total=df[gauges].sum()#gauges contains all column names creating new structure for all
print("Total Across all years")
print(gauge_total)
plt.figure(figsize=(8,8))
plt.pie(gauge_total,labels=gauge_total.index,autopct='%1.1f%%',startangle=140,colors=['red','blue','green'])
plt.title("Contribution Of Each Gauge Type")
plt.axis('equal') #helps to draw the pie chart as a circle
top_gauge=gauge_total.idxmax()
top_percent=(gauge_total.max()/gauge_total.sum())*100
print(f"Interpretation: {top_gauge} contributes the most , accounting for {top_percent:.1f}% of the total")


#�
#�
#Scenario 5: Advanced Analysis + Multiple Graphs 
#You are asked to perform a complete analysis of railway trends. 
#�
#�
#Tasks: 
#1. Create new columns: 
#○ % Broad Gauge 
#○ % Metre Gauge 
#○ % Narrow Gauge 
#2. Use NumPy (np.diff) to calculate yearly growth of Total tracks. 
#3. Plot: 
#○ Line graph for all gauges
#○ Stacked bar chart showing composition 
#4. Highlight: 
#○ Years with highest growth 
#○ Decline in any gauge 
#5. Provide a final conclusion: 
#�
#�
#“Is the railway system shifting towards a single dominant gauge?”

import numpy as np
gauge_list=['Broad Gauge','Metre Gauge','Narrow Gauge']
df['Total_Tracks']=df[gauge_list].sum(axis=1)
df['Yearly_Growth']=np.diff(df['Total_Tracks'],prepend=np.nan)
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(14,16))
for gauge in gauge_list:
    ax1.plot(df['Year'],df[gauge],marker='o',linewidth=2,label=gauge)
ax1.set_title("Railway Track Trends by gauge over Time")
ax1.set_xlabel('Year')
ax1.set_ylabel('Track Length')
ax1.legend()
ax1.grid(True)
ax2.bar(df['Year'],df['Broad Gauge'],label='Broad Gauge')
ax2.bar(df['Year'],df['Metre Gauge'],bottom=df['Broad Gauge'],label='Metre Gauge')
ax2.bar(df['Year'],df['Narrow Gauge'],bottom=df['Broad Gauge']+df['Metre Gauge'],label='Narrow Gauge')
ax2.set_title("Composition of Railway Gauge by Year")
ax2.set_xlabel('Year')
ax2.set_ylabel('Total Track Length')
ax2.legend()
plt.tight_layout()
plt.show()
max_growth=df['Yealy_Growth'].idmax()
highest_growth_year=df.loc[max_growth,'Year']
highest_growth_val=df.loc[max_growth,'Yearly_Growth']
print(f"Year with highest growth:{highest_growth_year}(+{highest_growth_val:.2f}")
print("Decline Analysis per Gauge")
for gauge in gauge_list:
    change=df[gauge].iloc[-1]-df[gauge].iloc[0]
    if change<0:
        print(f"{gauge} shows an overall decline of {abs(change):.2f}units")
    else:
        print(f"{gauge} shows an overall increase of {change:.2f}units")
broad_share_start=(df['Broad Gauge'].iloc[0]/df['Total_Tracks'].iloc[0])*100
broad_share_end=(df['Broad Gauge'].iloc[-1]/df['Total_Tracks'].iloc[-1])*100
print("********Final Coclusion*******")
print(f"Broad Gauge share changed from{broad_share_start:.1f}% to {broad_share_end:.1f}%")
if broad_share_end>broad_share_start and broad_share_end > 50:
    print("Yes the railway system is clearlyshifting towards Broad Gauge as a single dominant gauge,while metre and Narrow gauges are declining or being phased out")
else:
    print("The data shows mixed growth across gauges rather than a strict shift towards a single dominant gauge.")
    








    













    
