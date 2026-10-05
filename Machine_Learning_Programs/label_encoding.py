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

# Label Encoder create karo
encoder = LabelEncoder()

# Course column ko numerical values mein convert karo
df["Course"] = encoder.fit_transform(df["Course"])

print("\nDataset After Label Encoding:")
print(df)

# Encoding mapping show karo
print("\nLabel Mapping:")
for i, label in enumerate(encoder.classes_):
    print(label, "=", i)