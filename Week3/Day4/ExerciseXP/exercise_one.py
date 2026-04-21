# 🌟 Exercise 2: Import
# Goal: Create a module with a function and import it into another file.
# Instructions:
# Create a func.py file with a function that sums two numbers and prints the result. Then, import and call the function from exercise_one.py.
# Key Python Topics:
# Modules (creating and importing)
# Functions
# Step 1: Create func.py
# Create a file named func.py.
# Define a function inside that file that takes two numbers as arguments, sums them, and prints the result.
# Step 2: Create exercise_one.py
# Create a file named exercise_one.py.
# Import the function from func.py using one of the import syntaxes provided in the instructions.
# Call the imported function with two numbers.
import func
func.my_function(3, 5)


# 🌟 Exercise 3: String module
# Goal: Generate a random string of length 5 using the string module.
# Instructions:
# Use the string module to generate a random string of length 5, consisting of uppercase and lowercase letters only.
# Key Python Topics:
# string module
# random module
# String concatenation
# Step 1: Import the string and random modules
# Import the string and random modules.
import string
import random
# Step 2: Create a string of all letters
# Read about the strings methods HERE to find the best methods for this step
letters = string.ascii_letters
# Step 3: Generate a random string
# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.
result = ""
for _ in range(5):
    result += random.choice(letters) #random.choice(letters) → берёт случайную букву
print(result)


# 🌟 Exercise 4: Current Date
# Goal: Create a function that displays the current date.
# Key Python Topics:
# datetime module
# Instructions:
# Use the datetime module to create a function that displays the current date.
# Step 1: Import the datetime module
from datetime import datetime
# Step 2: Get the current date
# Step 3: Display the date
def display_current_date():
    # Получаем текущую дату и время
    now = datetime.now()
    # Форматируем дату для удобного отображения (ГГГГ-ММ-ДД)
    current_date = now.strftime("%Y-%m-%d")
    print(f"Текущая дата: {current_date}")
# Вызов функции
display_current_date()


# 🌟 Exercise 5: Amount of time left until January 1st
# Goal: Create a function that displays the amount of time left until January 1st.
# Key Python Topics:
# datetime module
# Time difference calculations
# Instructions:
# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE
# Step 1: Import the datetime module
from datetime import datetime
# Step 2: Get the current date and time
now = datetime.now()
# Step 3: Create a datetime object for January 1st of the next year
next_year = now.year + 1
new_year = datetime(next_year, 1, 1)
# Step 4: Calculate the time difference
time_left = new_year - now
# Step 5: Display the time difference
print(time_left)
print(time_left.days, "days")



# 🌟 Exercise 6: Birthday and minutes
# Key Python Topics:
# datetime module
# datetime.datetime.strptime() (parsing dates)
# Time difference calculations
# .total_seconds() method
# Instructions:
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.
from datetime import datetime
def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.now()
    time_lived = now - birthdate
    minutes = time_lived.total_seconds() / 60
    print(f"You have lived {int(minutes)} minutes")

minutes_lived("1990-05-17")

# 🌟 Exercise 7: Faker Module
# Goal: Use the faker module to generate fake user data and store it in a list of dictionaries.
# Read more about this module HERE
# Key Python Topics:
# faker module
# Dictionaries
# Lists
# Loops
# Instructions:
# Install the faker module and use it to create a list of dictionaries, where each dictionary represents a user with fake data.
# Step 1: Install the faker module
# pip install faker
# Step 2: Import the faker module
from faker import Faker
fake = Faker()
# Step 3: Create an empty list of users
# Step 4: Create a function to add users
# Create a function that takes the number of users to generate as an argument.
def generate_users(n):
# Inside the function, use a loop to generate the specified number of users.
# For each user, create a dictionary with the keys name, address, and language_code.
# Use the faker instance to generate fake data for each key:
# name: faker.name()
# address: faker.address()
# language_code: faker.language_code()
# Append the user dictionary to the users list.
    users = []
    for _ in range(n):
        user = {
            "name": fake.name(),
            "address": fake.address().replace("\n", ", "),
            "language_code": fake.language_code()
        }
        users.append(user)
    return users
# Step 5: Call the function and print the users list
users = generate_users(3)
print(users)