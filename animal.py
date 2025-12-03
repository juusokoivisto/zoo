"""Animal class that handles an animal"""

import random

class Animal:
    """Animal class. Used to generate Animal objects that contain name, species and age"""
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.id = None

    def __str__(self):
        return f"Id: {self.id}, Species: {self.species}, Age: {self.age}, Name: {self.name}"

    def eat(self):
        """Makes the animal eat"""
        print(f"{self.name} ate.")

    def sleep(self):
        """Makes the animal sleep a random amount"""
        print(f"{self.name} slept for {random.randint(1, 10)} hours.")

    def drink(self):
        """Makes the animal drink"""
        print(f"{self.name} drank.")
