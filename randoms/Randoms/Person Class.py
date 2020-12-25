class Person:
    def __init__(self, name):
        self.name = name
    
    
    def talk(self):
        print(f"Hi, I am {self.name}")
        

person1 = Person("John Smith")
person1.talk()

person2 = Person("Bob The Builder")
person2.talk()