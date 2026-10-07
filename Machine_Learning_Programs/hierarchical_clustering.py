import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

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

# Hierarchical clustering
model = AgglomerativeClustering(
    n_clusters=2,
    linkage="ward"
)

# Clusters create karo
df["Cluster"] = model.fit_predict(X_scaled)

print("\nDataset After Hierarchical Clustering:")
print(df)

# Cluster count
print("\nStudents in Each Cluster:")
print(df["Cluster"].value_counts())

# Dendrogram
linked = linkage(X_scaled, method="ward")

plt.figure(figsize=(8, 5))

dendrogram(
    linked,
    labels=df["Name"].values
)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Students")
plt.ylabel("Distance")
plt.show()