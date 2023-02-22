import matplotlib.pyplot as plt
import pandas as pd
import webbrowser
import numpy as np
from sklearn.linear_model import LinearRegression

file = open('housedata.txt', 'r')
read = file.readlines()

file_path = "housedata.txt"

def pr(needed_values):
    print(f"******************\n", (needed_values), "\n******************")

with open(file_path, 'r') as file:
        contents = file.read()

def tabulate_string(text):
    indent_level = 0
    result = ""
    for char in text:
        if char == '{':
            result += '{\n' + '\t' * (indent_level + 1)
            indent_level += 1
        elif char == '}':
            indent_level -= 1
            result += '\n' + '\t' * indent_level + '}'
        elif char == '[':
            result += '[\n' + '\t' * (indent_level + 1)
            indent_level += 1
        elif char == ']':
            indent_level -= 1
            result += '\n' + '\t' * indent_level + ']'
        elif char == ',':
            result += ',\n' + '\t' * indent_level
        else:
            result += char
    return result

tabulated_data= tabulate_string(contents) 

##pr(tabulated_data)

text_file = open("housedata_tabed.txt", "w")
n = text_file.write(tabulated_data)
text_file.close()



def correction_value_error(filename, word, newword):
    with open(filename, 'r') as file:
        contents = file.read()
    contents = contents.replace(word, newword)
    with open(filename, 'w') as file:
        file.write(contents)

correction_value_error("housedata_tabed.txt", "valueIncreaseRate", "valuIncreaseRate")
correction_value_error("housedata_tabed.txt", '"zestimate":', '"HouseZestimate":')

def increment_word_count(filename, word):

    with open(filename, 'r') as file:
        contents = file.read()
    count = 0
    start = 0
    while start < len(contents):
        start = contents.find(word, start)
        if start == -1:
            break
        count += 1
        contents = contents[:start] + f"{word}_{count}" + contents[start + len(word):]
        start += len(f"{word}_{count}")
    with open(filename, 'w') as file:
        file.write(contents)

increment_word_count("housedata_tabed.txt", "taxIncreaseRate")
increment_word_count("housedata_tabed.txt", "taxPaid")
increment_word_count("housedata_tabed.txt", "time")
increment_word_count("housedata_tabed.txt", "value")
increment_word_count("housedata_tabed.txt", "valuIncreaseRate")


def find_value_after_word(word, endchar):

    with open("housedata_tabed.txt", 'r') as file:
            string = file.read()

    index = string.find(word)
    if index == -1:
        return None
    index += len(word)
    start_index = string.find(':', index)
    end_index = string.find(endchar, start_index)
    if start_index == -1 or end_index == -1:
        return None
    if string[start_index + 1:end_index].strip() == 'null':
        return 0
    else:
        return string[start_index + 1:end_index].strip()

######## Section for Miscellaneous Info ############

city_address = find_value_after_word("city",',').strip().strip("\"")
state_address =  find_value_after_word("state",',').strip().strip("\"")
streetAddress =  find_value_after_word("streetAddress",',').strip().strip("\"")
zipCode =  find_value_after_word("zipcode",',').strip().strip("\"\}")
county = find_value_after_word("county",',').strip().strip("\"")
country = find_value_after_word("country",',').strip().strip("\"")
description_full = find_value_after_word("description",'\",').strip().strip("\"").split('\n')
description_full = ' '.join(description_full).replace('\t', '').replace(", ",",")

full_address = streetAddress + ", " + city_address + ", " + county +" "+ zipCode +" " + country

##use this for $/sqft 
house_sqft = float(find_value_after_word("livingArea",',').strip().strip("\""))
lotSize_sqft = float(find_value_after_word("lotSize",',').strip().strip("\""))


######## Section for Home Price Values ############
monthly_HoaFee = float(find_value_after_word("monthlyHoaFee",','))
lastSoldPrice = float(find_value_after_word("lastSoldPrice",',').strip().strip("\""))
monthly_rentZestimate = float(find_value_after_word("rentZestimate",',').strip().strip("\""))
zestimateHouse = float(find_value_after_word("HouseZestimate",','))

