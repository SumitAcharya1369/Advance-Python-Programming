#Hybride inheritance

class Manager:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Employee:
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
    def display(self):
        print("Employee ID:",self.emp_id)
        print("Salary:",self.salary)        
class Developer(Manager,Employee):
    def __init__(self,name,age,emp_id,salary,language):
        Manager.__init__(self,name,age)
        Employee.__init__(self,emp_id,salary)
        self.language=language
    def display(self):
        Manager.display(self)
        Employee.display(self)
        print("Programming Language:",self.language)
class Tester(Manager,Employee):
    def __init__(self,name,age,emp_id,salary,testing_tool):
        Manager.__init__(self,name,age)
        Employee.__init__(self,emp_id,salary)
        self.testing_tool=testing_tool
    def display(self):
        Manager.display(self)
        Employee.display(self)
        print("Testing Tool:",self.testing_tool)
                           
m = Manager("John",35)
e = Employee(101,50000) 
d = Developer("Alice",28,102,60000,"Python")
t = Tester("Bob",30,103,55000,"Selenium")
m.display() 
e.display()
d.display()
t.display()