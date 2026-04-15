# Exercise 1: Cats
# Key Python Topics:
# Classes and objects
# Object instantiation
# Attributes
# Functions


# Instructions:
# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.

# Step 1: Create Cat Objects

# Use the Cat class to create three cat objects with different names and ages.

# Step 2: Create a Function to Find the Oldest Cat

# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.


# Step 3: Print the Oldest Cat’s Details

# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.



class Cat:
    def __init__(self, cat_name, cat_age):
         self.name = cat_name
         self.age = cat_age

# # Step 1: Create cat objects
cat1 = Cat("Cat1", 1)
cat2 = Cat("Cat2", 2)
cat3 = Cat("Cat3", 3)

# # Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
#     # ... code to find and return the oldest cat ...
    oldest_cat = cat1
    if cat2.age >  cat1.age:
        oldest_cat = cat2
    if cat3.age > cat2.age:
        oldest_cat = cat3
    return oldest_cat
    
# # Step 3: Print the oldest cat's details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}. His age is {oldest_cat.age}")




# Exercise 2 : Dogs
# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.
# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Attributes
# Conditional statements (if)


# Instructions:
# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.

# Step 1: Create the Dog Class

# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “<dog_name> goes woof!”.
# Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
            jump_height = self.height * 2
            print(f"{self.name} jumps {jump_height} cm high!")
    
           

# Step 2: Create Dog Objects
# Create davids_dog and sarahs_dog objects with their respective names and heights.
davids_dog = Dog("David", 50)
sarahs_dog = Dog("Sarah", 60)

# Step 3: Print Dog Details and Call Methods
# Print the name and height of each dog.
print(davids_dog.name, davids_dog.height)
print(sarahs_dog.name, sarahs_dog.height)
# Call the bark() and jump() methods for each dog.
davids_dog.bark()
davids_dog.jump()

sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare Dog Sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}")
else:
    print(f"{sarahs_dog.name} and {davids_dog.name} are of the same height")

# 🌟 Exercise 3 : Who’s the song producer?
# Goal: Create a Song class to represent song lyrics and print them.
# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists
# Instructions:
# Create a Song class with a method to print song lyrics line by line.
# Step 1: Create the Song Class
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.
# Example:
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()
# Output: There’s a lady who’s sureall that glitters is goldand she’s buying a stairway to heaven
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()



# 🌟 Exercise 4 : Afternoon at the Zoo
# Goal:
# Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.
# Key Python Topics:
# Classes and objects
# Object instantiation
# Methods
# Lists
# Dictionaries (for grouping)
# String manipulation
# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.
# 2. Implement the __init__() method:
# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.
class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
# 3. Add a method add_animal(new_animal):
# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                # add animal to the list
                self.animals.append(animal)
# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.
    def get_animals(self):
        print(self.animals)
# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
           self.animals.remove(animal_sold)
# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.
# Example output:
# {
#    'B': ['Baboon', 'Bear'],
#    'C': ['Cat', 'Cougar'],
#    'G': ['Giraffe'],
#    'L': ['Lion'],
#    'Z': ['Zebra']
# }
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        groups = {}
        for animal in sorted_animals:
        # get first letter
            first_letter = animal[0]
            # if this letter is not in dictionary → create new list
            if first_letter not in groups:
                groups[first_letter] = [] #create new record in the dictionary "B": []
            # add animal to the group
            groups[first_letter].append(animal) #fill in the item: "B": ["Bear"]
        return groups

# 7. Add a method get_groups():
# This method prints the grouped animals as created by sort_animals().
# Example output:
# B: ['Baboon', 'Bear']
# C: ['Cat', 'Cougar']
# G: ['Giraffe']
# ...
    def get_groups(self):
        # get grouped animals from sort_animals
        groups = self.sort_animals()
        # print each group nicely
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")

# Create an instance of the Zoo class and pass a name for the zoo.
# Call the Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.
# # Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")
# #Use the Zoo methods
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon")
#brooklyn_safari.add_animal("Bear")
#brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()


# Bonus: Modify the add_animal() method to get *args so you dont need to repeat the method each time for a new animal, you can pass multiple animals names separated by a comma.
