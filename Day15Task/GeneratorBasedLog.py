#7. Generator-based Log Reader 
#Scenario: 
#A large log file needs to be processed. 
#Task: 
#● Create a generator to read file line by line 
#● Use loop to process logs 
#● Use condition to filter errors 
#● Count occurrences using a dictionary




log_file="sample.log"
def read_log(generatorlog):
    with open("generatorlog.txt","r")as file:
        for line in file:
            yield line.strip()
error_count={}
for log_line in read_log(log_file):
    if "ERROR" in log_line:
        error_count[log_line]=error_count.get(log_line,0)+1
for error,count in error_count.items():
    print(f"{error}:{count}")
        
