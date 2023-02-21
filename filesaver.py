import numpy as np
from sklearn.linear_model import LinearRegression

# Example input data
data = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])

# Reshape the data into a 2D array with one column
X = data.reshape(-1, 1)

# Use the first 5 values as training data
X_train = X[:5]
y_train = data[:5]

# Fit a linear regression model to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the next 5 values
X_test = X[5:]
y_pred = model.predict(X_test)

# Print the predicted values
print("Predicted values:", y_pred)
