#10. University Staff Management (Hierarchical Inheritance) 
#A university has different staff types such as Professor, LabAssistant, and Administrator. All inherit from a base class Staff. Implement hierarchical inheritance 
#to manage and display their information.





class Staff:
    def __init__(self,name,staff_id,department):
        self.name=name
        self.staff_id=staff_id
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("Staff_id:",self.staff_id)
        print("Department:",self.department)
class Professor(Staff):
    def __init__(self,name,staff_id,department,subject):
        Staff.__init__(self,name,staff_id,department)
        self.subject=subject
    def display_professor(self):
        print("***Professor Details***")
        Staff.display(self)
        print("Subject:",self.subject)
class LabAssistant(Staff):
    def __init__(self,name,staff_id,department,labname):
        Staff.__init__(self,name,staff_id,department)
        self.labname=labname
    def display_labassist(self):
        print("***Lab Assistant***")
        Staff.display(self)
        print("Lab:",self.labname)
class Admin(Staff):
    def __init__(self,name,staff_id,department,role):
        Staff.__init__(self,name,staff_id,department)
        self.role=role
    def display_admin(self):
        print("***Administrator Details***")
        Staff.display(self)
        print("Role:",self.role)
prof=Professor("Dr.Chandrashekhar",26009,"Computer Science","Software Development")
lab=LabAssistant("Kiran",56465,"Computer Science","Data Structures")
ad=Admin("Sushma","l097","Administration","Admissions")
prof.display_professor()
lab.display_labassist()
ad.display_admin()


    
