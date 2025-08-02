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

# --- 1D Array Operations ---

print("--- Appending to 1D Arrays ---")
some_array = np.array([1, 2, 3])
print(f"Original array: {some_array}")

# Appends a single value to the end of the array
appended_array = np.append(some_array, 4)
print(f"Appended a single value (4): {appended_array}")

# Appends multiple arrays to the original array, flattening the result
new_array = np.append(some_array, [some_array, some_array])
print(f"Appended the original array twice: {new_array}\n")

print("--- Inserting into 1D Arrays ---")
# Inserts the value 10 at index 2
insert_array = np.insert(some_array, 2, 10)
print(f"Original array: {some_array}")
print(f"Inserted 10 at index 2: {insert_array}")

# Inserts multiple values starting at index 2
insert_array2 = np.insert(some_array, 2, [10, 11, 12])
print(f"Inserted [10, 11, 12] at index 2: {insert_array2}\n")

print("--- Deleting from 1D Arrays ---")
# Deletes the elements at index 0 and 1
delete_index_array = np.delete(some_array, [0, 1])
print(f"Original array: {some_array}")
print(f"Deleted elements at indices [0, 1]: {delete_index_array}\n")

# --- 2D Array (Matrix) Operations ---

print("--- Appending to 2D Arrays (Matrices) ---")
some_matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original matrix:\n{some_matrix}")

# Appends a new row (axis=0)
# Note: The appended data must have the same number of columns
append_row_matrix = np.append(some_matrix, [[7, 8, 9]], axis=0)
print(f"\nAppended a new row (axis=0):\n{append_row_matrix}")

# Appends a new column (axis=1)
# Note: The appended data must have the same number of rows
append_col_matrix = np.append(append_row_matrix, [[10], [11], [12]], axis=1)
print(f"\nAppended a new column (axis=1):\n{append_col_matrix}\n")

print("--- Inserting into 2D Arrays (Matrices) ---")
# Inserts a new row at index 1 (axis=0)
insert_row_matrix = np.insert(some_matrix, 1, [10, 11, 12], axis=0)
print(f"Original matrix:\n{some_matrix}")
print(f"\nInserted a row at index 1 (axis=0):\n{insert_row_matrix}")

# Inserts a new column at index 3 (the end) (axis=1)
insert_col_matrix = np.insert(insert_row_matrix, 3, [13, 14, 15], axis=1)
print(f"\nInserted a column at index 3 (axis=1):\n{insert_col_matrix}")