##print(zestimateHouse)

######## Section for Taxes ############
tax_values= []
valuIncreaseRates = []
taxpaid = []
taxIncrease = []
comparable_years= []
comparable_years2 = []
year_start_tax = float(find_value_after_word("taxAssessedYear",","))
i1 =0
while i1 <=21:
    comparable_years.append(year_start_tax - i1)
    i1+=1
else:
    debug=3
i3=0
while i3<=4:
    comparable_years2.append(year_start_tax + i3)
    i3+=1
else:
    debug =1
i2=0
while i2<=21:
    tax_values.append(float(find_value_after_word("value_"+str(i2+1),",")))
    valuIncreaseRates.append(float(find_value_after_word("valuIncreaseRate_"+str(i2+1),"}")))
    taxpaid.append(float(find_value_after_word("taxPaid_"+str(i2+1),",")))
    taxIncrease.append(float(find_value_after_word("taxIncreaseRate_"+str(i2+1),",")))
    i2+=1
else:
    debug=4

def predic_value(past_array, amount_to_predict):
    # Example input data
    data = np.array(past_array)
    leng =len(past_array)-4
    
    # Reshape the data into a 2D array with one column
    X = data.reshape(-1, 1)

    # Use the first 5 values as training data
    X_train = X[:leng]
    y_train = data[:leng]

    model = LinearRegression()
    model.fit(X_train, y_train)

    X_test = X[:amount_to_predict]
    y_pred = model.predict(X_test)

    return y_pred

future_tax_values = predic_value(tax_values, 5)
future_valuIncreaseRates = predic_value(valuIncreaseRates, 5)

plt.rcParams["figure.figsize"] = [7, 4.50]
plt.rcParams["figure.autolayout"] = False

##Subplots for Tax Graphs

fig, ax = plt.subplots()
##ax.plot(comparable_years3, greymatter, '*-', color='blue', label='y3')
ax.plot(comparable_years2, future_tax_values, 'b*-', label='linear regression estimate')
ax.plot(comparable_years, tax_values, 'r^-', label='Previous Tax Values')
# set the axis labels and title
ax.set_xlabel('Years')
ax.set_ylabel('Tax Values')
ax.set_title('Predition of Tax Values in next 5 Years')

ax.legend(loc='best')

fig.savefig("my_plots_Tax_Values.png")

fig, ax2 = plt.subplots()
ax2.plot(comparable_years2, future_valuIncreaseRates, 'b*-', label='linear regression estimate')
ax2.plot(comparable_years, valuIncreaseRates, 'r^-', label='Previous Tax Increase Rates')
ax2.set_xlabel('Years')
ax2.set_ylabel('Tax Increase Rates')
ax2.set_title('Predition of Tax Change Rates in next 5 Years')

# add legend to the plot
ax2.legend(loc='best')

fig.savefig("my_plots_taxRates.png")

html_tab_TaxRate = []
html_tab_TaxValue = []
i=0
for year in range(int(year_start_tax+1),(int(year_start_tax)+5)):
    
    html_tab_TaxValue.append({
            "Year": int(year_start_tax+3)+i,
            "Tax Rage Change Prediction": round(future_tax_values[i], 3),
        })
    html_tab_TaxRate.append({
            "Year": int(year_start_tax+3)+i,
            "Tax Rage Change Prediction": round(future_valuIncreaseRates[i], 3),
        })
    i+=1
df_html_table_TaxRate = pd.DataFrame(html_tab_TaxRate)
table_TaxRate_html = df_html_table_TaxRate.to_html(classes='table table-stripped')
df_html_table_TaxValue = pd.DataFrame(html_tab_TaxValue)
table_TaxValue_html = df_html_table_TaxValue.to_html(classes='table table-stripped')


html_TaxRate_tb = df_html_table_TaxRate.to_html(classes='table table-stripped')

######## Section for Analytics ############

