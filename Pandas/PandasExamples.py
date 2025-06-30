
import pandas as pd
import numpy as np

# --- Creating DataFrames ---

# From a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 40, 28],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'Salary': [70000, 80000, 90000, 110000, 75000]}
df = pd.DataFrame(data)

print("--- Initial DataFrame ---")
print(df)
print("\n")

# --- Inspecting Data ---

print("--- DataFrame Info ---")
df.info()
print("\n")

print("--- First 3 Rows (head) ---")
print(df.head(3))
print("\n")

print("--- Last 2 Rows (tail) ---")
print(df.tail(2))
print("\n")

print("--- Descriptive Statistics (describe) ---")
print(df.describe())
print("\n")

# --- Selecting Data ---

print("--- Selecting a single column ('Name') ---")
print(df['Name'])
print("\n")

print("--- Selecting multiple columns (['Name', 'Salary']) ---")
print(df[['Name', 'Salary']])
print("\n")

# Selecting rows by integer location (iloc)
print("--- Selecting the first row (iloc[0]) ---")
print(df.iloc[0])
print("\n")

print("--- Selecting rows 1 to 3 (iloc[1:4]) ---")
print(df.iloc[1:4])
print("\n")

# Selecting rows by label/condition (loc)
# First, let's set the 'Name' column as the index
df_indexed = df.set_index('Name')
print("--- Selecting data for 'Charlie' (loc['Charlie']) ---")
print(df_indexed.loc['Charlie'])
print("\n")


# --- Filtering Data ---

print("--- Filtering for Age > 30 ---")
print(df[df['Age'] > 30])
print("\n")

print("--- Filtering for City == 'Chicago' ---")
print(df[df['City'] == 'Chicago'])
print("\n")


# --- Adding/Modifying Columns ---

print("--- Adding a 'Salary in Thousands' column ---")
df['Salary in Thousands'] = df['Salary'] / 1000
print(df)
print("\n")


# --- Grouping and Aggregating ---

data_sales = {'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Books', 'Books'],
              'Sales': [1200, 800, 1500, 900, 300, 500],
              'Units': [10, 25, 12, 30, 15, 20]}
sales_df = pd.DataFrame(data_sales)

print("--- Sales DataFrame ---")
print(sales_df)
print("\n")

print("--- Grouping by 'Category' and calculating sum of 'Sales' ---")
print(sales_df.groupby('Category')['Sales'].sum())
print("\n")

print("--- Grouping by 'Category' and calculating multiple aggregations ---")
print(sales_df.groupby('Category').agg({'Sales': 'mean', 'Units': 'sum'}))
print("\n")


# --- Handling Missing Data ---

data_missing = {'A': [1, 2, np.nan, 4],
                'B': [5, np.nan, np.nan, 8],
                'C': [9, 10, 11, 12]}
missing_df = pd.DataFrame(data_missing)

print("--- DataFrame with Missing Values ---")
print(missing_df)
print("\n")

print("--- Dropping rows with any missing values (dropna) ---")
print(missing_df.dropna())
print("\n")

print("--- Filling missing values with a specific value (e.g., 0) ---")
print(missing_df.fillna(0))
print("\n")

print("--- Filling missing values with the mean of the column ---")
print(missing_df.fillna(missing_df.mean()))
print("\n")


# --- Reading and Writing Files (Example) ---

# To save the DataFrame to a CSV file:
# df.to_csv('employees.csv', index=False)
# print("DataFrame saved to employees.csv")

# To read a DataFrame from a CSV file:
# df_from_csv = pd.read_csv('employees.csv')
# print("\n--- DataFrame read from employees.csv ---")
# print(df_from_csv)

