#polymorphism
class Animal:
    def speak(self):
        print("Animal speaks")
        
class Cat(Animal):
    def speak(self):
        print("Cat meows")
        
class Dog(Animal):
    def speak(self):
        print("Dog barks")
for animal in (Animal(), Cat(), Dog()):
    animal.speak()
    