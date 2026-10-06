import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

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

# Training aur testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Feature scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Model train
model.fit(X_train_scaled, y_train)

# Prediction
y_pred = model.predict(X_test_scaled)

print("\nActual Result:")
print(y_test.values)

print("\nPredicted Result:")
print(y_pred)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# New student prediction
new_student = [[21, 6]]

new_student_scaled = scaler.transform(new_student)

prediction = model.predict(new_student_scaled)

print("\nNew Student:")
print("Age = 21")
print("Study Hours = 6")

if prediction[0] == 1:
    print("Predicted Result: PASS")
else:
    print("Predicted Result: FAIL")