import numpy as np


some_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(some_array[8])

some_array[8] = 100 # access and change elements the same as lists
print(some_array) # replacing the 8th index value (9) with 100

some_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(some_matrix)
print(some_matrix[0]) # can acess any part of the matrix. this prints the first row
print(some_matrix[0][2]) # this prints the value at the 2nd index in the first row. can change the value just as easily

some_matrix[2] = np.array([10, 11, 12]) # this will replace the entire 3rd row
print(some_matrix)

new_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(new_array[0:5]) # this will print a range from the 0 - 4th index. upper bound is not included
print(new_array[5:9]) # 9th index is actually oob but since it's not included in the statement this will work
print(new_array [-1]) # this will print the last element in the array. -2 second to last and so on

new_array [5:9] = 6 # this will change all values in the range to 6
print(new_array)

print(some_matrix[:, 2]) # this will get all elements from every row in the 3rd col


