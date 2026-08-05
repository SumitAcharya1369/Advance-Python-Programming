# Overriding 
class Parent:
    def show(self):
        print("This is parent class")
        
class Child(Parent):
    def show(self):
        print("This is child class")
        super().show()

f = Child()
f.show()       