class Dog:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("I can walk")
        
class Alligator:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("I can crawl")

Sam = Dog("Sam")
Enika = Alligator("Enika")

animals = (Sam, Enika)

for animal in animals:
    animal.move()