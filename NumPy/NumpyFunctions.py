import numpy as np

some_array = np.array([1, 2, 3,])
appended_array = np.append(some_array, 4) # appends a value to the end of the array
print(appended_array)

new_array = np.append(some_array, [some_array, some_array]) #append entire arrays to an array
print(new_array)

insert_array = np.insert(some_array, 2, 10) # insert a value at a specific index. insert will be at the specified index so value at that index gets bumped to the right
print(insert_array)

insert_array2 = np.insert(some_array, 2, [10, 11, 1]) # same as append and can inset multiple values or arrays
print(insert_array2)

delete_index_array = np.delete(some_array, [0, 1]) # deletes index 0 and 1 from array. works with matrix as well
print(delete_index_array)

some_matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(some_matrix)

append_index_matrix = np.append(some_matrix, [[7, 8, 9]], axis=0) # this will add a new row. axis 0 = row. axis 1 = col
print(append_index_matrix)

append_index_matrix2 = np.append(append_index_matrix, [[7], [8], [9]], axis=1) # this will add a new col at the end of each row.
print(append_index_matrix2)

insert_into_matrix = np.insert(some_matrix, 1, [10, 11, 12], axis=0) # doesn't have to be double brackets because it's inserting not adding a new dimension
print(insert_into_matrix)

insert_into_matrix2 = np.insert(insert_into_matrix, 3, [13, 14, 15], axis=1) # again, each element doesn't need it's own bracket
print(insert_into_matrix2)