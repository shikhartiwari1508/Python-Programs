import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# CSV file ka correct path
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "data.csv")

# Dataset load karo
df = pd.read_csv(csv_file)

print("Original Dataset:")
print(df)

# Missing values check
print("\nMissing Values:")
print(df.isnull().sum())

# Numerical columns ke missing values ko mean se fill karo
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

# Categorical columns ke missing values ko mode se fill karo
categorical_columns = df.select_dtypes(include=["object"]).columns

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# Categorical data ko numerical data mein convert karo
encoder = LabelEncoder()

for column in categorical_columns:
    df[column] = encoder.fit_transform(df[column])

print("\nPreprocessed Dataset:")
print(df)

print("\nMissing Values After Preprocessing:")
print(df.isnull().sum())