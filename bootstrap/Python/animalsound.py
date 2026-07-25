from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print(f"{self.name} ({self.breed}) says: Woof!")

class Parrot(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def speak(self):
        print(f"{self.name} ({self.color}) says: Sqwauk!")
class Lion(Animal):
    def __init__(self, name, mane_color):
        super().__init__(name)
        self.mane_color = mane_color
    def speak(self):
        print(f"{self.name} ({self.mane_color}) says: Roar!")

dog = Dog("Buddy", "Labrador")
parrot = Parrot("Mithu", "Green")
lion = Lion("Simba", "Golden")
dog.speak()
parrot.speak()
lion.speak()