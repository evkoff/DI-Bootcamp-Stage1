#Exercise 1: Converting Lists into Dictionaries
#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
#Lists:

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# Expected Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
key_value_list = zip(keys, values)
my_dict = dict(key_value_list)
print(my_dict)

# Exercise 2: Cinemax #2
# Key Python Topics:
# Looping through dictionaries
# Conditionals
# Calculations

# Instructions
# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.
family = {}
total_cost = 0
print("--- Ticket Prices ---")
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name.capitalize()} (age {age}): ${price}")
    total_cost += price
print(f"Total cost: ${total_cost}")

# 
# Bonus:
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.
# 
print("\n--- Enter Family Members ---")
while True:
    name = input("Enter family member's name (or 'done' to finish): ")
    if name == 'done':
        break
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age
print("\n--- Ticket Prices ---")
for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name.capitalize()} (age {age}): ${price}")
    total_cost += price
print(f"Total cost: ${total_cost}")

                    