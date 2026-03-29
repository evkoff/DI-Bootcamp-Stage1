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



#Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A= {}
for index, name in enumerate(users):
    disney_users_A[name] = index
print(disney_users_A)

disney_users_B = {}
for index, name in enumerate(users):
    disney_users_B[index] = name
print(disney_users_B)

sorted_users = sorted(users)
disney_users_C = {name: index for index, name in enumerate(sorted_users)}
print(disney_users_C)


