import os
import pandas as pd

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

# Multiple input features
X = df[["Age", "StudyHours"]]

# Target/output
y = df["Marks"]

# Training aur testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model create karo
model = LinearRegression()

# Model train karo
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(y_pred)

# Coefficients
print("\nCoefficients:")
print("Age:", model.coef_[0])
print("Study Hours:", model.coef_[1])

print("\nIntercept:", model.intercept_)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error:", mse)
print("R2 Score:", r2)

# New student prediction
new_student = [[21, 6]]

prediction = model.predict(new_student)

print("\nPredicted Marks:")
print("Age = 21, Study Hours = 6")
print("Predicted Marks =", prediction[0])
