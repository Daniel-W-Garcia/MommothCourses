import pandas as pd
import numpy as np

#Panda Series are 1-dimensional only

series = pd.Series([1, 3, 5, 6, 8]) # creates a series from a list with a paired index
mixed_dataType_series = pd.Series([1, 2, 3, True, 'Daniel']) # this creates a Series of different data types as type 'Object'
nan_series = pd.Series([1, 2, np.nan, 4, 5, None]) # data type of float because NaN (not a number) is a float64
specified_dtype_series = pd.Series([1, 2, 3, 4, 5], dtype=np.float64) #inferred would be int but we specify float 64 as data type
dict_series = pd.Series({'a': 10, 'b': 20, 'c': 30}) # replacing default index (0,1,2 ...etc) with custom index labels
dict_series2 = pd.Series([60, 70, 80], index=['a', 'b', 'c']) # a different way to assign custom index labels
same_value_all_index = pd.Series(10, index=['a', 'b', 'c'])


print(series) # this will actually print the inferred data type of the series
print(mixed_dataType_series) # prints the series as 'Object'
print(nan_series)
print(specified_dtype_series)
print(dict_series) # will print dict with 'a' as index instead of '0' for value '10'
print(dict_series2)
print(same_value_all_index)

# Converting back and forth from Pandas Series to Numpy Arrays

np_series = pd.Series(np.array([1, 2, 3, 4, 5])) # creating a series from a numpy array
numpy_series = np_series.to_numpy() # converting that series back to a numpy array

print(f"This is the series created from numpy:\n{np_series}") #prints as series
print(f"This is the converted series back to numpy:\n{numpy_series}") #prints as array


