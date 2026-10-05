import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# CSV file ka correct path
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "data.csv")

# Dataset load karo
df = pd.read_csv(csv_file)

print("Original Dataset:")
print(df)

# Numerical columns select karo
X = df[["Age", "Marks"]]

print("\nBefore Normalization:")
print(X)

# Min-Max Scaler
scaler = MinMaxScaler()

# Normalization apply karo
X_normalized = scaler.fit_transform(X)

# DataFrame mein convert karo
normalized_df = pd.DataFrame(
    X_normalized,
    columns=["Age", "Marks"]
)

print("\nAfter Normalization:")
print(normalized_df)