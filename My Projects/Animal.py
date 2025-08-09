class Animal:
    def __init__(self,name,age,type):
        self.name = name
        self.age = age
        self.type = type
    
    def display(self):
        print(f"the name is {self.name} and the age is {self.age} and the type is {self.type}")

class Dog(Animal):

    def __init__(self, name, age, type,sound):
       super().__init__(name,age,type)
       self.sound = sound

    def sound_display(self):
        print(f"the sound of {self.name} is {self.sound}")

class Cat(Animal):
    def __init__(self,name,age,type,sound):
        super().__init__(name,age,type)
        self.sound = sound
    def sound_display(self):
        print(f"the sound of {self.name} is {self.sound}")
    

dog1 = Dog("Jimy", 2,"shofu","Houf")
cat1 = Cat("mily", 4,"himila","Miaw")
dog1.display()
