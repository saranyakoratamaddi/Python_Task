#4. Basic File Logger 
#A system logs user actions. 
#Task: 
#● Take user input 
#● Store logs in a file 
#● Use loop to allow multiple entries 
#● Handle file errors using exception handling






try:
    while True:
        log=input("Enter Your action(or 'exit' to 'stop')")
        if log.lower()=="exit":
            print("logging stoped")
            break
        with open("user_logs.txt","a")as file:
            file.write(log+"\n")
        print("Log saved sucessfully")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("PermissionDenined")
except Exception as e:
    print("An Error occured :",e)
                  
