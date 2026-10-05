import os
import pandas as pd

# CSV file ka correct path
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "data.csv")

# Dataset load karo
df = pd.read_csv(csv_file)

print("Original Dataset:")
print(df)

# One-Hot Encoding
df_encoded = pd.get_dummies(
    df,
    columns=["Course"],
    dtype=int
)

print("\nDataset After One-Hot Encoding:")
print(df_encoded)