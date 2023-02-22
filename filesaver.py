import matplotlib.pyplot as plt
import pandas as pd
import webbrowser
import numpy as np
from sklearn.linear_model import LinearRegression


from scipy.interpolate import interp1d


comparable_years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
taxpaid = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1100]
taxIncrease = [1, 2, 3, 12, 5, 6, 7, 5, 9, 16]
tax_values = [150, 200, 250, 300, 350, 400, 450, 500, 5340, 1500]
valuIncreaseRates = [10, 20, 30, 120, 50, 60, 70, 50, 90, 160, 40, 67, 34, 45, 80, 50, 80]

def predic_value(past_array, amount_to_predict):
    # Example input data
    data = np.array(past_array)

    # Reshape the data into a 2D array with one column
    X = data.reshape(-1, 1)

    # Use the first 5 values as training data
    X_train = X[:5]
    y_train = data[:5]

    # Fit a linear regression model to the training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict the next x values
    X_test = X[amount_to_predict:]
    y_pred = model.predict(X_test)

    # Print the predicted values
    ##print("Predicted values:", y_pred)
    return y_pred

future_tax_values = predic_value(tax_values, 5)
future_valuIncreaseRates = predic_value(valuIncreaseRates, 5)


plt.rcParams["figure.figsize"] = [15.50, 9.50]
plt.rcParams["figure.autolayout"] = True




"""
fig, axs = plt.subplots(1, 1)
axs[0, 0].plot(comparable_years, tax_values, '*-', color='red', markersize=5)
axs[0, 0].set_title('Tax Values by Year')
ax2 = axs.twinx()
ax2.plot(comparable_years, future_tax_values, 'r^-', label='Predicted Tax Values')
axs[0, 1].plot(comparable_years, valuIncreaseRates, '*-', color='green', markersize=5)
axs[0, 1].set_title('Tax Value Increase Rate by Year')
ax3 = axs.twinx()
ax3.plot(comparable_years, future_valuIncreaseRates, 'r^-', label='Predicted Values')
axs[1, 0].plot(comparable_years, taxpaid, '*-', color='blue', markersize=5)
axs[1, 0].set_title('Tax Paid by Year')
axs[1, 1].plot(comparable_years, taxIncrease, '*-', color='orange', markersize=5)
axs[1, 1].set_title('Tax Increase by Year')


fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(comparable_years, taxpaid, '*-', color='blue', markersize=5)
ax1.set_title('Tax Paid by Year')
ax2.plot(comparable_years, taxIncrease, '*-', color='orange', markersize=5)
ax2.set_title('Tax Increase by Year')
plt.savefig('my_plots.png')
ax1.secondary_xaxis(top)
fig, axs1 = plt.subplots()
axs1.plot(comparable_years, tax_values, '*-', color='red', markersize=5)
axs1.set_title('Tax Values by Year')
axs1.set_xlabel('X1 axis label')
axs1.set_ylabel('Y1 axis label')
ax2 = axs1.twinx()
ax2.plot(comparable_years, future_tax_values, 'r^-', label='Predicted Tax Values')
lines, labels = axs1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='best')
##axs[0, 1].plot(comparable_years, valuIncreaseRates, '*-', color='green', markersize=5)
##axs[0, 1].set_title('Tax Value Increase Rate by Year')
##ax3 = axs.twinx()
##ax3.plot(comparable_years, future_valuIncreaseRates, 'r^-', label='Predicted Values')
plt.show()"""



# create arrays
comparable_years2 = [2017, 2018, 2019, 2020, 2021]
"""
x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 4, 6, 8, 10])
x2 = np.array([1.5, 3, 4.5])
y2 = np.array([3, 7, 9])
"""
x1 = comparable_years
y1 = tax_values
x2 = comparable_years2
y2 = future_tax_values
print(future_tax_values)
# interpolate data to get values of y2 at the points of x1
##f = interp1d(x2, y2)
y2_interpolated =(x1)

# plot the arrays on a single plot
fig, ax = plt.subplots()
ax.plot(x1, y1, 'bo-', label='y1')
ax.plot(x2, y2, 'r^-', label='y2')

# set the axis labels and title
ax.set_xlabel('X axis label')
ax.set_ylabel('Y axis label')
ax.set_title('Title of the plot')

# add legend to the plot
ax.legend(loc='best')

# display the plot
plt.show()
