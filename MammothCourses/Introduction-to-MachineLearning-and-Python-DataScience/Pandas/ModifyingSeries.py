import pandas as pd


series_from_dict = pd.Series({'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60, 'g': 70, 'h': 80, 'i': 90, 'j': 100}) #assigning custom labels as index

# Adding items
series_from_dict['k'] = 110 # creates a new item with kvp of 'k': 110
series_to_add = pd.Series({'l': 120, 'm': 130, 'n': 140}) # series to demo appending to another series
appended_series = pd.concat([series_from_dict, series_to_add]) # this will combine the series into 1

# Removing items
del appended_series['n'] # deletes single value and index
new_series = appended_series.drop(['m', 'l']) # creates a new series minus the specified dropped values
popped = new_series.pop('a') # this REMOVES the 'a' value from the series and stores it in the 'popped' var

# Modifying items
modified_series = appended_series.copy()
modified_series[0] = 0 # creating a new series with index 0's value changed from 10 to 0
modified_series_10s = modified_series.copy()
modified_series_10s[:3] = 10 # creates a new series where the first 3 indexes are assigned 10 as value
renamed_series = modified_series_10s.rename('Series 1')
renamed_series = modified_series_10s.rename(str.upper) # changes lowercase strings to upppercase



print(series_from_dict)
print(appended_series)
print(f"This series drops 'm' and 'l':\n{new_series}")
print(f"This is the popped value: {popped}")
print(f"This is the modified series with 0 in the first index:\n{modified_series}")
print(f"This is the series with 10's in the first 3 indexes:\n {modified_series_10s}")
print(f"This is the renamed series:\n{renamed_series}")