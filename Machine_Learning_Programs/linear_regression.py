import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# CSV file ka correct path
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "data.csv")

# Dataset load karo
df = pd.read_csv(csv_file)

print("Dataset:")
print(df)

# Input feature
X = df[["Age"]]

# Target/output
y = df["Marks"]

# Training aur testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Linear Regression model
model = LinearRegression()

# Model train karo
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(y_pred)

# Model coefficients
print("\nSlope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

# Model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error:", mse)
print("R2 Score:", r2)

# New prediction
new_age = [[23]]
prediction = model.predict(new_age)

print("\nPredicted Marks for Age 23:", prediction[0])

# Graph
plt.scatter(X, y, label="Actual Data")
plt.plot(X, model.predict(X), label="Regression Line")

plt.xlabel("Age")
plt.ylabel("Marks")
plt.title("Linear Regression")
plt.legend()
plt.show()