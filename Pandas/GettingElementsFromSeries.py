import pandas as pd
import numpy as np


panda_series = pd.Series([1, 3, 5, 6, 8], index=['a', 'b', 'c', 'd', 'e'])
first_element_by_index = panda_series[0] # retrieves value by index
first_element_by_label = panda_series['a'] # retrieves value by index Label
last_element_by_index = panda_series[-1] # -1 is a way to count backwards. so -1 is the last element in the series
using_get = panda_series.get(9) # this is OOB of the series. 'get' handles exception by returning a default value
using_get_custom_default = panda_series.get(9, default='This is outside the series')
get_range_of_values = panda_series[0:3] #this will create a series with an index of 0,1,2
greater_than_3 = panda_series[panda_series > 3] # returns a series from pandas series of all values greater than 3
indexes = panda_series.index # will fetch only indexes
values = panda_series.values # will fetch only values
pandas_array = panda_series.array


print(panda_series)
print(first_element_by_index)
print(f"The first element in the series is: {first_element_by_label}")
print(f"The last element in the series is: {last_element_by_index}")
print(using_get) # since we have null at index 9, default value 'None' is returned
print(f"This is our custom default: {using_get_custom_default}") # prints our custom default
print(f"This is the range of values:\n{get_range_of_values}")
print(f"From the original series:\n{panda_series}\nThis is all values greater than 3:\n{greater_than_3}")
print(f"This is a list of all indexes in\n{panda_series}:\n{indexes}")
print(f"This is a list of all values in\n{panda_series}:\n{values}")
print(f"This is now back to a pandas array:\n{pandas_array}")