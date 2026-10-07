import os
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# CSV file ka correct path
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "data.csv")

# Dataset load karo
df = pd.read_csv(csv_file)

print("Original Dataset:")
print(df)

# Numerical features select karo
X = df[["Age", "StudyHours", "Marks"]]

print("\nOriginal Features:")
print(X)

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA apply karo
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

# PCA result ko DataFrame mein convert karo
pca_df = pd.DataFrame(
    X_pca,
    columns=["PC1", "PC2"]
)

print("\nDataset After PCA:")
print(pca_df)

# Explained variance
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

# Total variance preserved
total_variance = pca.explained_variance_ratio_.sum()

print("\nTotal Variance Preserved:",
      total_variance)