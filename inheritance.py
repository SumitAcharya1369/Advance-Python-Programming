# multilevel Inheritance
class Father:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
f=Father("Odysseus",50)
f.display()    
super = "college"
class Son(Father):
    def __init__(self,name,age,language,colour):
        self.name = name
        self.age = age
        self.language = language
        self.colour = colour

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Language:",self.language)
        print("Colour:",self.clour)
        print("Father's College:",super)
s=Son("Telemachus",20,"Python","Blue")
s.display()


#Multiple Inheritance
class Father:   
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Mother:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Child(Father,Mother):
    def __init__(self,name,age,language,clour):
        self.name = name
        self.age = age
        self.language = language
        self.clour = clour

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Language:",self.language)
        print("Colour:",self.clour)
c = Child("Agamemnon",19,"Python","Blue")
c.display()                        

# Hybrid Inheritance
class Father:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Mother:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Child(Father,Mother):
    def __init__(self,name,age,language,colour):
        self.name = name
        self.age = age
        self.language = language
        self.colour = colour

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Language:",self.language)
        print("Colour:",self.clour)
class GrandChild(Child):
    def __init__(self,name,age,language,clour,school):
        self.name = name
        self.age = age
        self.language = language
        self.clour = clour
        self.school = school

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Language:",self.language)
        print("Colour:",self.clour)
        print("School:",self.school)
c = GrandChild("Agamemnon",19,"Python","Blue","ABC School")
c.display()

#Herarchical Inheritance
class Father:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Son(Father):
    def __init__(self,name,age,language,colour):
        self.name = name
        self.age = age
        self.language = language
        self.colour = colour

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Language:",self.language)
        print("Colour:",self.clour)
p = Son("Telemachus",20,"Python","Blue")
p.display()            