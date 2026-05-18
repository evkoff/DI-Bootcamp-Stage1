# import pandas as pd
# # dataSeties = pd.Series([1, 3, 5, 7, 9])
# # dataFrame = {
# #     'Name': ['John', 'Anna', 'Peter', 'Linda'],
# #     'Age': [28, 34, 29, 32],
# #     'City': ['New York', 'Paris', 'Berlin', 'London']
# # }
# # df = pd.DataFrame(dataFrame)

# df = pd.read_csv('/Users/evgeniakolesnikova/Library/Mobile Documents/com~apple~CloudDocs/ai_data_analysis_lab/Lessons/Data_Analysis.py')
# df.head()  # Displays the first 5 rows by default

# import numpy as np
# array_1d = np.arange(1, 6)
# type(array_1d)

import numpy as np

# arr = np.arange(1, 11)
# print(arr[4])
# print(arr[2:8])

# arr = np.arange(1, 11)
# print(arr)
# arr[4] = 50
# print(arr)
# arr[3:8] = -arr[3:8]
# print(arr)

# random_arr = np.random.randint(1, 101, 20)
# print(random_arr)
# random_arr[random_arr > 50] = -1 #Set all values greater than 50 to -1.
# # print(random_arr)

# arr_2d = np.arange(1, 26).reshape(5, 5) #2D array of shape (5, 5),

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# # print(arr1)
# # print(arr2)
# # print(arr1 + arr2)
# # print(arr1 - arr2)
# # print(arr1 * arr2)
# # print(arr1 / arr2)
# print(arr1.sum())
# print(arr1.mean())


# arr = np.arange(1, 13)
# print(arr)
# print(arr.shape)
# matrix_4x3 = arr.reshape(4, 3)
# print(matrix_4x3)
# matrix_2x6 = arr.reshape(2, 6)
# print(matrix_2x6)
# transposed = matrix_2x6.T
# print(transposed)
# print(transposed.shape)
matrix = np.arange(1, 13).reshape(3, 4)
print(matrix)
transposed_matrix = matrix.T
print(transposed_matrix)
flat_array = transposed_matrix.reshape(12)
print(flat_array)