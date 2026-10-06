import os
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

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

# K-Means model
model = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

# Clustering
df["Cluster"] = model.fit_predict(X_scaled)

print("\nDataset After K-Means Clustering:")
print(df)

# Cluster centers
print("\nCluster Centers:")
print(model.cluster_centers_)

# Har cluster mein kitne students hain
print("\nStudents in Each Cluster:")
print(df["Cluster"].value_counts())