import numpy as np


x_values = [1,3,6,5,4,7,2,6,3,6,8,2,9]

numpy_x_values = np.array(x_values) # numpy formats arrays to be a little cleaner when printed
numpy_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(numpy_x_values)
print(x_values)

ones_array = np.ones(10) # creates single dimensional array of 10 ones. default is float
print(ones_array)
zeros_array = np.zeros(6, dtype=np.int32) # array of int's instead of floats by changing dtype
print(zeros_array) # now decimals are removed from np array output because data type is int and not float

number_sequence_array = np.arange(10) # 0-9
print(number_sequence_array)

limit_array = np.arange(1, 11) # 1-10
print(limit_array)

skip_nums_array = np.arange(10, 101, 10) #10 - 100 in increments of 10
print(skip_nums_array)

linspace_array = np.linspace(1, 10, 5) # linspace defines the number of elements in an array based on start and stop params
print(linspace_array) # prints 5 evenly spaced elements from 1 and 10. includes the start value and stop value

linespace_array2 = np.linspace(0, 10, 6) # 0-10 with 6 elements including start and stop.
print(linespace_array2) # should print out even numbers from 0-10