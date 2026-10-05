'''import pandas as pd

# Import CSV dataset
df = pd.read_csv("data.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display number of rows and columns
print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())'''


import pandas as pd
import os

# Get the folder where this Python file is located
folder = os.path.dirname(os.path.abspath(__file__))

# Create complete path of CSV file
csv_file = os.path.join(folder, "data.csv")

# Load CSV dataset
df = pd.read_csv(csv_file)

print("First 5 Rows:")
print(df.head())

print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())