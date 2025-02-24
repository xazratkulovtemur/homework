import json
import random

import json
import random

# Farm Model
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def walk(self):
        print(f"{self.name} is walking around.")

    def make_sound(self):
        print(f"{self.name} makes a generic animal sound.")

class Cow(Animal):
    def produce_milk(self):
        print(f"{self.name} is producing milk.")
        return 10  # Represents 10 liters of milk

    def make_sound(self):
        print(f"{self.name} says Moo!")

class Chicken(Animal):
    def lay_egg(self):
        print(f"{self.name} laid an egg.")
        return 1  # Represents 1 egg

    def make_sound(self):
        print(f"{self.name} says Cluck!")

class Sheep(Animal):
    def produce_wool(self):
        print(f"{self.name} is producing wool.")
        return 5  # Represents 5 units of wool

    def make_sound(self):
        print(f"{self.name} says Baa!")

# Farm Management
class Farm:
    def __init__(self):
        self.animals = []
        self.bank = Bank()

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the farm.")

    def list_animals(self):
        if not self.animals:
            print("No animals on the farm.")
        else:
            for animal in self.animals:
                print(f"{animal.name}, Age: {animal.age}, Type: {type(animal).__name__}")

    def farm_produce(self):
        earnings = 0
        for animal in self.animals:
            if isinstance(animal, Cow):
                earnings += animal.produce_milk() * 2  # $2 per liter of milk
            elif isinstance(animal, Chicken):
                earnings += animal.lay_egg() * 0.5  # $0.5 per egg
            elif isinstance(animal, Sheep):
                earnings += animal.produce_wool() * 3  # $3 per wool unit
        if earnings > 0:
            self.bank.deposit_to_farm(earnings)
        else:
            print("No products were collected.")