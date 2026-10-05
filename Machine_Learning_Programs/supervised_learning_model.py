import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load CSV dataset
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Get current Python file folder
folder = os.path.dirname(os.path.abspath(__file__))

# Load CSV from same folder as Python file
csv_file = os.path.join(folder, "data.csv")

df = pd.read_csv(csv_file)

print("Dataset:")
print(df)

# Features
X = df[["Age"]]

# Target
y = df["Marks"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(y_pred)

# Predict marks for a new student
new_student = [[23]]
prediction = model.predict(new_student)

print("\nPredicted Marks for Age 23:", prediction[0])