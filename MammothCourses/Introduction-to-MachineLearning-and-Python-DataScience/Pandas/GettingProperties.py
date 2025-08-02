import pandas as pd

panda_series = pd.Series([1, 3, 2, 5, 8, 4, 1, 6, 9, 2, 5, 1, 3, 5, 1, 2, 4])
series_count = panda_series.count() # counts number of elements in series
series_max = panda_series.max() # returns max value in series
series_min = panda_series.min() # returns min value in series
series_mean = panda_series.mean() # returns the mean of the series
series_median = panda_series.median() # returns the median of the series
series_std = panda_series.std() # returns the standard deviation of the series
series_description = panda_series.describe() # this returns count, mean, med, mode, min, max, 25%, 50%, 75% values of the series
series_sum = panda_series.sum() # this returns the sum of the entire series
largest_n_series = panda_series.nlargest(2) # this returns a series with the 2 greatest values in the collection and their index
smallest_n_series = panda_series.nsmallest(2) # this returns a series with the 2 smallest values in the collection
max_index = panda_series.idxmax() # this returns the index of the higest value in the series
min_index = panda_series.idxmin() # this returns the index of the lowest value in the series
histogram_ints = panda_series.value_counts() # this returns a series of unique values and their counts



print(f"this is the output of the describe function:\n{series_description}\n")
print(f"The max value in the series is: {series_max} and the min value is: {series_min}")
print(f"The mean value in the series is: {series_mean} and the median value is: {series_median}")
print(f"The standard deviation of the series is: {series_std} and the count of the series is: {series_count}")
print(f"The sum of the series is: {series_sum}")
print(f"The 2 largest values in the series are:\n{largest_n_series}")
print(f"The 2 smallest values in the series are:\n{smallest_n_series}")
print(f"The index of the highest value in the series is: {max_index}")
print(f"The index of the lowest value in the series is: {min_index}")
print(f"This is the histogram of the series:\n{histogram_ints}")