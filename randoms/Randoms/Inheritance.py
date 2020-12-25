class Mammal:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        print(f"{self.name} is Walking")

class Dog(Mammal):
    def bark(self):
        print(f"{self.name} says: Bark")
        
class Cat(Mammal):
    def meow(self):
        print(f"{self.name} says: Meow")

koko = Cat("Koko")
raul = Dog("Raul")

koko.walk()
raul.bark()
raul.walk()
koko.meow()