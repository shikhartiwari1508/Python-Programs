import os
import pandas as pd

from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# CSV file ka correct path
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "data.csv")

# Dataset load karo
df = pd.read_csv(csv_file)

print("Dataset:")
print(df)

# Input features
X = df[["Age", "StudyHours"]]

# Target
y = df["Pass"]

# Model + Scaling Pipeline
model = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

# 5-Fold Cross Validation
kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

# Cross-validation scores
scores = cross_val_score(
    model,
    X,
    y,
    cv=kf,
    scoring="accuracy"
)

print("\nCross-Validation Accuracy Scores:")
print(scores)

print("\nMean Accuracy:")
print(scores.mean())

print("\nStandard Deviation:")
print(scores.std())