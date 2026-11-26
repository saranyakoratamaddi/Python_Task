#8. Decorator-based Access Control 
#Scenario: 
#Restrict access to certain functions. 
#Task: 
#● Create a decorator to check user role 
#● Use condition inside decorator 
#● Apply decorator to multiple functions 
#● Store roles in a dictionary





user_roles={"Raj":"admin","bob":"editor","charan":"viewer"}
def required_role(allowed_roles):
    def decorator(func):
        def wrapper(username,*args,**kwargs):
            role=user_roles.get(username)
            if role in allowed_roles:
                return func(username,*args,**kwargs)
            else:
                print(f"Acess denied for {username} role: {role} required {allowed_roles}")
        return wrapper
    return decorator
@required_role(["admin"])
def delete_db(username):
    print(f"Database deleted by{username}")
@required_role(["admin","editor"])
def edit_article(username,article_id):
    print(f"Article {article_id} edited by {username}")
@required_role(["admin","editor","viewer"])
def view_dashboard(username):
    print(f"Viewing dashboard as {username}")
delete_db("Raj")
edit_article("bob",101)
view_dashboard("charan")
          
                 
