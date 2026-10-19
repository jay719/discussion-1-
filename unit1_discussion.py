"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    category = "Character"
    def __init__ (self,name,level):
        self.name = name
        self.level = level
    def display_character_info(self):
        return f"{self.name} is a level {self.level} character."
    # Allow the mage to pick up new inventory items
    def add_item(self, item):
        self.inventory.append(item)
        return f"{self.name} picked up {item}!"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    character_type = "Mage"
    def __init__(self,name, level, spell, inventory):
        super().__init__(name, level)
        self.spell = spell
        self.inventory = inventory
    def cast_spell(self):
        return f"{self.name} casts {self.spell}!"
    def display_character_info(self):
        return f"{self.name} is a level {self.level} mage who uses {self.spell}."


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    # Create Characters
    mage1 = ChildClass("Cyclone", 10, "Tornado", ["Healing Potion","Staff"])
    mage2 = ChildClass("Goat", 8, "BAAAAD Day", ["Mana Potion","Staff"])

    #Display Character type information
    print("Character type from class:", ChildClass.character_type)
    print("Character type from mage1:", mage1.character_type)

    # Manipulate the previously made mage by giving it a nickname
    mage1.nickname = "The Banished One"

    # Display the attributes belonging to each character
    print("Cyclone's attributes:", mage1.__dict__)
    print("Goat's attributes:", mage2.__dict__)

    # Display the attributes and methods belonging to the class
    print("Mage class namespace:", list(ChildClass.__dict__.keys()))
    print("Parent character category:", ChildClass.category)
# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    # Create Nova with a starting inventory
    original_mage = ChildClass("Nova", 10, "Fireball", ["Potion", "Staff"])

    # Create a shallow copy and a deep copy of Nova(somehow I never learned this during my time programming, this is great!)
    shallow_mage = copy(original_mage)
    # Deep copy wil have its own inventory that will not change based on the original changing
    deep_mage = deepcopy(original_mage)

    # Add a new item to Nova's inventory
    original_mage.inventory.append("Magic Ring")

    # Display each character's inventory after the change
    print("Original Nova's inventory:", original_mage.inventory)
    print("Shallow copy inventory:", shallow_mage.inventory)
    print("Deep copy inventory:", deep_mage.inventory)

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Character ===")
    base_character = ParentClass(name="Mage",level=10)
    print(base_character.display_character_info())

    print("\n=== Child Character ===")
    mage_character = ChildClass("Nova", 10, "Tornado", ["Healing Potion", "Staff"])
    print(mage_character.display_character_info())
    print(mage_character.cast_spell())
    print("Character type:", mage_character.character_type)
    print("Inherited category:", mage_character.category)
    # My added feature is below
    print(mage_character.add_item("Magic Scroll"))
    print("Updated inventory:", mage_character.inventory)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()