""" Mortgage payment = (P * r * (1 + r)^n) / ((1 + r)^n - 1)
where:

P is the principal (the amount of the loan)
r is the monthly interest rate (annual interest rate divided by 12)
n is the total number of payments (the number of years of the loan multiplied by 12)
Note that this equation assumes a fixed-rate mortgage. If you have an adjustable-rate mortgage, the mortgage payment may change over time."""

option_1 = input("Do you have the monthly interest rate or the yearly? (0 for monthly, 1 for yearly)") or 1
if option_1 == 0:
    princible_rate = float(input("What is the interest rate?") or 6)
    princible_rate = princible_rate/(12/100)
elif option_1 == 1:
    princible_rate = float(input("What is the interest rate?") or 6)
    princible_rate = princible_rate/(100)
else:
    print("that is not a correct option")


initialpayment_Percent = int(input("How much (%) of the total value do you plan on puting down?") or 20)/100 
princible_loan_zest = float(zestimateHouse) * (1-initialpayment_Percent) 
numOfPayments = int(input("What is total amount of payments?") or 360) 

##print("princible" + princible_loan_zest)
print("princible_rate: " + str(princible_rate) +"\tinicialpayment%: " + str(initialpayment_Percent)+"\princible_loan_zest: " + str(princible_loan_zest)+ "\t# of payments: " + str(numOfPayments))

mortgage_payment_zest = (princible_loan_zest * initialpayment_Percent * princible_rate * (1 + princible_rate) ** numOfPayments)/((1 + princible_rate) ** (360-1))

pr(mortgage_payment_zest)


"""
Break-even point = Total cost of owning the property / Rental income per year
"""
breakEvenPoint = round(zestimateHouse/monthly_rentZestimate, 2)
print("zestimateHouse: "+ str(zestimateHouse)+ "\tmonthly_rentZestimate: "+ str(monthly_rentZestimate)+ "\nBreak Even Point: "+ str(breakEvenPoint))

"""
The cap rate is found by dividing the property's net operating expenses by its purchase price. You can find the cap rate by doing the following: 

Find your gross income by taking the average monthly rent for your property and multiplying it by 11.5. This will show the maximum amount you can make from the property, allowing for a two-week per year vacancy.

Then, subtract your monthly operating expenses ( utilities, taxes, maintenance) from your gross income to get your net income.

Divide your net income by the purchase price to find your cap rate.

Multiply the cap rate by 100 to find the percentage of your potential returns on the property.


"""

html_header_info_1 = "This report was run for: "+full_address 
html_header_info_2 = description_full
html_header_info_3 =" Additional calculations:\n" +" Princible Interest Rate: " + \
    str(princible_rate) +" Initial Loan Payment: " + str(initialpayment_Percent)+" Princible Loan Amount for Zestimate: " + str(princible_loan_zest) + \
        " # of payments: " + str(numOfPayments)
html_header_info_4 = " Breakeven Point: "+ str(breakEvenPoint) +" Morgage Payment bases on Zesimate: "+ str(mortgage_payment_zest)
"""

Section for table of PRoperty calculator

"""

house_prop_data = []
expenses_per_month=200

total_rent_income = monthly_rentZestimate *12
total_expenses = expenses_per_month *12
net_income = total_rent_income-total_expenses

##accumeulated values
accumulated_total_income = total_rent_income
accumulated_total_expense = total_expenses
accumulated_net_income = net_income

total_roi = ((zestimateHouse+ princible_loan_zest) +net_income)/(zestimateHouse+ princible_loan_zest)

house_prop_data.append({
        "Year": int(year_start_tax)+2,
        "Total Income": round(total_rent_income, 3),
        "Total Expenses": round(total_expenses, 3),
        "Net Income": round(net_income, 3),
        "Total ROI": round(total_roi, 3),
        "Acc. Total Income": round(accumulated_total_income, 3),
        "Acc. Total Expence": round(accumulated_total_expense, 3),
        "Acc. Total Net Income": round(accumulated_net_income, 3)
    })


