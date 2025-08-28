class Animal:
    def moves(self):
        return "All animals move"
    
class Dog(Animal):
    def moves(self):
        return "Dogs move by walking"
    
class Bird(Animal):
    def moves(self):
        return "Birds move by flying"
    
class Locust(Animal):
    def moves(self):
        return "Locusts move by hopping"

dog = Dog()
bird = Bird()
locust = Locust()

animals = [dog, bird, locust]
for x in animals:
    print(x.moves())
