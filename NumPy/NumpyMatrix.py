import numpy as np

matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]


numpy_matrix = np.array(matrix)

print(matrix) # simple print output
print(numpy_matrix) # NumPy formats the matrix with rows and cols and removing commas

ones_array = np.ones((2,3)) # this is a feature that will create a matrix with the dimensions speicfied. 2 rows and 3 cols.
print(ones_array)

zeros_array = np.zeros((3,2))# same as above but with zeros instead of ones and 3 rows and 2 cols
print(zeros_array)

some_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

reshaped_arrary = some_array.reshape(3, 3) # takes the input array and outputs it into a matrix. if the number of indexes are the same
print(reshaped_arrary)

def create_matrix_from_multiplycation(row, col):
    return row * col

created_matrix = np.fromfunction(create_matrix_from_multiplycation, (4, 4)) # creates a 4 x 4 where rows are multiplied by cols top left (0*0 = 0) to bottom right (3*3 = 9)
print(created_matrix)