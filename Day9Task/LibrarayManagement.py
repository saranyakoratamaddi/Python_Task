#16. Library Management System (Constructor & Inheritance) 
#A library stores information about books and digital books. Create a base class Book with a constructor to initialize book details. Create a derived class EBook that adds file 
#size information.





class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def display_info(self):
        print("Title of the Book:",self.title)
        print("Author of the Book:",self.author)
        print("No. of Pages in the book:",self.pages)
class DigitalBook(Book):
    def __init__(self,title,author,pages,file_size):
        self.title=title
        self.author=author
        self.pages=pages
        self.file_size=file_size
    def display_info(self):
        print("Title of the Book:",self.title)
        print("Author of the Book:",self.author)
        print("No. of Pages in the book:",self.pages)
        print("File Size of the digital book :",self.file_size,"MB")
        
b1=DigitalBook("PythonProgramming","John",400,100)
b1.display_info()
    
    
