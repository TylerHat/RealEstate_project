# import the necessary libraries
import pandas as pd

# set the initial parameters
initial_investment = 100000
monthly_rent = 2000
expenses_per_month = 1000

# create a list to store the data for each year
data = []

# loop through 10 years and calculate the data for each year
for year in range(1, 11):
    # calculate the total income for the year
    total_income = monthly_rent * 12
    
    # calculate the total expenses for the year
    total_expenses = expenses_per_month * 12
    
    # calculate the net income for the year
    net_income = total_income - total_expenses
    
    # calculate the total return on investment for the year
    total_roi = (initial_investment + net_income) / initial_investment
    
    # add the data for the year to the list
    data.append({
        "Year": year,
        "Total Income": total_income,
        "Total Expenses": total_expenses,
        "Net Income": net_income,
        "Total ROI": total_roi
    })

# create a pandas DataFrame from the data
df = pd.DataFrame(data)

# create an HTML table from the DataFrame
html_table = df.to_html()

# create a new HTML file and write the HTML table to it
with open("rental_calculator.html", "w") as f:
    f.write(html_table)

# print a message to confirm that the HTML file has been created
print("The rental calculator table has been exported to rental_calculator.html.")
