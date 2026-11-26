#9. Smart Data Processing Pipeline 
#Scenario: 
#A system processes numeric data from file. 
#Task: 
#● Read numbers from a file 
#● Use NumPy for calculations (mean, std) 
#● Convert results to Pandas DataFrame 
#● Use exception handling for bad data 
#● Use a generator to stream data 
#● Apply decorator to measure execution time;






import time
import numpy as np
import pandas as pd
def measure_time(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"Execution time{end-start:.6f}seconds")
        return result
    return wrapper
def stream_num(dataprocessing):
    try:
        with open("dataprocessing.txt","r")as file:
            for line in file:
                try:
                    yield float(line.strip())
                except ValueError:
                    print(f"Error:{dataprocessing} notfound")
    except FileNotFoundError:
        print("File not found:")
@measure_time
def process_pipeline(dataprocessing):
    data=list(stream_num(dataprocessing))
    if not data:
        print("no valid data")
        return none
    arr=np.array(data)
    status={"count"[arr.size],"mean"[np.mean(arr)],"stddev"[np.std(arr)]}
    df=pd.DataFrame(status)
    return df

    
