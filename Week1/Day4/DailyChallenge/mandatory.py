
"""
Exercise 1: Favorite Numbers
Key Python Topics:

Sets
Adding/removing items in a set
Set concatenation (using union)


Instructions:

Create a set called my_fav_numbers and populate it with your favorite numbers.
Add two new numbers to the set.
Remove the last number you added to the set.
Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
Note: Sets are unordered collections, so ensure no duplicate numbers are added.
"""
my_fav_numbers={1,22,7,777,77,95}
my_fav_numbers.add(47)
my_fav_numbers.add(33)
my_fav_numbers.remove(33)
friend_fav_numbers = {3, 7, 9, 11}
our_fav_numbers = my_fav_numbers | friend_fav_numbers



"""
 Exercise 2: Tuple
Key Python Topics:

Tuples (immutability)


Instructions:

Given a tuple of integers, try to add more integers to the tuple.
Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
"""
my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4,)


"""
🌟 Exercise 3: List Manipulation
Key Python Topics:

Lists
List methods: append, remove, insert, count, clear


Instructions:

You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
Remove "Banana" from the list.
Remove "Blueberries" from the list.
Add "Kiwi" to the end of the list.
Add "Apples" to the beginning of the list.
Count how many times "Apples" appear in the list.
Empty the list.
Print the final state of the list.
"""

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.append("Kiwi")
basket.insert(0, "Apples")
basket.count("Apples")
basket.clear()


"""
🌟 Exercise 4: Floats
Key Python Topics:

Lists
Floats and integers
Range generation

Instructions:

Recap: What is a float? What’s the difference between a float and an integer?
Create a list containing the following sequence of mixed types: floats and integers:
1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
Avoid hard-coding each number manually.
Think: Can you generate this sequence using a loop or another method?
"""


floats_list = []
current_value = 1.5

while current_value <= 5:
    if current_value % 1 == 0:
        floats_list.append(int(current_value))
    else:
        floats_list.append(current_value)
    
    current_value += 0.5

print(floats_list)


"""
Exercise 5: For Loop
Key Python Topics:

Loops (for)
Range and indexing


Instructions:

Write a for loop to print all numbers from 1 to 20, inclusive.
"""

for i in range(1, 21):
    print(i)

# Write another for loop that prints every number from 1 to 20 where the index is even.

numbers = list(range(1, 21))
for i in range(len(numbers)):
    if i % 2 == 0:
    	print(numbers[i])



"""
Exercise 6: While Loop

Key Python Topics:

Loops (while)

Conditionals

Instructions:

Use an input to ask the user to enter their name.

Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)

hint: check for the method isdigit()

if the input is incorrect, keep asking for the correct input until it is correct
"""

while True:
     user_name = input(prompt)
     if user_name.isdigit() or len(user_name) < 3:
         prompt = "Give the correct name: "
         continue
     else:
         print("thank you")
         break


"""
Exercise 7: Favorite Fruits
Key Python Topics:

Input/output
Strings and lists
Conditionals


Instructions:

Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
Store these fruits in a list.
Ask the user to input the name of any fruit.
If the fruit is in their list of favorite fruits, print:
"You chose one of your favorite fruits! Enjoy!"
If not, print:
"You chose a new fruit. I hope you enjoy it!"
"""

user_input = input("Enter your favorite fruits (separated by a space): ")
favorite_fruits = user_input.split()
chosen_fruit = input("Enter the name of any fruit: ")
if chosen_fruit in favorite_fruits:
	print("You chose one of your favorite fruits! Enjoy!")
else:
	print("You chose a new fruit. I hope you enjoy it!")


"""
Exercise 8: Pizza Toppings
Key Python Topics:

Loops
Lists
String formatting


Instructions:

Write a loop that asks the user to enter pizza toppings one by one.
Stop the loop when the user types 'quit'.
For each topping entered, print:
"Adding [topping] to your pizza."
After exiting the loop, print all the toppings and the total cost of the pizza.
The base price is $10, and each topping adds $2.50.
"""

toppings = []
base_price = 10
topping_price = 2.5

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ").lower()
    
    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

total_price = base_price + (len(toppings) * topping_price)

print("\n--- Your Order Summary ---")
print("Toppings:", toppings)
print(f"Total price: ${total_price}")

"""
🌟 Exercise 9: Cinemax Tickets
Key Python Topics:

Conditionals
Lists
Loops


Instructions:

Ask for the age of each person in a family who wants to buy a movie ticket.
Calculate the total cost based on the following rules:
Free for people under 3.
$10 for people aged 3 to 12.
$15 for anyone over 12.
Print the total ticket cost.
"""

total_cost = 0

while True:
    age_input = input("Enter the age of a family member (or 'done' to calculate): ").lower()
    
    if age_input == 'done':
        break
    
    age = int(age_input)
    
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
        
    total_cost += ticket_price
    print(f"Ticket price for age {age}: ${ticket_price}")

print(f"\nTotal ticket cost for the family: ${total_cost}")



"""
Bonus:

Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
Write a program to:
Ask for each person’s age.
Remove anyone who isn’t allowed to watch.
Print the final list of attendees.
"""

teenagers = ["Alice", "Bob", "Charlie", "David", "Eve"]
allowed_attendees = []

for name in teenagers:
    age = int(input(f"How old is {name}? "))
    
    if 16 <= age <= 21:
        allowed_attendees.append(name)
    else:
        print(f"Sorry {name}, you are not allowed to watch this movie.")

print("Final list of attendees:")
print(allowed_attendees)
