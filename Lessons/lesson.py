# # import os
# # os.system('clear') # Это очистит терминал перед каждым запуском
# name = "Student"
# # print(f"Ready to learn Python, {name}!")
# # print("Привет, это мой первый запуск в VS Code!")
# # print("Я учусь программировать на Python.")
# # print("Это мой второй запуск в VS Code!")
# # print("Я продолжаю учиться программировать на Python.")  
# # author = {
# #    "first_name": "Jonathan",
# #    "last_name": "Hsu",
# #    "username": "jhsu98"
# # }

# # print(f"Автор: {author['first_name']} {author['last_name']} (Username: {author['username']})")
# # my_list = ['Rick', 'Sanchez']
# # print("My last name is:", my_list[1])
# # numbers = 10, 20, 30
# # print(type(numbers))
# # x = 10
# # y = 20

# # print(f'x={x}, y={y}')

# # tmp = x
# # x = y
# # y = tmp

# # print(f'x={x}, y={y}')
# # a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# # print(a_dict.items())
# # sample_dict = { 
# #    "class":{ 
# #       "student":{ 
# #          "name":"Mike",
# #          "marks":{ 
# #             "physics":70,
# #             "history":80
# #          }
# #       }
# #    }
# # }
# # print(sample_dict['class']['student']['marks']['history'])
# # rick_dict = {
# #     'first_name':'Rick',
# #     'last_name':'Sanchez'
# # }
# # print(rick_dict.items())

# # my_books = {
# #   "title": "Harry Potter",
# #   "author": "JK Rowling",
# # }

# # for x, y in my_books.items(): 
# #     print("the " + x + " is " + y)
# # for letter in 'Leonardo':
# #     if letter == 'a':
# #         break
# #     print(letter, end='') # end='' renders each letter next to the other
# # print()
# # while True:
# #     s = input('Enter something : ')
# #     if s == 'quit':
# #         break
# #     print('Length of the string is', len(s))
# # print('Done')



# # #Exercise 4: Disney Characters
# # users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# # #Create a dictionary that maps characters to their indices:
# # disney_users_A= {}
# # for index, name in enumerate(users):
# #     disney_users_A[name] = index
# # print(disney_users_A)

# # #Create a dictionary that maps indices to characters:
# # disney_users_B = {}
# # for index, name in enumerate(users):
# #     disney_users_B[index] = name
# # print(disney_users_B)

# # #Create a dictionary where characters are sorted alphabetically and mapped to their indices:
# # sorted_users = sorted(users)
# # disney_users_C = {name: index for index, name in enumerate(sorted_users)}
# # print(disney_users_C)

# # items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
# # wallet = "$300"
# # wallet_value = int(wallet.replace("$", "").replace(",", ""))
# # basket = []
# # for item, price in items_purchase.items():
# #     price_value = int(price.replace("$", "").replace(",", ""))
# #     if price_value <= wallet_value:
# #         basket.append(item)
# #         wallet_value -= price_value
# #     else:
# #         print(f"You cannot afford {item} which costs {price}.")
# # if not basket:
# #     print("Nothing")
# # else:
# #     print(sorted(basket))



# # def calculation(a, b):
# #     addition = a + b
# #     substraction = a - b

# # res = calculation(40, 10)
# # print(res)

# # def double(n):
# #   return n * 2

# # myList = [10, 25, 17, 9, 30, -5]

# # myList2 = map(double, myList)
# # print (list(myList2))
# # The code is longer!

# # def multipleOf5(n):
# #   if(n % 5 == 0):
# #     return n

# # myList = [10, 25, 17, 9, 30, -5]

# # myList2 = filter(multipleOf5, myList)
# # print (list(myList2))

# # myList = [10, 25, 17, 9, 30, -5]
# # # Filters the elements which are not multiples of 5
# # myList2 = filter(lambda n : n%5 == 0, myList)
# # print (list(myList2))

# # lst = [1, 2, 3, 4, "a", "b", "c", 38.5, "56.7"]
# # print(lst)
# # print(type(lst))
# # print(type(lst[-1])) 

# # l1 = [1, 2, 3, 4, 5, 6]
# # l1.append(3)
# # l1.extend([7, 8, 9])
# # l1.extend([6, 7, 8])
# # print(l1)


# # l1=[1, 2, 3, 4, 5, 6]
# # l1.insert(2, 6)
# # print(l1)
# # a = ["b", "g", "a", "d", "f", "c", "h", "e"]
# # x = sorted(a)
# # print("a after sorted function")
# # print(a)
# # print(x)
# # b = [1, 2, 5, 8, 3]
# # b.sort()
# # print(b)

# # lst = [1, 2, 3, 4, 5, 6, 7]
# # print(lst[0:4])
# # print(lst[::])
# # print(lst[::-1])

