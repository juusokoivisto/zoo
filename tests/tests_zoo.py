"""Tests for zoo.py"""
import unittest
from io import StringIO
from unittest.mock import patch
from src.zoo import Zoo
from src.animal import Animal

class TestZoo(unittest.TestCase):
    """Test cases for zoo.py"""
    def setUp(self):
        self.zoo = Zoo("Test Zoo")
        self.test_animal1 = Animal("Mauri", "Lizard", 10)
        self.test_animal2 = Animal("Tirri", "Cat", 5)
        self.test_animal3 = Animal("Niilo", "Dog", 6)

    def test_create_zoo(self):
        """Tests if the zoo has been created successfully and the name is correct."""
        self.assertIsInstance(self.zoo, Zoo)
        self.assertEqual(self.zoo.name, "Test Zoo")

    def test_add_animal(self):
        """Tests if adding animals is successful."""
        self.zoo.add_animal(self.test_animal1)
        self.assertIn(self.test_animal1, self.zoo.animals)

    def test_remove_animal(self):
        """Tests if removing animals is successful."""
        self.zoo.add_animal(self.test_animal1)
        self.zoo.add_animal(self.test_animal2)
        self.zoo.add_animal(self.test_animal3)

        self.zoo.remove_animal(self.test_animal2.id)

        self.assertIn(self.test_animal1, self.zoo.animals)
        self.assertNotIn(self.test_animal2, self.zoo.animals)
        self.assertIn(self.test_animal3, self.zoo.animals)

    def test_list_animals_empty(self):
        """Tests displaying an empty zoo."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.zoo.display_animals()
            self.assertEqual(fake_out.getvalue(), "Your zoo is empty.\n")

    def test_list_animals(self):
        """Tests displaying a zoo with three animals with different names, species and ages."""
        self.zoo.add_animal(self.test_animal1)
        self.zoo.add_animal(self.test_animal2)
        self.zoo.add_animal(self.test_animal3)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.zoo.display_animals()
            self.assertEqual(
                fake_out.getvalue(),
                f"Animals in the zoo: \n"
                f"{self.test_animal1}\n"
                f"{self.test_animal2}\n"
                f"{self.test_animal3}\n"
            )

    def test_list_animals_remove_one(self):
        """Tests displaying a zoo when an animal has been removed."""
        self.zoo.add_animal(self.test_animal1)
        self.zoo.add_animal(self.test_animal2)
        self.zoo.add_animal(self.test_animal3)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.zoo.display_animals()
            self.assertEqual(
                fake_out.getvalue(),
                f"Animals in the zoo: \n"
                f"{self.test_animal1}\n"
                f"{self.test_animal2}\n"
                f"{self.test_animal3}\n"
            )

        self.zoo.remove_animal(self.test_animal2.id)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.zoo.display_animals()
            self.assertEqual(
                fake_out.getvalue(),
                f"Animals in the zoo: \n"
                f"{self.test_animal1}\n"
                f"{self.test_animal3}\n"
            )

if __name__ == '__main__':
    unittest.main()
