import numpy as np

some_array = np.array([2, 5, 3, 1, 4, 6])
array_with_duplicates = np.array([1, 2, 2, 3, 4, 4, 4, 5, 5])

# --- Calculations/Fetch Operations ---
array_max_number = some_array.max() # Max value in the array
array_min_number = some_array.min() # Min value in the array
array_sum = some_array.sum() # Sum of all elements in the array
array_mean = some_array.mean() # Mean (Average) of all elements in the array
array_median = np.median(some_array) # Median of all elements in the array
array_std = np.std(some_array) # Standard deviation of the array
array_argMin = some_array.argmin() # Index of the minimum value
array_argMax = some_array.argmax() # Index of the maximum value
array_nonzero_index = some_array.nonzero() # Index of all elements in the array with non-zero values
unique_elements = np.unique(array_with_duplicates) # returns array with unique elements only. Removes duplicates
conditional_array = np.where(some_array > 3, 99, some_array) # replaces any number larger than 3 with 99

# --- Descriptive Printing using f-strings ---
print(f"Original Array: {some_array}")
print(f"Maximum value: {array_max_number}")
print(f"Minimum value: {array_min_number}")
print(f"Sum of all elements: {array_sum}")
print(f"Mean (Average): {array_mean}")
print(f"Median: {array_median}")
print(f"Standard Deviation: {array_std:.2f}")  # You can even format numbers inside!some_array = np.array([2,5,3,1,4,6])
print(f"Index of minimum value: {array_argMin}")
print(f"Index of maximum value: {array_argMax}")
print(f"Indices of non-zero elements: {array_nonzero_index}")
print(f"Finding unique elements in {array_with_duplicates}: {unique_elements}")

# --- Calculations/Modify Operations ---
quicksort_array = np.sort(some_array) # Sort the array in ascending order DEFAULT is QUICKSORT but you can specify sorting type
revers_array = np.flip(some_array) # Reverse the order of elements in the array
conditional_array = np.where(some_array > 3, 99, some_array) # replaces any number larger than 3 with 99
clipped_array = np.clip(some_array, 3, 5) # Values < 3 become 3, and values > 5 become 5.
cum_sum_array = np.cumsum(some_array) # replaces each index value with cumulative sum

# --- Descriptive Printing using f-strings ---
print(f"Sorted Array: {quicksort_array}")
print(f"Reversed Array: {revers_array}")
print(f"Finding unique elements in {array_with_duplicates}: {unique_elements}")
print(f"Array values in {some_array} clipped between 3 and 5: {clipped_array}")
print(f"Cumulative sum of {some_array}: {cum_sum_array}")

# --- Multinomial Array Manipulation ---
some_matrix = np.array([[3, 1, 2], [8, 9, 7], [5, 6, 4]])
max_val_per_0axis = some_matrix.max(axis=0) # axis 0 is the vertical axis. so this is max value of each col
max_val_per_1axis = some_matrix.max(axis=1) # axis 1 is the horizontal axis. so this is the max value of each row
argmax_val_per_0axis = some_matrix.argmax(axis=0) # this will return the INDEX of where the max value of each col is
argmax_val_per_1axis = some_matrix.argmax(axis=1) # this will return the INDEX of where the max value of each row is
sort_by_row_array = np.sort(some_matrix, axis=1) # this will sort each row
sort_by_col_array = np.sort(some_matrix, axis=0) # this will sort each column
transpose_matrix = some_matrix.transpose() # rows become cols with this operation
flatten_array = some_matrix.flatten() # this will flatten array into one row. rows will append to end of previous row

# --- Descriptive Printing using f-strings ---
print(f"Original Matrix:\n{some_matrix}\n Has a max value of {max_val_per_0axis} on the '0th' axis.")
print(f"Original Matrix:\n{some_matrix}\n Has a max value of {max_val_per_1axis} on the '1st' axis.")
print(f"Original Matrix:\n{some_matrix}\n Has a Argmax index of:\n {argmax_val_per_0axis} on the '0th' axis.")
print(f"Original Matrix:\n{some_matrix}\n Has a Argmax index of:\n {argmax_val_per_1axis} on the '1st' axis.")
print(f"Original Matrix:\n{some_matrix}\n When sorted by row:\n {sort_by_row_array}")
print(f"Original Matrix:\n{some_matrix}\n When sorted by col:\n {sort_by_col_array}")
print(f"Original Matrix:\n{some_matrix}\n When transposed:\n {transpose_matrix}")
print(f"Original Matrix:\n{some_matrix}\n When flattened:\n {flatten_array}")