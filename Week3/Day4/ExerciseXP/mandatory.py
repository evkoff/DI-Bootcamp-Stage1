# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Dunder methods (__str__, __int__, __repr__, __add__, __iadd__)
# Modules (importing and using)
# string module
# datetime module
# faker module
# 🌟 Exercise 1: Currencies
# Goal: Implement dunder methods for a Currency class to handle string representation, integer conversion, addition, and in-place addition.
# Key Python Topics:
# Dunder methods (__str__, __repr__, __int__, __add__, __iadd__)
# Type checking (isinstance())
# Raising exceptions (raise TypeError)
# Instructions:
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self):
        if self.amount % 10 == 1 and self.amount % 100 != 11:
            return f"{self.amount} {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"
    def __int__(self):
        return self.amount
    def __repr__(self):
        return str(self)
    def __add__(self, other):
# если other — число → просто прибавляем к amount
# если other — Currency:
# проверяем валюту
# если одинаковая → складываем
# если нет → ошибка
# всё остальное → тоже ошибка
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        else:
            raise TypeError("Unsupported type") 
    def __iadd__(self, other): #меняет self.amount а не возвращает число как __add__
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
            raise TypeError("Unsupported type") 
        return self

# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
#the comment is the expected output
print(c1)
# '5 dollars'
print(int(c1))
# 5
print(repr(c1))
# '5 dollars'
print(c1 + 5)
# 10
#print(c1 + c2)
# 15
print(c1) 
# 5 dollars
c1 += 5
print(c1)
# 10 dollars
#c1 += c2
print(c1)
# 20 dollars
print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>
#comment the print above before you run the file for next exercises (since the error will crash your file)



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
