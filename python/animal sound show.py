from abc import ABC,abstractmethod

class animal(ABC):
    def __init__(self,name,habitat):
        self.name = name
        self.habitat = habitat
    def display(self):
        print(f"name {self.name} | habitat {self.habitat}")
    @abstractmethod
    def speak(self):
        pass   

#__child class 1_________
class dog(animal):
    def __init__(self,name,habitat,breed):
        super().__init__(name,habitat)
        self.breed = breed
    def speak(self):
        print(f"{self.name} ({self.breed}) says:woof! woof!")    

#__child class 2_________
class parrot(animal):
    def __init__(self,name,habitat,phrase):
        super().__init__(name,habitat)
        self.phrase = phrase
    def speak(self):
        print(f"{self.name} says:{self.phrase}! {self.phrase}!")   

#__child class 3_________
class lion(animal):
    def __init__(self,name,habitat,pride):
        super().__init__(name,habitat)
        self.pride = pride
    def speak(self):
        print(f"{self.name} (pride{self.pride}) says:ROAR!")   

#creating objects
Dog = dog("caramel","home","pomeranian")
Parrot = parrot("titu","jungle","squawk")
Lion = lion("mufassa","savannah","pride rock")  

print("=== animal sound show ===/n")
for animal in [dog , parrot, lion]:
    animal.display()
    animal.speak()
    print()