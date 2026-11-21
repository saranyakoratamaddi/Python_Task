#13. Secure Login System (Decorators) 
#A web application wants to ensure that users are authenticated before accessing sensitive functions. Create a decorator that checks whether the user is logged in before 
#allowing access to a function. 




def login(func):
    def wrapper():
        logged_in=True
        if logged_in:
            print("Access Granted")
        else:
            print("Please login first:")
    return wrapper
@login
def dashboard():
    print("Welcome to the dashboard")
dashboard()  
