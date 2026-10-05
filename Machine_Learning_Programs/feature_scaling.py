import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

# CSV file ka correct path
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "data.csv")

# Dataset load karo
df = pd.read_csv(csv_file)

print("Original Dataset:")
print(df)

# Numerical features select karo
X = df[["Age", "Marks"]]

print("\nBefore Scaling:")
print(X)

# StandardScaler create karo
scaler = StandardScaler()

# Scaling apply karo
X_scaled = scaler.fit_transform(X)

# Scaled data ko DataFrame mein convert karo
scaled_df = pd.DataFrame(
    X_scaled,
    columns=["Age", "Marks"]
)

print("\nAfter Standard Scaling:")
print(scaled_df)