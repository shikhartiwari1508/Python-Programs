import os
import pandas as pd
from sklearn.model_selection import train_test_split

# CSV file ka correct path
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "data.csv")

# Dataset load karo
df = pd.read_csv(csv_file)

print("Original Dataset:")
print(df)

# Input (X) aur Output (y)
X = df[["Age"]]
y = df["Marks"]

# Dataset ko 80% training aur 20% testing mein divide karo
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTraining Target:")
print(y_train)

print("\nTesting Data:")
print(X_test)

print("\nTesting Target:")
print(y_test)