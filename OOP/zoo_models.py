"""Create a program that models a zoo. The program should have a base class Animal that stores the animal's name, species,
 and number of legs. The class should have a method make_sound that returns a string indicating the sound the animal makes.
 The make_sound method should be overriden in the subclasses to return a sound specific to each type of animal.
Then, create three subclasses of Animal: Mammal, Bird, and Reptile. Each of these subclasses should inherit the name, species,
and number of legs from the Animal class.
For the Mammal class, add a method give_birth and return "Roar" for make_sound method.
For the Bird class, add a method lay_eggs and return "Squawk" for make_sound method.
For the Reptile class, add a method shed_skin and return "Hiss" for make_sound method."""

class Animal:
    name = None
    species = None
    legs = None

    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def make_sound(self):
        pass


class Mammal(Animal):
    def __init__(self, name, species='Mammal', legs= 4):
        super().__init__(name, species, legs)

    def make_sound(self):
        return "Roar"

    def give_birth(self):
        pass


class Bird(Animal):
    def __init__(self, name, species='Bird', legs=2):
        super().__init__(name, species, legs)

    def make_sound(self):
        return "Squawk"

    def lay_eggs(self):
        pass


class Reptile(Animal):
    def __init__(self, name, species='Reptile', legs= 0):
        super().__init__(name, species, legs)

    def make_sound(self):
        return "Hiss"

    def shed_skin(self):
        pass


animals = [Mammal("Lion", "Mammal", 4), Bird("Falcon", "Bird", 2), Reptile("Python", "Reptile", 4)]

for animal in animals:
    print(f"Animal: {animal.name}, Species: {animal.species}, Legs: {animal.legs}, Sound: {animal.make_sound()}")