# # lst = [1, 2, 3, 4, 5, 6, 7]
# # print(lst.pop())
# # print(lst)
# # lst.remove(4)
# # print(lst) 
# # lst.clear()
# # print(lst)

# # t = (1, 2, 3, 4, 5, "a", "b", "c")
# # t1 = 1, 2, 3, 4, "g", "l"
# # print(t)
# # print(t1)
# # print(len(t))

# # t1 = (1, 2, 3, 4, 5)
# # t2 = (6, 7, 8, 9)
# # t3 = t1 + t2 
# # print(t3)

# # d = {1:'10', 2:'20', 3:'30', 4:'40', 5:'50'}
# # l1 =list(d.keys())
# # print("the key values are:")
# # print(l1)
# # l2 = list(d.values())
# # print("The values are of dictionary is")
# # print(l2)
# # l3 = list(d.items())
# # print("the list items are")
# # print(l3)

# # set1 = {1, 2, 3, 4, "hi", "world", "python"}
# # print("python" in set1)
# # set1.remove(4)
# # print(set1)

# # a = {1, 2, 3, 4, 5}
# # b = {2, 3, 6, 7, 5}
# # c = a^b 
# # print(c)
# # d = a - b
# # print(d)
# # e = b - a 
# # print(e)

# # def get_formatted_name(first_name, last_name):
# #     """Return a full name, neatly formatted."""
# #     full_name = first_name + ' ' + last_name
# #     return full_name.title()

# # musician = get_formatted_name('jimi', 'hendrix') 
# # print(musician)

# # def format_name(first_name, last_name):
# #     return (first_name.title(), last_name.title())

# # first, last = format_name("RICk", "mORTY")
# # print(first)
# # print(last)

# # def my_function(username, **details):
# #   print("Username:", username)
# #   print("Additional details:")
# #   for key, value in details.items():
# #     print("  ", key + ":", value)

# # my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# filtered_names = filter(lambda name: len(name) >= 4, people)
# hello_people = map(lambda name: f"Hello, {name}", filtered_names)


# print(list(hello_people))

# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# # filtered_people = filter(lambda name: len(name) <= 4, people)
# hello_messages = map(lambda name: f"Hello, {name}", filter(lambda name: len(name) <= 4, people))
# print(list(hello_messages))

# from collections import Counter  
# list = [1,2,3,4,1,2,6,7,3,8,1,2,2]  
# answer=Counter()
# answer = Counter(list)  
# print(answer[2])  

# from collections import deque  
# #initialization
# list = ["a","b","c"]  
# deq = deque(list)  
# print(deq)  

# #insertion
# deq.append("z")  
# deq.appendleft("g")  
# print(deq)
# #removal
# deq.pop()  
# deq.popleft()  
# # print(deq)

# from collections import namedtuple
# Student = namedtuple('Student', 'fname, lname, age')  
# s1 = Student('Peter', 'James', '13')  
# # print(s1.fname) 

# import collections

# dictionary1 = { 'a' : 1, 'b' : 2 }  
# dictionary2 = { 'c' : 3, 'b' : 4 }  
# chain_Map = collections.ChainMap(dictionary1, dictionary2)  
# print(chain_Map.maps)  

# from collections import OrderedDict  
# order = OrderedDict()  
# order['a'] = 1  
# order['b'] = 2  
# order['c'] = 3  
# print(order)  

# #unordered dictionary
# unordered=dict()
# unordered['a'] = 1  
# unordered['b'] = 2  
# unordered['c'] = 3 
# print("Default dictionary", unordered)


# import itertools

# result = itertools.count(start = 0, step = 2)

# for number in result:
# # termination condition
#     if number < 8:
#         print (number)
#     else:
#         break

# import itertools

# result = itertools.cycle('12345')
# counter = 0

# for number in result:
# # termination condition
#     if counter < 10 :
#         print (number)
# #         counter = counter + 1
# #     else:
# #         break

# # print hello two times
# import itertools

# result = itertools.repeat('hello', times = 2)

# for word in result:
#     print (word)

# # iterate over three lists
# import itertools

# list_one = ['a', 'b', 'c']
# list_two =['d', 'e', 'f']
# list_three = ['1', '2', '3']

# result = itertools.chain(list_one, list_two, list_three)

# for element in result:
#   print (element)

#find the names of people who have the flu
# import itertools

# names = ['Alice', 'James', 'Matt']
# have_flu = [True, True, False]

# result = itertools.compress(names, have_flu)

# for element in result:
#   print (element)

# import itertools

# my_list = [0, 0, 1, 2, 0]

# result = itertools.dropwhile(lambda x: x == 0, my_list)

# for elements in result:
#   print (elements)

# class MyClass(object):
#     count = 0

