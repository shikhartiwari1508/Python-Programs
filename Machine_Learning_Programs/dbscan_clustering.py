import os
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

# CSV file ka correct path
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "data.csv")

# Dataset load karo
df = pd.read_csv(csv_file)

print("Original Dataset:")
print(df)

# Features select karo
X = df[["Age", "StudyHours", "Marks"]]

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# DBSCAN model
model = DBSCAN(
    eps=1.5,
    min_samples=2
)

# Clustering
df["Cluster"] = model.fit_predict(X_scaled)

print("\nDataset After DBSCAN Clustering:")
print(df)

# Cluster information
print("\nCluster Counts:")
print(df["Cluster"].value_counts())

# Noise points
noise = df[df["Cluster"] == -1]

print("\nNoise / Outlier Points:")
if noise.empty:
    print("No noise points found.")
else:
    print(noise)