for year in range(int(year_start_tax+3),(int(year_start_tax)+23)):

    total_rent_income *= 1.03
    total_expenses *= 1.03
    net_income *= 1.03

    total_roi = ((zestimateHouse+ princible_loan_zest) +net_income)/(zestimateHouse+ princible_loan_zest)

    accumulated_total_income += total_rent_income
    accumulated_total_expense += total_expenses
    accumulated_net_income += net_income

    house_prop_data.append({
            "Year": int(year+3),
            "Total Income": round(total_rent_income, 3),
            "Total Expenses": round(total_expenses, 3),
            "Net Income": round(net_income, 3),
            "Total ROI": round(total_roi, 3),
            "Acc. Total Income": round(accumulated_total_income, 3),
            "Acc. Total Expence": round(accumulated_total_expense, 3),
            "Acc. Total Net Income": round(accumulated_net_income, 3)
        })
df = pd.DataFrame(house_prop_data)

html_yr_calc_tb = df.to_html(classes='table table-stripped')
  
df.to_csv('house30yrinvestment.csv')


img_path = 'my_plots.png'
image_tag = f'<img src="{img_path}" alt="image" width="1200">'

table_html = df.to_html(classes='table table-stripped')


full_html = """
<!DOCTYPE html>
<html>
<head>
	<title>Real Estate Report</title>
    <style>
		.img-container {
			display: flex;
			flex-direction: row;
            align-items: center;
			justify-content: center;
		}
		.img-container img {
			margin-right: 10px;
		}
        .label {
			text-align: Center;
			font-size: 16px;
			font-weight: bold;
		}
	</style>
    <style>
		.highlight {
			background-color: red;
			font-weight: bold;
		}
	</style>
</head>
<body>
	<h1>"""  +f"""</h1>
	<h1>This report was run for the Address: {streetAddress}, {city_address} {state_address}</h1>
	<p>Description: {description_full}.<br><br>
    Monthly Rent Estimate: <span class="highlight">{monthly_rentZestimate}</span>.<br><br>
    Princible Loan from Zestimate: <span class="highlight">{princible_loan_zest}</span>&emsp;Last Sold Price: <span class="highlight">{lastSoldPrice}</span>&emsp;<br>Zillow's Estimate on House Cost: <span style="color: blue;">{zestimateHouse}</span><br>House Sqft: <span style="color: blue;">{house_sqft}</span><br>Zestimate Price/Sqft: <span class="highlight">{round(zestimateHouse/house_sqft,2)} sqft</span>
    <br><br>
    Monthyl HOA Fee: <span class="highlight">{monthly_HoaFee}</span>
    <br><br>
    Mortgage payment = (P * r * (1 + r)^n) / ((1 + r)^n - 1)
    &emsp;P is the principal (the amount of the loan)
    &emsp;r is the monthly interest rate (annual interest rate divided by 12)
    &emsp;n is the total number of payments (the number of years of the loan multiplied by 12)
    <br>Morgage Payment Estimate: <span style="color: blue;">{mortgage_payment_zest}</span>
    <br><br>Break-even point = Total cost of owning the property / Rental income per year
    <br>BreakEven Point: <span style="color: blue;">{breakEvenPoint}</span>
    </p>
   
    <div class="img-container">
		<div>
			<img src="my_plots_taxRates.png" alt="Image 1">
			<p class="label">Esimated Future Tax Rate Changes:"""+table_TaxRate_html +"""</p>
		</div>
		<div>
			<img src="my_plots_Tax_Values.png" alt="Image 2">
			<p class="label">Esimated Future Tax Values: """+ table_TaxValue_html+""":</p>
		</div>
	</div>
    <div>
    <p class="label">"""+ table_html +"""</p>
    </div>
</body>
</html>
"""

# Save the HTML code to a file
with open('result.html', 'w') as f:
    f.write(full_html)

# open the HTML page in a new tab in the default web browser
webbrowser.open_new_tab("result.html")