import numpy as np

some_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
multiplied_array = some_array * 2 # this will multiply every element in the array by 2
print(multiplied_array)

add_array = np.array([1, 2, 3])
sum_arrays = add_array + np.array([1, 1, 1]) # as long as the arrays are the same size, you can perform operations on them
print(sum_arrays)

trim_array = some_array[:4] + np.array([1, 1, 1, 1]) # can trim an array then perform operations on it
print(trim_array)

some_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(some_matrix)

new_matrix = some_matrix[:, 1:3] # this takes values from the 2nd and 3rd cols in all rows
print(new_matrix)

new_matrix2 = some_matrix[1:3, 1:3] + 5 # this adds 5 to sliced matrix values
print(new_matrix2)