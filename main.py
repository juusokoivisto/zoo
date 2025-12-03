"""Main handler for the zoo program"""

import os
import animal
import zoo

def print_choices():
    """Print menu navigation choices."""
    print("1. Zoo Details")
    print("2. Add animal")
    print("3. Remove animal")
    print("4. Leave the zoo")

def zoo_details(zoo_obj):
    """Shows all of the zoo animals and their parameters."""
    os.system("cls")

    zoo_obj.display_animals()

def new_animal(zoo_obj):
    """Tries to create a new animal and adds it to the zoo."""
    try:
        os.system("cls")

        new_animal_name = input("Name: ")
        new_animal_species = input("Species: ")
        new_animal_age = int(input("Age: "))

        created_animal = animal.Animal(new_animal_name, new_animal_species, new_animal_age)

        zoo_obj.add_animal(created_animal)
    except ValueError as exc:
        show_error("Age must be a number.", exc)

def remove_animal(zoo_obj):
    """Tries to remove an animal using an id from the zoo."""
    os.system("cls")
    try:
        animal_id = int(input("Animal's Id: "))

        zoo_obj.remove_animal(animal_id)
    except ValueError as exc:
        show_error("ID must be a number.", exc)

def show_error(error_msg, error_exception=None):
    """Prints an error message and the error to the console."""
    os.system("cls")

    print(error_msg)
    if error_exception is not None:
        print(error_exception)

    input("Press Enter to continue...")

def main():
    """Main function. Menu navigation, management."""
    zoo_name = input("Name your zoo: ")
    my_zoo = zoo.Zoo(zoo_name)

    os.system('cls')

    print(f"Welcome to {my_zoo.name}")

    while True:
        print_choices()

        user_input = input("Choice: ")
        try:
            choice = int(user_input)
        except ValueError:
            show_error("Please enter a valid number.")
            continue

        try:
            match choice:
                case 1:
                    zoo_details(my_zoo)
                case 2:
                    new_animal(my_zoo)
                case 3:
                    remove_animal(my_zoo)
                case 4:
                    print("Exiting...")
                    break
                case _:
                    show_error("Invalid choice.")
        except ValueError as exc:
            show_error("Choice must be a number.", exc)

if __name__ == "__main__":
    main()
