# import os
# os.system('clear') # Это очистит терминал перед каждым запуском
name = "Student"
# print(f"Ready to learn Python, {name}!")
# print("Привет, это мой первый запуск в VS Code!")
# print("Я учусь программировать на Python.")
# print("Это мой второй запуск в VS Code!")
# print("Я продолжаю учиться программировать на Python.")  
# author = {
#    "first_name": "Jonathan",
#    "last_name": "Hsu",
#    "username": "jhsu98"
# }

# print(f"Автор: {author['first_name']} {author['last_name']} (Username: {author['username']})")
# my_list = ['Rick', 'Sanchez']
# print("My last name is:", my_list[1])
# numbers = 10, 20, 30
# print(type(numbers))
# x = 10
# y = 20

# print(f'x={x}, y={y}')

# tmp = x
# x = y
# y = tmp

# print(f'x={x}, y={y}')
# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# print(a_dict.items())
# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(sample_dict['class']['student']['marks']['history'])
# rick_dict = {
#     'first_name':'Rick',
#     'last_name':'Sanchez'
# }
# print(rick_dict.items())

# my_books = {
#   "title": "Harry Potter",
#   "author": "JK Rowling",
# }

# for x, y in my_books.items(): 
#     print("the " + x + " is " + y)
# for letter in 'Leonardo':
#     if letter == 'a':
#         break
#     print(letter, end='') # end='' renders each letter next to the other
# print()
# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     print('Length of the string is', len(s))
# print('Done')



# #Exercise 4: Disney Characters
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# #Create a dictionary that maps characters to their indices:
# disney_users_A= {}
# for index, name in enumerate(users):
#     disney_users_A[name] = index
# print(disney_users_A)

# #Create a dictionary that maps indices to characters:
# disney_users_B = {}
# for index, name in enumerate(users):
#     disney_users_B[index] = name
# print(disney_users_B)

# #Create a dictionary where characters are sorted alphabetically and mapped to their indices:
# sorted_users = sorted(users)
# disney_users_C = {name: index for index, name in enumerate(sorted_users)}
# print(disney_users_C)

# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
# wallet = "$300"
# wallet_value = int(wallet.replace("$", "").replace(",", ""))
# basket = []
# for item, price in items_purchase.items():
#     price_value = int(price.replace("$", "").replace(",", ""))
#     if price_value <= wallet_value:
#         basket.append(item)
#         wallet_value -= price_value
#     else:
#         print(f"You cannot afford {item} which costs {price}.")
# if not basket:
#     print("Nothing")
# else:
#     print(sorted(basket))



# def calculation(a, b):
#     addition = a + b
#     substraction = a - b

# res = calculation(40, 10)
# print(res)

# def double(n):
#   return n * 2

# myList = [10, 25, 17, 9, 30, -5]

# myList2 = map(double, myList)
# print (list(myList2))
# The code is longer!

# def multipleOf5(n):
#   if(n % 5 == 0):
#     return n

# myList = [10, 25, 17, 9, 30, -5]

# myList2 = filter(multipleOf5, myList)
# print (list(myList2))

# myList = [10, 25, 17, 9, 30, -5]
# # Filters the elements which are not multiples of 5
# myList2 = filter(lambda n : n%5 == 0, myList)
# print (list(myList2))

# lst = [1, 2, 3, 4, "a", "b", "c", 38.5, "56.7"]
# print(lst)
# print(type(lst))
# print(type(lst[-1])) 

# l1 = [1, 2, 3, 4, 5, 6]
# l1.append(3)
# l1.extend([7, 8, 9])
# l1.extend([6, 7, 8])
# print(l1)


# l1=[1, 2, 3, 4, 5, 6]
# l1.insert(2, 6)
# print(l1)
# a = ["b", "g", "a", "d", "f", "c", "h", "e"]
# x = sorted(a)
# print("a after sorted function")
# print(a)
# print(x)
# b = [1, 2, 5, 8, 3]
# b.sort()
# print(b)

# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst[0:4])
# print(lst[::])
# print(lst[::-1])

# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst.pop())
# print(lst)
# lst.remove(4)
# print(lst) 
# lst.clear()
# print(lst)

# t = (1, 2, 3, 4, 5, "a", "b", "c")
# t1 = 1, 2, 3, 4, "g", "l"
# print(t)
# print(t1)
# print(len(t))

# t1 = (1, 2, 3, 4, 5)
# t2 = (6, 7, 8, 9)
# t3 = t1 + t2 
# print(t3)

# d = {1:'10', 2:'20', 3:'30', 4:'40', 5:'50'}
# l1 =list(d.keys())
# print("the key values are:")
# print(l1)
# l2 = list(d.values())
# print("The values are of dictionary is")
# print(l2)
# l3 = list(d.items())
# print("the list items are")
# print(l3)

# set1 = {1, 2, 3, 4, "hi", "world", "python"}
# print("python" in set1)
# set1.remove(4)
# print(set1)

# a = {1, 2, 3, 4, 5}
# b = {2, 3, 6, 7, 5}
# c = a^b 
# print(c)
# d = a - b
# print(d)
# e = b - a 
# print(e)

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix') 
# print(musician)

# def format_name(first_name, last_name):
#     return (first_name.title(), last_name.title())

# first, last = format_name("RICk", "mORTY")
# print(first)
# print(last)

# def my_function(username, **details):
#   print("Username:", username)
#   print("Additional details:")
#   for key, value in details.items():
#     print("  ", key + ":", value)

# my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
filtered_names = filter(lambda name: len(name) >= 4, people)
hello_people = map(lambda name: f"Hello, {name}", filtered_names)


print(list(hello_people))






