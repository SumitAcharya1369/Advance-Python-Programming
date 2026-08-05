# Creating a simple class in Python
class Person:
    def __init__(self):
        self.name = "ABCD"
    def display(self):
        print("Name:", self.name)
p = Person()
p.display()            


# Creating a class with parameters in Python
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
p = Person("EFGH", 25)
p.display()            

# Creating a class with methods in Python
class Person:   
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
    def greet(self):
        print("Hello,", self.name)

p = Person("EFGH", 25)
p.display()
p.greet()


# Creating a class with class variables in Python
class Library:
    books = "Collection of books"
    def __init__(self,id,name):
        self.id = id
        self.name = name
    
    def display(self):
        print("Library:", self.books)
        print("Library ID:", self.id)
        print("Library Name:", self.name)
l = Library(1, "City Library")
l.display()        


#
collect = "Collection of books"
class Library:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    
    def display(self):
        print("Library:", collect)
        print("Library ID:", self.id)
        print("Library Name:", self.name)
k = Library(1, "City Library")
k.display()        

# Creating a class with inheritance in Python
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Student(Person):
    def __init__(self,name,age,roll_no):
        self.name = name
        self.age = age  
        self.roll_no = roll_no
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age) 
        print("Roll No:", self.roll_no)
s = Student("IJKL", 20, 101)
s.display()

# Creating a class with hierarchy in Python
class Teacher(Student):
    def __init__(self,name,age,roll_no,salary):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.salary = salary
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Salary:", self.salary)
t = Teacher("QRST", 40, 101, 50000)
t.display()