import pandas as pd


days_since_11Jan = pd.date_range('20250111', periods=10, freq='D') # will create a series of 10 dates incremented by 1 day starting at 11 jan with.
hours_since_11Jan = pd.date_range('20250111', periods=10, freq='H') # will create a series of 10 dates incremented by 1 hour starting at 11 jan
time_in_4hr_blocks = pd.date_range('20250111', periods=10, freq='4H') # this will create a series of 10 times that increment in 4hr blocks
start_end_date_range = pd.date_range('20250111', '20250120', freq='D', inclusive='both') #creates a series from 11 jan through 20 jan incrementing by 1 day
dates = pd.date_range('20250111', periods=5, freq='D')
series_with_date_range_index = pd.Series([1, 2, 3, 4, 5], index=dates) #assigns each date from the date range as and index for each value in the series.
date_range_to_series = pd.Series(dates) #convert date_range to series with the default index
get_days = date_range_to_series.dt.day # create a series with only the day info from the date_range. many options for m,y,h,sec...etc

print(days_since_11Jan)
print(hours_since_11Jan)# starts at 0:00 and increments by 1 hour
print(time_in_4hr_blocks) # starts at 0:00 and increments by 4 hours.
print(start_end_date_range) # includes start and end date
print(series_with_date_range_index) # index[0] = 2025-01-11 and value = 1 (the first value in the series)
print(date_range_to_series)
print(get_days)