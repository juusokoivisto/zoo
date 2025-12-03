"""
OOP Zoo Example featuring two classes and multiple objects
"""
import os
import random

class Zoo:
    """Zoo class. Used to generate zoo objects that contain animal objects in a list."""
    _id_counter = 0

    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        """Adds the specified animal to the zoo
        Parameters:
        - animal
        """
        self.animals.append(animal)
        animal.id = self._id_counter
        self._id_counter += 1

        self.animals_action()

    def animals_action(self):
        """Makes each animal do a random action"""
        for _temp_animal in self.animals:
            functions = [_temp_animal.eat, _temp_animal.sleep, _temp_animal.drink]
            random.choice(functions)()

    def remove_animal(self, animal_id):
        """Removes the specified animal from the zoo
        Parameters:
        - animal
        """
        if animal_id is None:
            print("Animal Id does not exist.")
            return

        for zoo_animal in self.animals:
            if zoo_animal.id == animal_id:
                self.animals.remove(zoo_animal)

    def display_animals(self):
        """Displays the animals in the zoo
        Parameters:
        - none.
        """
        if not self.animals:
            os.system("cls")
            print("Your zoo is empty.")
            return

        print("Animals in the zoo: ")
        for animal in self.animals:
            print(animal)

    def get_animal(self, animal_id):
        """Returns an animal based on their id"""
        for zoo_animal in self.animals:
            if zoo_animal.name == animal_id:
                return zoo_animal

        return None
