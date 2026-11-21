#14. Performance Tracker (Decorators) 
#A software team wants to track how long functions take to execute. Create a decorator that measures and prints the execution time of a function.






import time
def performance(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        execution=end-start
        print("Execution time:",execution,"second")
    return wrapper
@performance
def task():
    print("Task is running..")
    time.sleep(2)
task()