#     def __init__(self, val):
#         self.val = val
#         MyClass.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val

#     @classmethod
#     def get_count(cls):
#         return cls.count

# object_1 = MyClass(10)
# print("\nValue of object : %s" % object_1.get_val())
# print(MyClass.get_count())

# object_2 = MyClass(20)
# print("\nValue of object : %s" % object_2.get_val())
# print(MyClass.get_count())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __call__(self):
#         print (f"Person: {self.name}, Age: {self.age}")

# person1 = Person("Sarah", 25)
# # person1()
# class Person:
#   def __init__(self, name, age):
#       self.name = name
#       self.age  = age

#   def __repr__(self):
#       return f"{self.__class__.__name__} : {self.name} {self.age}"

# newPerson = Person('Sarah', 24)

# print(newPerson)
# # >> Person : Sarah 24 
# # __repr__ is the representation of an object

class Person:
  def __init__(self, name, lastName):
      self.name = name
      self.lastName = lastName

  def __repr__(self):
      return f"{self.__class__.__name__} : {self.name} {self.lastName}"

  def __add__(self, other):
      return Person(self.name, other.lastName)

# father = Person('John', 'Snow')
# mother = Person('Kaleesi', 'MotherOfDragons')
# # using the __add__() method
# dragonChild = father + mother 

# print(dragonChild)
# # >> Person : John MotherOfDragons // __add__ is called to add two objects

# print(type(dragonChild))
# # >> <class '__main__.Person'>

# print(dir(dragonChild))
# # >> ['__add__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'lastName', 'name']


# class Person:
#     def __init__(self, name, lastName):
#         self.name = name
#         self.lastName = lastName


# #Here we overloaded the method by redefining '__repr__ 'using 'def' and passed the argument '(self)'

#     def __repr__(self):

# # We can write whatever we want inside this method, but we have to return an object.

#       return f"{self.__class__.__name__} : {self.name} {self.lastName}"

#     def __add__(self,other):
#         name = self.name[0] + other.name[1:]
#         lastname = other.lastName
#         return Person(name,lastname)

# father = Person('John', 'Snow')
# mother = Person('Kaleesi', 'MotherOfDragons')
# # using the __add__() method
# dragonChild = father + mother 

# print(dragonChild)
# # >>Person : Jaleesi MotherOfDragons


# from datetime import datetime, timedelta, date


# today_date = date.today()
# actual_datetime = datetime.now()

# in_15_hours = actual_datetime + timedelta(hours=15, minutes=10)

# print(f"Today is the {today_date.strftime('%d/%m')}")
# print(f"In 15 hours and 10 minutes it will be the {in_15_hours.strftime('%d/%m')}")

# from datetime import datetime, timedelta, date

# today_date = datetime.date.today()
# actual_datetime = datetime.now()
# in_15_hours = actual_datetime + timedelta(hours=15, minutes=10)

# print(f"Today is the {today_date.strftime('%d/%m')}")
# print(f"In 15 hours and 10 minutes it will be the {in_15_hours.strftime('%d/%m')}")

# from datetime import datetime, timedelta, date

# today_date = date.today()
# actual_datetime = datetime.now()
# in_15_hours = actual_datetime + timedelta(hours=15, minutes=10)

# print(f"Today is the {today_date.strftime('%d/%m')}")
# print(f"In 15 hours and 10 minutes it will be the {in_15_hours.strftime('%d/%m')}")

# from datetime import datetime

# def birthday_countdown():
#     now = datetime.now()
#     birthday = datetime(now.year, 12, 15)
    
#     if now >= birthday:
#         birthday = datetime(now.year + 1, 12, 15)
    
#     diff = birthday - now
    
#     days = diff.days
#     hours, remainder = divmod(diff.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)
    
#     print(f"My birthday is in {days} days, and {hours:02}:{minutes:02}:{seconds:02}")

# birthday_countdown()

# import requests

# # 1. Получаем категории
# categories_url = "https://api.chucknorris.io/jokes/categories"
# categories = requests.get(categories_url).json()

# print("Available categories:", categories)

# # 2. Берём первую категорию (или любую)
# category = categories[0]

# # 3. Получаем шутку
# joke_url = f"https://api.chucknorris.io/jokes/random?category={category}"
# joke = requests.get(joke_url).json()

# print("\nCategory:", category)
# print("Joke:", joke["value"])




import requests

try:
    # категории
    categories = requests.get(
        "https://api.chucknorris.io/jokes/categories"
    ).json()

    category = categories[0]

    # несколько шуток
    for _ in range(3):
        response = requests.get(
            f"https://api.chucknorris.io/jokes/random?category={category}"
        )
        
        if response.status_code == 200:
            data = response.json()
            print(data["value"])

except requests.exceptions.RequestException as e:
    print("Error:", e)